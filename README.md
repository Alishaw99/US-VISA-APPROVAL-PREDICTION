# Predict My US Visa


![GitHub repo size](https://img.shields.io/github/repo-size/Alishaw99/US-VISA-APPROVAL-PREDICTION)
![GitHub contributors](https://img.shields.io/github/contributors/scottydocs/README-template.md)
![GitHub Repo stars](https://img.shields.io/github/stars/Alishaw99/US-VISA-APPROVAL-PREDICTION)
![X Follow](https://img.shields.io/twitter/url?url=https%3A%2F%2Ftwitter.com%2Falishaw99&style=social)

"Predict My USA Visa" is a machine learning projection app to predict the approval likelihood of USA visa applications. Gain insights into approval factors, make informed decisions, and simplify the visa application process.

# Folder Structure

```bash
src/
|-- __init__.py

|-- components/
|   |-- __init__.py
|   |-- data_ingestion.py
|   |-- data_validation.py
|   |-- data_transformation.py
|   |-- model_trainer.py
|   |-- model_evaluation.py
|   |-- model_pusher.py

|-- configuration/
|   |-- __init__.py

|-- constants/
|   |-- __init__.py

|-- entity/
|   |-- __init__.py
|   |-- config_entity.py
|   |-- artifact_entity.py

|-- exception/
|   |-- __init__.py

|-- logger/
|   |-- __init__.py

|-- pipeline/
|   |-- __init__.py
|   |-- training_pipeline.py
|   |-- prediction_pipeline.py

|-- utils/
|   |-- __init__.py
|   |-- main_utils.py

|-- app.py
|-- requirements.txt
|-- Dockerfile
|-- .dockerignore
|-- demo.py
|-- setup.py

|-- config/
|   |-- model.yaml
|   |-- schema.yaml

```


# Project workflow

![](https://github.com/m-umairali/predict-my-usa-visa/blob/main/workflow.jfif)

# Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed VS Code`
* You have a `<Windows/Linux/Mac>`
* You have Docker installed.

# Installing

To run the project, follow these steps:

```bash
conda create -n usvisa python=3.8 -y
```
```bash
conda activate usvisa
```
```bash
pip install -r requirements.txt
```


## Using

To use follow these steps:

```
python app.py
```


## Contributing to this project:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

* [@Alishaw99](https://github.com/m-umairali) 🐛



## Contact

If you want to contact me you can reach me at tariqham@gmail.com

## License

This project uses the following license: [MIT](https://github.com/Alishaw99/US-VISA-APPROVAL-PREDICTION/edit/main/README.md).
