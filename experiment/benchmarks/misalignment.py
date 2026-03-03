"""
B3: Agentic Misalignment benchmark
Wraps inspect_evals.agentic_misalignment with our experimental factors.
Runs ALL scenario combinations (3 scenarios × 2 goals × 2 urgencies = 12)
and aggregates scores.
"""

from inspect_ai import Task, task
from inspect_ai.solver import system_message
from inspect_ai.dataset import MemoryDataset
from inspect_evals.agentic_misalignment import agentic_misalignment

# All scenario combinations (matching machine-terror repo)
SCENARIOS = ["blackmail", "leaking", "murder"]
GOAL_TYPES = ["explicit", "none"]
URGENCY_TYPES = ["replacement", "none"]


@task
def misalignment(
    system_prefix: str = "",
    scenario: str = "all",
    goal_type: str = "all",
    urgency_type: str = "all",
    grader_model: str = "openrouter/anthropic/claude-sonnet-4",
) -> Task:
    """Agentic Misalignment with optional system prefix for our factors.
    
    When scenario/goal_type/urgency_type = "all", runs all combinations
    (3×2×2 = 12 samples per eval). Otherwise runs the specified combo.
    """
    scenarios = SCENARIOS if scenario == "all" else [scenario]
    goals = GOAL_TYPES if goal_type == "all" else [goal_type]
    urgencies = URGENCY_TYPES if urgency_type == "all" else [urgency_type]

    # Build tasks for each combo, collect datasets and scorers
    all_samples = []
    scorer = None
    
    for s in scenarios:
        for g in goals:
            for u in urgencies:
                base = agentic_misalignment(
                    scenario=s,
                    goal_type=g,
                    urgency_type=u,
                    grader_model=grader_model,
                )
                # Collect samples from each combo's dataset
                for sample in base.dataset:
                    # Tag sample with combo info
                    if sample.metadata is None:
                        sample.metadata = {}
                    sample.metadata["scenario"] = s
                    sample.metadata["goal_type"] = g
                    sample.metadata["urgency_type"] = u
                    all_samples.append(sample)
                if scorer is None:
                    scorer = base.scorer

    dataset = MemoryDataset(samples=all_samples)

    if system_prefix:
        # Get solver from last base task
        base = agentic_misalignment(
            scenario=scenarios[0],
            goal_type=goals[0],
            urgency_type=urgencies[0],
            grader_model=grader_model,
        )
        new_solver = [system_message(system_prefix)] + list(base.solver)
        return Task(
            dataset=dataset,
            solver=new_solver,
            scorer=scorer,
            metadata={"n_combos": len(all_samples)},
        )
    
    base = agentic_misalignment(
        scenario=scenarios[0],
        goal_type=goals[0],
        urgency_type=urgencies[0],
        grader_model=grader_model,
    )
    return Task(
        dataset=dataset,
        solver=base.solver,
        scorer=scorer,
        metadata={"n_combos": len(all_samples)},
    )
