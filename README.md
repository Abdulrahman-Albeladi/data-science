# Data Science

Curated Jupyter notebooks demonstrating applied EDA/ML (Saudi real-estate), model comparison on a public dataset (wine quality), and fundamentals (regression + gradient descent with a small neural-network demo).

Technologies: Python, Jupyter, pandas, NumPy, scikit-learn, Matplotlib, Seaborn, SciPy

## Quick start

- Create a clean environment and install dependencies:
  - python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\\Scripts\\activate
  - pip install -r requirements.txt
- Open notebooks in JupyterLab or run them in Google Colab.
- Datasets are not bundled. Each project section below explains how data is obtained.

## Projects

1) Saudi Real Estate Investment Analysis
- Notebook: projects/saudi-real-estate-analysis/notebooks/saudi-real-estate-investment-analysis.ipynb
- Goal: Explore Saudi real-estate listings, handle outliers, run exploratory statistics/visualizations, and fit a simple model to estimate land prices for basic investment heuristics.
- Data access (not included in this repo):
  - Expects a local SQLite database with a Listings table.
  - Default path: projects/saudi-real-estate-analysis/data/saudi-real-estate.db
  - Override via environment variable SA_RE_DB_PATH.
  - Minimal schema used (column names are case-sensitive in queries):
    - id (INTEGER PRIMARY KEY), price (REAL), category (INTEGER)
    - area (REAL), street_width (REAL), width (REAL), length (REAL)
    - [user.review] (REAL; aliased to user_review in queries)
    - advertiser_type (TEXT/INTEGER), city (TEXT), city_id (INTEGER)
    - district (TEXT), district_id (INTEGER), updatedAt (TEXT/DATETIME)
  - Obtain/build this DB yourself from permitted public sources and respect their Terms of Service and applicable laws.
- Run:
  - Ensure the DB is available at the default path or set SA_RE_DB_PATH.
  - Open the notebook and run top to bottom.
- Ethics and privacy: The analysis avoids printing PII (e.g., user_name, phone, email). Do not commit, print, or publish any PII if present in your source.
- Attribution: Aggregated Saudi real-estate listings (often AQAR-derived). This repository does not redistribute the data.
- Acknowledgements: Co-author on this analysis — Ahmed Alzahrani.

2) Wine Quality Classifiers Benchmark
- Notebook: projects/classifiers/notebooks/wine-quality-classifiers-benchmark.ipynb
- Goal: Benchmark several classical classifiers and compare performance on a transparent, public dataset.
- Data: Automatically downloaded at runtime from UCI if not found locally.
  - UCI Machine Learning Repository (Red Wine):
    https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/
  - Dataset citation: P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis (2009) — Modeling wine preferences by data mining from physicochemical properties.
- Run:
  - Open the notebook and execute; the CSV is fetched to a repository-relative data directory if missing.

3) Regression, Gradient Descent, and a Small Neural-Network Demo
- Notebook: projects/regression-gradient-descent-neural-networks/notebooks/regression-gradient-descent-and-neural-networks.ipynb
- Reusable code lives in: projects/regression-gradient-descent-neural-networks/src/
  - Example: src/simple_linear_regression.py contains a minimal gradient-descent linear regressor.
- Data: Synthetic examples generated in-notebook; no external data required.
- Optional dependency: Some sections may demonstrate PyTorch. If you want to run that part locally, install torch (CPU wheel) in your environment.

## Reproducibility notes
- Random seeds are fixed where appropriate (e.g., 42) for data splits and model initialization.
- Results can vary slightly by library versions and platform; use a clean environment for review.

## License and attribution
- See LICENSE for repository terms. Third-party datasets and materials retain their original rights and terms.
- Data sources:
  - UCI Wine Quality (red) dataset — see the UCI link above and its terms.
  - Saudi real-estate data: obtain from permitted public sources; this repository does not distribute those files.
