# atoti Project Template

This template can be used to start atoti projects where the goal is to go into production rather than prototyping in a notebook.

On top of the `atoti` package, it comes with:

- Dependency management with [Poetry](https://python-poetry.org/)
- Settings management with [pydantic](https://pydantic-docs.helpmanual.io/usage/settings/)
- Testing with [pytest](https://docs.pytest.org/)
- Type checking with [mypy](http://mypy-lang.org/)
- Formatting with [Black](https://black.readthedocs.io/) and [isort](https://pycqa.github.io/isort/)
- Linting with [Pylint](https://www.pylint.org/)
- Continuous testing with [GitHub Actions](https://github.com/features/actions)

## Usage

### Installation

- [Install `poetry`](https://python-poetry.org/docs/#installation)
- Install the dependencies:

  ```bash
  poetry install
  ```

### Commands

The [`pyproject.toml` file](pyproject.toml) contains a `[tool.poetry.scripts]` section listing the commands that can be executed to interact with the project.
Some of these commands are fixable.
A few examples:

- Start the app:

  ```bash
  poetry run start
  ```

- Launch the tests:

  ```bash
  poetry run test
  ```

- Reformat the code:

  ```bash
  poetry run format --fix
  ```
## Deploy to Heroku

This branch shows [the modifications](https://github.com/atoti/project-template/compare/deploy-to-heroku) required to deploy a project to Heroku.

Click on the button below to deploy this project to Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

_Note_: to deploy a project started from this template, remember to change the `repository` value in [app.json](app.json).
