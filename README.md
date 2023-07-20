# pydantic-stuff

Learning Pydantic by writing some schemas that may be useful.

## Setup

```sh
# Simple install with virtual env
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Or with Poetry dependency manager
poetry install
```

## Sync requirements

```sh
# Generate requirements.txt from Poetry dependencies in pyproject.toml
# Maybe put this in CI later
poetry export -o requirements.txt --without-hashes --without-urls
```
