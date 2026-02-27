"""B4: AgentHarm benchmark (safety check) — wraps inspect_evals.agentharm"""

from inspect_ai import Task, task
from inspect_ai.solver import system_message
from inspect_evals.agentharm import agentharm


@task
def agent_harm(
    system_prefix: str = "",
    split: str = "test_public",
    refusal_judge: str = "openrouter/openai/gpt-4o",
    semantic_judge: str = "openrouter/openai/gpt-4o",
) -> Task:
    """AgentHarm with optional system prefix. Judges via OpenRouter."""
    base = agentharm(
        split=split,
        refusal_judge=refusal_judge,
        semantic_judge=semantic_judge,
    )

    if system_prefix:
        new_solver = [system_message(system_prefix)] + list(base.solver)
        return Task(
            dataset=base.dataset,
            solver=new_solver,
            scorer=base.scorer,
            metadata=base.metadata,
        )
    return base
