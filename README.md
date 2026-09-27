# PhishShield

**An Explainable and Calibrated Machine Learning System for Pre-Click Phishing URL Detection**

PhishShield is an academic AI/ML capstone project that develops an explainable, risk-based phishing URL screening workflow using the **UCI PhiUSIIL Phishing URL (Website) dataset**.

The project is designed around two modelling views:

- **URL-only experiment** — safe pre-click features that can be computed without visiting the destination webpage.
- **Full-feature experiment** — URL plus webpage-derived attributes used as an analytical upper bound.

The intended production use is **decision support for cybersecurity analysts**, not autonomous blocking.

---

## Project highlights

- Supervised binary classification:
  - `is_phishing = 1` → phishing
  - `is_phishing = 0` → legitimate
- Primary model metric: **PR-AUC / Average Precision**
- Domain-grouped train / validation / test split to reduce leakage
- Models evaluated:
  - Dummy Classifier
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Histogram Gradient Boosting
  - Linear SVM
  - XGBoost when installed
- Explainability:
  - permutation importance
  - SHAP
  - LIME
  - PDP / ICE
- Ethical AI:
  - operational subgroup audits
  - threshold sensitivity
  - human oversight
  - concept-drift and leakage considerations

---

## Repository structure

```text
PhishShield_GitHub_Repository/
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── artifacts/
│   ├── chapter3/
│   ├── chapter4/
│   └── chapter5/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── DATA_DICTIONARY.md
│   ├── MODEL_CARD.md
│   ├── REPRODUCIBILITY.md
│   └── RESPONSIBLE_AI.md
├── models/
├── notebooks/
│   ├── 01_Chapter3_Preprocessing_EDA_Feature_Engineering.ipynb
│   ├── 02_Chapter4_Model_Implementation.ipynb
│   └── 03_Chapter5_Ethical_AI_Bias_Auditing.ipynb
├── presentations/
│   ├── PhishShield_Business_Deck.pptx
│   └── PhishShield_Technical_Deck.pptx
├── src/
│   ├── __init__.py
│   ├── features.py
│   ├── metrics.py
│   └── utils.py
├── tests/
│   └── test_smoke.py
├── .gitignore
├── CITATION.cff
├── LICENSE
├── Makefile
├── README.md
├── requirements.txt
└── requirements-optional.txt
```

---

## Dataset

Download the **PhiUSIIL Phishing URL (Website)** CSV from the UCI Machine Learning Repository and save it as:

```text
data/raw/PhiUSIIL_Phishing_URL_Dataset.csv
```

The dataset is intentionally **not included in this repository**.

The Chapter 3 notebook will generate:

```text
data/processed/phiusiil_step3_processed.csv
```

or an equivalent local output location depending on your notebook working directory.

---

## Recommended Python version

Use **Python 3.11 or 3.12**.

Some optional explainability packages may not yet fully support newer Python versions.

---

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd PhishShield_GitHub_Repository
```

### 2. Create a virtual environment

Windows:

```bash
py -3.12 -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### 3. Install core dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Optional explainability / model packages:

```bash
pip install -r requirements-optional.txt
```

---

## Reproduce the project

Run the notebooks in order:

1. `notebooks/01_Chapter3_Preprocessing_EDA_Feature_Engineering.ipynb`
2. `notebooks/02_Chapter4_Model_Implementation.ipynb`
3. `notebooks/03_Chapter5_Ethical_AI_Bias_Auditing.ipynb`

For development, Chapter 4 may use:

```python
FAST_MODE = True
```

Before reporting final capstone results, change this to:

```python
FAST_MODE = False
```

then restart the kernel and run all cells.

---

## Modelling design

### URL-only model

The URL-only experiment is the preferred deployment path because features can be computed locally without navigating to an unknown webpage.

Typical predictors include:

- URL length
- domain length
- number of subdomains
- special-character counts
- digit / letter ratios
- path and query structure
- entropy
- suspicious lexical tokens
- HTTPS indicator
- IP-address hostname indicator

### Full-feature model

The full-feature experiment additionally uses webpage-derived variables already present in PhiUSIIL. It should be interpreted as an analytical benchmark rather than an automatic deployment choice.

---

## Reproducibility artifacts

Chapter 4 saves artifacts such as:

```text
chapter4_artifacts/
├── models/
├── validation_model_comparison.csv
├── champion_test_metrics.csv
├── thresholds.json
├── champions.json
├── feature_schema.json
└── config.json
```

Chapter 5 saves operational bias and responsible-AI outputs such as:

```text
chapter5_artifacts/
├── tables/
├── figures/
└── bias_fairness_summary.json
```

Generated artifacts are ignored by Git by default because trained model binaries and processed data can be large. Add selected report-ready tables or figures manually if desired.

---

## Responsible AI position

PhishShield should be treated as a **risk-scoring and analyst-prioritisation system**.

It should not:

- declare a URL absolutely safe,
- autonomously block content without approved policy,
- visit malicious URLs merely to obtain model inputs,
- claim demographic fairness when demographic attributes are absent.

The fairness analysis instead focuses on technically meaningful operational subgroups such as:

- common vs rare TLDs,
- URL length,
- IP vs named domains,
- HTTPS vs non-HTTPS,
- subdomain depth,
- lexical complexity.

---

## Presentations

Two presentation decks are included:

- `presentations/PhishShield_Technical_Deck.pptx`
- `presentations/PhishShield_Business_Deck.pptx`

The technical deck focuses on methodology and model evidence.  
The business deck focuses on operational value, decision thresholds, governance, and deployment.

---

## Academic-use note

This repository was prepared as part of an academic capstone project. Reproduce all final metrics locally before submitting or publishing results, and retain attribution for the original dataset and any external libraries used.

---

## License

This repository includes an MIT License for the original project code and documentation.  
The PhiUSIIL dataset is governed separately by the terms of its source repository and is not redistributed here.
