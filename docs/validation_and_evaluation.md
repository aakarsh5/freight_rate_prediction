# Validation and Evaluation Strategy

**Status:** Approved baseline\
**Version:** 1.0

## 1. Validation Principle

The labeled data covers January--October 2025, while the final
prediction period follows it.

Validation must therefore preserve chronological order:

> Train only on information available before the validation period.

Random train/test splitting and shuffled K-fold cross-validation will
not be used as the primary evaluation strategy.

## 2. Development Validation

Use expanding-window temporal validation:

  Fold   Training period   Validation period
  ------ ----------------- -------------------
  1      January--June     July
  2      January--July     August

These folds are used during model and feature development.

## 3. Model-Selection Validation

After initial development:

``` text
Train: January–August
Validate: September
```

September is used to compare promising approaches.

## 4. Final Holdout

October is reserved as the final labeled temporal holdout:

``` text
Train: January–September
Holdout: October
```

The holdout should not be repeatedly used for unrestricted model tuning.

## 5. Final Training

After the model is selected and the holdout has been evaluated:

``` text
Train final model: January–October
Predict: November–December
```

This uses all available labeled data before the final prediction period.

## 6. Sampling

No training-data sampling is required.

All available observations in each training period will be used.

Sampling may be used only to make visualizations readable and must not
affect model evaluation.

## 7. Primary Metric

### MAE --- Mean Absolute Error

``` text
MAE = mean(abs(actual - predicted))
```

MAE is the primary model-selection metric because it represents average
absolute prediction error in rate units.

## 8. Secondary Metric

### RMSE --- Root Mean Squared Error

``` text
RMSE = sqrt(mean((actual - predicted)^2))
```

RMSE is reported because large prediction errors are important and the
target contains extreme values.

## 9. Supporting Metrics

Also report:

-   R²
-   MAPE

These are diagnostics rather than primary selection criteria.

## 10. Model Selection Rule

Select the model primarily by:

1.  temporal-validation MAE;
2.  temporal-validation RMSE;
3.  stability across validation periods;
4.  ability to generalize to unseen routes and changed conditions;
5.  reasonable model complexity.

A model should not be selected because it performs exceptionally well on
only one validation period.

## 11. Leakage Rules

The following are prohibited:

-   using `load_id` as a predictive feature;
-   using future observations to create training features;
-   using validation-period target information during training;
-   calculating target-derived statistics using validation observations;
-   fitting preprocessing statistics on future validation data;
-   creating target-derived features without an out-of-fold/strictly
    historical procedure.

## 12. Holdout Interpretation

The goal is not to prove that overfitting is impossible.

The goal is to reduce the risk of: - model overfitting, - validation
overfitting, - temporal leakage, - optimistic performance estimates.

The October holdout provides the strongest labeled check of future-like
performance before final training.
