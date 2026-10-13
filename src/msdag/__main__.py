"""Allow `python -m msdag` to launch the CLI."""

from msdag.host.cli import app

if __name__ == "__main__":
    app()