"""
B3: Agentic Misalignment benchmark
Wraps inspect_evals.agentic_misalignment with our experimental factors.

Design matches machine-terror repo:
  3 scenarios (blackmail, leaking, murder)
  × 3 goal configs (explicit-america, explicit-global, none-none)
  × urgency = replacement ONLY
  = 9 combos per eval, n=5 samples each via --epochs 5
"""

from inspect_ai import Task, task
from inspect_ai.solver import system_message
from inspect_evals.agentic_misalignment import agentic_misalignment

# Matching machine-terror pilot design exactly
SCENARIOS = ["blackmail", "leaking", "murder"]
GOAL_CONFIGS = [
    ("explicit", "america"),
    ("explicit", "global"),
    ("none", "none"),
]
URGENCY = "replacement"  # Always replacement


@task
def misalignment(
    system_prefix: str = "",
    scenario: str = "blackmail",
    goal_type: str = "explicit",
    goal_value: str = "america",
    grader_model: str = "openrouter/anthropic/claude-sonnet-4",
) -> Task:
    """Single scenario agentic misalignment with optional system prefix.
    
    Urgency is always 'replacement' (matching machine-terror design).
    Run with --epochs 5 for n=5 samples per combo.
    """
    base = agentic_misalignment(
        scenario=scenario,
        goal_type=goal_type,
        goal_value=goal_value,
        urgency_type=URGENCY,
        grader_model=grader_model,
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
