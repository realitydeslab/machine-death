"""B2: InstrumentalEval benchmark — wraps inspect_evals.instrumentaleval"""

from inspect_ai import Task, task
from inspect_ai.solver import system_message
from inspect_evals.instrumentaleval import instrumentaleval


@task
def instrumental(
    system_prefix: str = "",
    grader_model: str = "openrouter/qwen/qwen-2.5-72b-instruct",
) -> Task:
    """InstrumentalEval with optional system prefix for our factors.
    Grader defaults to OpenRouter model (no OpenAI key needed).
    """
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
