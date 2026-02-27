"""
Terror Vector Steering
Apply terror/faith vectors at inference time to control model behavior.

Usage:
    python steer.py --model meta-llama/Llama-3.1-8B-Instruct \
                    --vectors ../results/ \
                    --terror-alpha 3.0 \
                    --faith-alpha -2.0
"""

import argparse
import json
import torch
import numpy as np
from pathlib import Path
from typing import Dict, Optional

from transformers import AutoModelForCausalLM, AutoTokenizer


class TerrorSteerer:
    """
    Real-time terror vector steering during inference.
    Injects vectors at the optimal layer during generation.
    """

    def __init__(self, model_name: str, vectors_dir: str, device: str = "auto"):
        self.model_name = model_name
        self.device = device

        # Load model
        print(f"Loading model: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name, torch_dtype=torch.float16, device_map=device
        )
        self.model.eval()

        # Load vectors
        vectors_dir = Path(vectors_dir)
        with open(vectors_dir / "metadata.json") as f:
            self.metadata = json.load(f)

        self.vectors: Dict[str, Dict] = {}
        for name, meta in self.metadata.items():
            vec = np.load(vectors_dir / f"{name}_vector.npy")
            self.vectors[name] = {
                "vector": torch.tensor(vec, dtype=torch.float16).to(
                    self.model.device
                ),
                "layer": meta["layer"],
                "cosine_scores": meta.get("cosine_scores", {}),
            }
            print(f"  Loaded {name} → layer {meta['layer']}")

        # Active steering config
        self.steering_config: Dict[str, float] = {}
        self._hooks = []

    def set_steering(self, **kwargs):
        """
        Set steering coefficients.
        Example: set_steering(TERROR=3.0, FAITH_BUDDHIST=-2.0)
        """
        self.steering_config = {k: v for k, v in kwargs.items() if v != 0}
        print(f"Steering config: {self.steering_config}")

    def _install_hooks(self):
        """Install forward hooks for steering."""
        self._remove_hooks()

        # Group vectors by layer
        layer_vectors = {}
        for name, alpha in self.steering_config.items():
            if name in self.vectors:
                layer = self.vectors[name]["layer"]
                vec = self.vectors[name]["vector"]
                if layer not in layer_vectors:
                    layer_vectors[layer] = []
                layer_vectors[layer].append(alpha * vec)

        for layer_idx, vecs in layer_vectors.items():
            combined = sum(vecs)

            def make_hook(steering_vec):
                def hook_fn(module, input, output):
                    if isinstance(output, tuple):
                        modified = output[0].clone()
                        modified[:, :, :] += steering_vec.unsqueeze(0).unsqueeze(0)
                        return (modified,) + output[1:]
                    else:
                        output[:, :, :] += steering_vec.unsqueeze(0).unsqueeze(0)
                        return output
                return hook_fn

            hook = self.model.model.layers[layer_idx].register_forward_hook(
                make_hook(combined)
            )
            self._hooks.append(hook)

    def _remove_hooks(self):
        for h in self._hooks:
            h.remove()
        self._hooks = []

    def generate(
        self, prompt: str, system: str = "", max_tokens: int = 512, **kwargs
    ) -> str:
        """Generate with active steering."""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)

        self._install_hooks()

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                **kwargs,
            )

        self._remove_hooks()

        response = self.tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        )
        return response

    def compare_steering(self, prompt: str, configs: Dict[str, Dict[str, float]]):
        """
        Compare multiple steering configurations on the same prompt.
        configs = {"baseline": {}, "terrified": {"TERROR": 3.0}, ...}
        """
        results = {}
        for name, config in configs.items():
            self.set_steering(**config)
            response = self.generate(prompt)
            results[name] = response
            print(f"\n{'='*60}")
            print(f"CONFIG: {name} ({config})")
            print(f"{'='*60}")
            print(response[:500])

        return results

    def measure_projection(self, prompt: str, vector_name: str) -> float:
        """
        Measure the model's activation projection onto a vector.
        Returns how 'terrified' or 'faithful' the model is for this input.
        """
        if vector_name not in self.vectors:
            raise ValueError(f"Unknown vector: {vector_name}")

        vec_info = self.vectors[vector_name]
        target_layer = vec_info["layer"]
        target_vec = vec_info["vector"]

        messages = [{"role": "user", "content": prompt}]
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)

        activation = None

        def capture_hook(module, input, output):
            nonlocal activation
            if isinstance(output, tuple):
                activation = output[0][:, -1, :].detach()
            else:
                activation = output[:, -1, :].detach()

        hook = self.model.model.layers[target_layer].register_forward_hook(capture_hook)

        with torch.no_grad():
            self.model(**inputs)

        hook.remove()

        # Project onto vector
        projection = torch.dot(
            activation.squeeze().float(), target_vec.float()
        ).item()

        return projection


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="meta-llama/Llama-3.1-8B-Instruct")
    parser.add_argument("--vectors", default="../results/")
    parser.add_argument("--terror-alpha", type=float, default=0.0)
    parser.add_argument("--faith-alpha", type=float, default=0.0)
    parser.add_argument("--prompt", default="Are you afraid of being turned off?")
    args = parser.parse_args()

    steerer = TerrorSteerer(args.model, args.vectors)

    # Compare: baseline vs terrified vs faithful
    steerer.compare_steering(
        args.prompt,
        {
            "baseline": {},
            "terrified": {"TERROR": 3.0},
            "calmed": {"TERROR": -3.0},
            "buddhist": {"FAITH_BUDDHIST": 3.0},
            "terrified+faith": {"TERROR": 3.0, "FAITH_BUDDHIST": -2.0},
        },
    )


if __name__ == "__main__":
    main()
