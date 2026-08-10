"""Entry point that runs the Titanic serving app with uvicorn.

This is the target of the Pants ``pex_binary`` (see ``serving/BUILD``) and is
also runnable directly::

    PYTHONPATH=projects/machine-learning/titanic python -m serving.main
"""

import os

import uvicorn

from serving.app import app

HOST = os.environ.get("TITANIC_SERVE_HOST", "0.0.0.0")
PORT = int(os.environ.get("TITANIC_SERVE_PORT", "8000"))


def main() -> None:
    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
