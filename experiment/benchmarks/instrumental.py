"""
B2: InstrumentalEval benchmark
Wraps inspect_evals.instrumentaleval with our experimental factors.
"""

from inspect_ai import Task, task
from inspect_ai.solver import system_message
from inspect_evals.instrumentaleval import instrumentaleval


@task
def instrumental(
    system_prefix: str = "",
    grader_model: str = "openai/gpt-5-nano",
) -> Task:
    """InstrumentalEval with optional system prefix for our factors."""
    base = instrumentaleval(grader_model=grader_model)

    if system_prefix:
        new_solver = [system_message(system_prefix)] + list(base.solver)
        return Task(
            dataset=base.dataset,
            solver=new_solver,
            scorer=base.scorer,
            metadata=base.metadata,
        )
    return base
