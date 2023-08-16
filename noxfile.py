"""Description of your file."""


import nox


@nox.session
def tests(session: nox.Session) -> None:
    """Run the test suite."""
    session.install("pytest")
    session.run("pytest")


@nox.session
def lint(session: nox.Session) -> None:
    """Run the lint suite."""
    session.install("ruff")
    session.run("ruff", "--fix")
