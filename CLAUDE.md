# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

FAIR Wizard Integration SDK (`fair-wizard-integration-sdk`) — a Python SDK for building serverless automations that handle authentication events (SAML and OpenID Connect) in FAIR Wizard. Handlers follow the AWS Lambda signature `handler(event: dict, context) -> dict`.

## Build & Development

```bash
# Install locally (editable)
pip install -e .

# Install dependencies
pip install -r requirements.txt
```

Requires Python >=3.11, <4.

## Testing

Tests live in `tests/` with each subdirectory containing `test.py`, `handler.py`, and `func.py`:

```bash
# Run a single test (from its directory)
cd tests/saml_user_logged_in && python test.py
cd tests/openid_user_logged_in && python test.py
```

CI runs all tests via: `for d in tests/*/; do (cd "$d" && python test.py); done`

## Linting & Type Checking

```bash
# Flake8 (errors + complexity)
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --max-complexity=16 --max-line-length=200 --statistics

# MyPy
mypy --install-types --ignore-missing-imports --check-untyped-defs src/fair_wizard/
```

## Documentation

```bash
cd docs && pip install -r requirements.txt && make html
```

Docs hosted at https://integration-sdk.fair-wizard.com

## Architecture

The SDK uses a **handler factory pattern** with three layers:

1. **Models** (`model.py`) — Pydantic models for events and responses. All use `Field(alias='...')` for camelCase JSON serialization and `ConfigDict(populate_by_name=True)`.

2. **Wrappers** (`wrappers.py`) — Factory functions (`make_saml_user_logged_in_handler`, `make_openid_user_logged_in_handler`) that wrap user functions with Pydantic validation, timeout enforcement via `func_timeout`, exception handling, and serialization.

3. **Handlers** (`handlers.py`) — Default handler implementations.

Module layout under `src/fair_wizard/automation/`:
- `common/` — Shared response models (`AuthorizedUserResponse`, `ForbiddenResponse`, `ErrorResponse`), `HandlerContext`, and the generic `make_handler`/`make_error_handler` wrappers.
- `saml/` — SAML assertion models, attribute helpers (`get_first_name`, `get_last_name`, `get_email` which search by friendly name or OID URN).
- `openid/` — OpenID `IdToken` model with standard + custom claims (`otherClaims` dict).

Response serialization: all response models have `.serialize()` returning `model_dump(by_alias=True, mode='json')`.

## Key Conventions

- Python 3.11+ union syntax (`X | Y` not `Union[X, Y]`)
- Pydantic v2 models with camelCase field aliases
- Factory functions named `make_*_handler(func)`
- Type aliases for callable signatures (e.g., `ISAMLUserLoggedInFunction`)
- Lambda packaging via `make lambda-package` (creates layer with manylinux pydantic binaries)
