# Project Documentation

This directory contains the core methodology documents for the
freight-rate prediction project.

## Documents

1.  [`01_problem_definition.md`](01_problem_definition.md)\
    Defines the prediction problem, data, constraints, and project
    objectives.

2.  [`02_validation_and_evaluation.md`](02_validation_and_evaluation.md)\
    Defines the temporal split, cross-validation, holdout, metrics, and
    leakage rules.

3.  [`03_model_experiment_plan.md`](03_model_experiment_plan.md)\
    Defines the baseline-to-final model experiment sequence and
    feature/target experiments.

## Documentation Principle

These documents intentionally separate:

``` text
What is the problem?
        ↓
How will we validate it?
        ↓
How will we choose the model?
```

Final measured results belong in the experiment log and final assessment
report, not in these methodology documents.
