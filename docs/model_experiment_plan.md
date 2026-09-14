# Model Experiment Plan

**Status:** Approved baseline\
**Version:** 1.0

## 1. Experiment Principle

Models will be developed incrementally.

Every meaningful experiment must use the same temporal validation splits
and record its metrics.

The final model will be selected from measured evidence rather than
assumed in advance.

## 2. Baselines

### Baseline 1 --- Global Median

Predict the training-set median rate for every observation.

Purpose: establish a minimum benchmark.

### Baseline 2 --- Distance Model

Use `distance` as the primary predictor.

Purpose: measure the predictive value of the strongest obvious freight
feature.

### Baseline 3 --- Ridge Regression

Use numerical features and encoded categorical features.

Purpose: establish an interpretable linear benchmark.

## 3. Candidate Models

Evaluate, as justified by baseline results:

1.  ExtraTrees or another tree-based regression baseline.
2.  CatBoost Regressor.

CatBoost is the leading candidate because the problem combines
categorical variables, numerical variables, missing values, nonlinear
relationships, and route interactions.

It remains a candidate until temporal validation confirms its advantage.

## 4. Feature Groups

Features will be added in controlled groups.

### Group A --- Core

-   pickup
-   delivery
-   equipment
-   distance
-   weight
-   market_index
-   quote_signal

### Group B --- Route

``` text
route = pickup + "__" + delivery
```

### Group C --- Geographic

-   latitude difference
-   longitude difference
-   absolute coordinate differences

### Group D --- Temporal

-   year
-   month
-   day
-   day of week
-   day of year
-   weekend indicator

Cyclical date features may be tested if useful.

## 5. Data-Quality Experiments

Missing values will not cause rows to be dropped automatically.

For invalid negative `weight`, compare:

1.  leave unchanged;
2.  treat as missing;
3.  treat as missing + `weight_invalid` indicator.

The selected treatment must be based on temporal validation.

Extreme target values will be investigated but not automatically
removed.

## 6. Target Formulations

If the direct-rate baseline is competitive, test:

### A. Direct rate

``` text
posted_rate = f(features)
```

### B. Rate per mile

``` text
rate_per_mile = posted_rate / distance
predicted_rate = predicted_rate_per_mile * distance
```

### C. Log target

Test only if the target distribution and validation results justify it.

## 7. Objective Experiments

For boosting models, compare robust and squared-error objectives where
supported:

-   MAE-oriented objective
-   RMSE-oriented objective

Evaluate all models using the same MAE and RMSE metrics.

## 8. Experiment Order

The preferred sequence is:

``` text
1. Data validation
2. Baselines
3. Temporal validation
4. Core features
5. Route features
6. Geographic features
7. Temporal features
8. Candidate models
9. Target formulations
10. Objective/hyperparameter tuning
11. Final model selection
12. October holdout
```

Do not start with extensive hyperparameter search.

## 9. Experiment Record

For each meaningful experiment record:

-   experiment ID;
-   model;
-   feature set;
-   target formulation;
-   objective;
-   validation folds;
-   MAE;
-   RMSE;
-   key observation;
-   decision.

Example:

  ID    Model      Features         Mean MAE   Mean RMSE Decision
  ----- ---------- -------------- ---------- ----------- -----------
  E01   Median     baseline                              Benchmark
  E02   Distance   distance                              Benchmark
  E03   Ridge      core                                  Compare
  E04   CatBoost   core                                  Compare
  E05   CatBoost   core + route                          Compare

## 10. Final Model Decision

The final model should:

-   outperform simple baselines;
-   perform consistently across temporal folds;
-   maintain acceptable October holdout performance;
-   handle missing values and unseen routes;
-   avoid leakage;
-   remain reproducible and reasonably simple.

Only after this decision will the model be retrained on all
January--October data and used for final predictions.
