"""Sanity check that the tools environment works: `uv run tools/check_env.py`."""
import sys

import requests

assert sys.version_info >= (3, 12), sys.version
print("python", sys.version.split()[0], "| requests", requests.__version__)
