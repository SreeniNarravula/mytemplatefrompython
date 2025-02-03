# Python Template

A Python project template to save you time and energy.

[![Build Status](https://github.com/oneTakeda/devops-python-repository-template/workflows/build/badge.svg)](https://github.com/oneTakeda/devops-python-repository-template/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=oneTakeda_devops-python-repository-template&metric=alert_status&token=35f44dc5ad02eb732925ff374fc156e1ccb39987)](https://sonarcloud.io/summary/new_code?id=oneTakeda_devops-python-repository-template)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=oneTakeda_devops-python-repository-template&metric=coverage&token=35f44dc5ad02eb732925ff374fc156e1ccb39987)](https://sonarcloud.io/summary/new_code?id=oneTakeda_devops-python-repository-template)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=oneTakeda_devops-python-repository-template&metric=reliability_rating&token=35f44dc5ad02eb732925ff374fc156e1ccb39987)](https://sonarcloud.io/summary/new_code?id=oneTakeda_devops-python-repository-template)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=oneTakeda_devops-python-repository-template&metric=security_rating&token=35f44dc5ad02eb732925ff374fc156e1ccb39987)](https://sonarcloud.io/summary/new_code?id=oneTakeda_devops-python-repository-template)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=oneTakeda_devops-python-repository-template&metric=sqale_rating&token=35f44dc5ad02eb732925ff374fc156e1ccb39987)](https://sonarcloud.io/summary/new_code?id=oneTakeda_devops-python-repository-template)

## Install

Request a new GitHub Repository via [Issue Form](https://github.com/oneTakeda/devops-repo-automation/issues/new?assignees=&labels=python&projects=&template=a2-repo-create-request-form.yml&title=%5BGitHub+Repository+Creation+Request%5D%3A+Create%20Repo%20from%20Python%20Template) and select this template from the dropdown along with the rest of the information needed.

## Usage

### File configuration

1. Configure the `setup.cfg` file
1. Configure the `.github/workflows/build.yml` file
1. Uncomment the `publish` step of the `.github/workflows/release.yml` file
1. Update this `README.md` with your own info
1. Rename/replace other files/folders as needed and configure their content
1. Modify .pre-commit-config.yaml as needed and run `pre-commit install`

### GitHub configuration

1. Add GitHub Repository secrets for `PYPI_REPO_TOKEN` and `PYPI_REPO_URL` so that the `release` job in `.github/workflows/release.yml` may publish your package.

### Local setup

1. You can build using `pip install build && python -m build` and install dependencies with `pip install -e .[dev]`
