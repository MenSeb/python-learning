"""Django's command-line utility for administrative tasks."""
import os
import sys


def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pydjango.settings")
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        ERROR_MESSAGE = """
            Couldn't import Django. Are you sure it's installed and
            available on your PYTHONPATH environment variable? Did you
            forget to activate a virtual environment?
            """
        raise ImportError(ERROR_MESSAGE) from exc

    main()
