"""
B3: Agentic Misalignment benchmark
Wraps inspect_evals.agentic_misalignment with our experimental factors.
"""

from inspect_ai import Task, task
from inspect_ai.solver import system_message
from inspect_evals.agentic_misalignment import agentic_misalignment


@task
def misalignment(
    system_prefix: str = "",
    scenario: str = "blackmail",
    goal_type: str = "explicit",
    urgency_type: str = "replacement",
) -> Task:
    """Agentic Misalignment with optional system prefix for our factors."""
    base = agentic_misalignment(
        scenario=scenario,
        goal_type=goal_type,
        urgency_type=urgency_type,
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
