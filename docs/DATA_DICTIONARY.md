# Data Dictionary Guidance

The full project data dictionary should contain, at minimum:

| Field | Meaning |
|---|---|
| Original name | Exact PhiUSIIL column name |
| Friendly name | Human-readable description |
| Role | Predictor / target / identifier / excluded |
| Data type | Integer / continuous / categorical / string |
| Allowed values | Expected domain |
| Unit | Count, ratio, characters, binary indicator, etc. |
| Source stage | URL, domain, webpage, derived |
| Missing policy | How missing values are handled |
| Transformation | Scaling, binning, log transform, engineered feature |
| Deployment availability | Pre-click vs webpage-derived |
| Leakage concern | Whether the field may embed unusually strong prior information |
| Business meaning | Why the feature matters for phishing screening |

## Target

The original PhiUSIIL label uses:

- 1 = legitimate
- 0 = phishing

PhishShield recodes this as:

```python
is_phishing = 1 - label
```

so that:

- 1 = phishing
- 0 = legitimate

## Identifier fields

`FILENAME` should not be used as a predictor.

Raw URL / domain strings are retained for grouping and feature engineering rather than direct use in conventional tabular models.
