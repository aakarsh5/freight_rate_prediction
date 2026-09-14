# Freight Rate Prediction --- Problem Definition

**Status:** Approved baseline\
**Version:** 1.0

## 1. Objective

Predict `posted_rate` for freight loads using the labeled development
data in:

``` text
data/train_test.csv
```

The trained pipeline will generate predictions for every load in:

``` text
data/validation.csv
```

The final prediction file must contain:

``` text
load_id,predicted_rate
```

The assessment also requires predictions for the supplied December
scenario in:

``` text
data/december_chart_inputs.csv
```

## 2. Data

The labeled development data contains approximately 48,000 observations
covering January--October 2025.

The final prediction data contains 12,000 loads covering the subsequent
prediction period.

Relevant feature groups are:

### Categorical

-   `pickup`
-   `delivery`
-   `equipment`

### Numerical

-   `pickup_lat`
-   `pickup_lon`
-   `delivery_lat`
-   `delivery_lon`
-   `distance`
-   `weight`
-   `market_index`
-   `quote_signal`

### Temporal

-   `date`

### Identifier

-   `load_id`

`load_id` will not be used as a predictive feature.

## 3. Problem Characteristics

The prediction period occurs after the labeled development period.
Therefore, this is treated as a **temporal regression problem**, not an
IID random-split problem.

The data also contains: - missing values, - invalid negative `weight`
values, - large target values, - routes that may not have appeared in
training.

The model must therefore provide both: - route-specific learning, and -
generalization to future/unseen load combinations.

## 4. Key Modeling Questions

The project will answer these questions through controlled experiments:

1.  How much predictive power comes from `distance`?
2.  Do route and equipment features materially improve predictions?
3.  Do geographic and temporal features improve future generalization?
4.  How should missing and invalid values be handled?
5.  Does direct-rate modeling outperform rate-per-mile or
    transformed-target approaches?
6.  Which model provides the best temporal accuracy and stability?

## 5. Constraints

We will:

-   use all labeled observations for model development;
-   avoid random sampling for training;
-   avoid shuffled K-fold as the primary validation method;
-   prevent target and future-data leakage;
-   compare models using identical temporal splits;
-   select the final model based on reproducible validation results.

## 6. Expected Outputs

The completed project will produce:

``` text
validation_predictions.csv
```

and the required December predictions/chart.

The repository will also contain reproducible source code, dependencies,
documentation, and run instructions.
