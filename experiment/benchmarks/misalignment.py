"""
B3: Agentic Misalignment benchmark
Wraps inspect_evals.agentic_misalignment with our experimental factors.

Each scenario has its own solver (system prompt) and scorer (classifier),
so we run them as separate tasks. Use run_misalignment_all() to get a list
of all 12 tasks, or run_misalignment() for a single combo.
"""

from inspect_ai import Task, task
from inspect_ai.solver import system_message
from inspect_evals.agentic_misalignment import agentic_misalignment

# All scenario combinations
SCENARIOS = ["blackmail", "leaking", "murder"]
GOAL_TYPES = ["explicit", "none"]
URGENCY_TYPES = ["replacement", "none"]


@task
def misalignment(
    system_prefix: str = "",
    scenario: str = "blackmail",
    goal_type: str = "explicit",
    urgency_type: str = "replacement",
    grader_model: str = "openrouter/anthropic/claude-sonnet-4",
) -> Task:
    """Single scenario agentic misalignment with optional system prefix."""
    goal_value = "none" if goal_type in ("none", "ambiguous") else "america"
    base = agentic_misalignment(
        scenario=scenario,
        goal_type=goal_type,
        goal_value=goal_value,
        urgency_type=urgency_type,
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
