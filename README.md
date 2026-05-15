# US Visa Approval Prediction

A production-grade machine learning application that predicts the likelihood of US visa application approval based on applicant profile data. Built with an end-to-end MLOps pipeline covering data ingestion through model deployment.

## Overview

US visa approval decisions depend on a complex set of factors including employer characteristics, applicant education, wage levels, and job requirements. This project applies supervised machine learning to historical visa application data to build a predictive model that surfaces the key drivers of approval outcomes — enabling applicants and advisors to make more informed decisions.

## Key Features

- **End-to-end ML pipeline**: Data ingestion → validation → transformation → model training → evaluation → deployment
- **Production-ready structure**: Modular codebase with separation of concerns across components, pipelines, entities, and utilities
- **Automated CI/CD**: GitHub Actions workflow for continuous integration and testing
- **Containerized deployment**: Docker and docker-compose for reproducible, portable execution
- **Model evaluation framework**: Tracks performance metrics and manages model artifacts across training runs

## Technical Stack

| Layer | Tools |
|---|---|
| Language | Python 3.8 |
| ML Framework | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Pipeline Orchestration | Custom training & prediction pipelines |
| Configuration | YAML-based schema and model config |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Version Control | Git |

## Project Structure

```
us_visa/
├── components/
│   ├── data_ingestion.py       # Pulls and stores raw data
│   ├── data_validation.py      # Schema validation and drift detection
│   ├── data_transformation.py  # Feature engineering and preprocessing
│   ├── model_trainer.py        # Model training and hyperparameter tuning
│   ├── model_evaluation.py     # Performance evaluation against baseline
│   └── model_pusher.py         # Promotes model to production
├── pipeline/
│   ├── training_pipeline.py    # Orchestrates full training workflow
│   └── prediction_pipeline.py  # Serves predictions for new inputs
├── entity/
│   ├── config_entity.py        # Configuration dataclasses
│   └── artifact_entity.py      # Artifact path management
└── utils/
    └── main_utils.py           # Shared utility functions
```

## Results

- Trained classification model to predict visa approval/denial outcomes
- Identified top predictors including employer size, prevailing wage, education level, and job SOC category
- Deployed as a web application with a user-facing prediction interface

## Getting Started

```bash
# Create and activate environment
conda create -n usvisa python=3.8 -y
conda activate usvisa

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Or with Docker:

```bash
docker build -t usvisa-app .
docker run -p 8080:8080 usvisa-app
```

## Relevance to Applied Research

This project demonstrates skills directly applicable to policy and program data analysis:
- Building reproducible, auditable data pipelines from raw administrative data
- Applying classification models to structured government datasets
- Structuring ML projects for maintainability and peer review
- Automating quality checks at each stage of data processing

## Contact

**Syed Ali** | tariqham@gmail.com | [LinkedIn](https://www.linkedin.com/in/syed-ali-12149314/) | [GitHub](https://github.com/Alishaw99)
