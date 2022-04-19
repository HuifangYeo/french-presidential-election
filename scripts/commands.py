from .run_command import run_command

_PACKAGES = ("app", "scripts", "tests")


def format() -> None:  # pylint: disable=redefined-builtin
    run_command("poetry", "run", "black", ".", check_args=["--check"])


def lint() -> None:
    run_command("poetry", "run", "pylint", "--jobs=0", *_PACKAGES)


def sort_imports() -> None:
    run_command("poetry", "run", "isort", "--gitignore", ".", check_args=["--check"])


def start() -> None:
    run_command("poetry", "run", "python", "-m", "app")


def test() -> None:
    run_command("poetry", "run", "pytest")


def typecheck() -> None:
    run_command(
        "poetry",
        "run",
        "mypy",
        "--show-error-codes",
        *[arg for package in _PACKAGES for arg in ["--package", package]]
    )
