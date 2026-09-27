# Model Card — PhishShield

## Intended use

PhishShield is a cybersecurity decision-support system for estimating whether a submitted URL is likely to be phishing.

The recommended deployment path is the **URL-only champion model**, because its predictors can be derived without visiting the destination webpage.

## Intended users

- SOC analysts
- cybersecurity teams
- security operations personnel
- research / academic evaluators

## Out-of-scope use

- autonomous blocking without approved policy
- malware execution or analysis
- visiting suspicious live websites for feature collection
- threat-actor attribution
- demographic decision-making
- guarantees that a low-risk URL is safe

## Target

`is_phishing`

- 1 = phishing
- 0 = legitimate

## Primary evaluation metric

PR-AUC / Average Precision

Supporting metrics:

- recall
- precision
- F1
- ROC-AUC
- false-positive rate
- Brier score where probabilities are available
- inference latency

## Evaluation design

The project uses a domain-grouped train / validation / test split to reduce leakage from repeated or related domains.

The test set is kept locked until model and threshold selection are complete.

## Explainability

Supported techniques include:

- permutation importance
- SHAP
- LIME
- PDP
- ICE

## Fairness / bias position

The source records represent URLs and websites rather than people. The project therefore does not claim demographic fairness across gender, race, age, or socioeconomic status.

Operational subgroup auditing is used instead.

## Key risks

- dataset-source bias
- duplicate / related domains
- leakage from high-information derived variables
- overfitting
- concept drift
- mismatch between full-feature training inputs and URL-only production inputs
- automation bias

## Human oversight

Predictions should be presented as risk estimates and should support, not replace, analyst judgment.
