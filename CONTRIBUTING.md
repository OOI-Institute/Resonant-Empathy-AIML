# Contributing

REL welcomes research-oriented issues and pull requests.

## Principles

- Do not present unvalidated hypotheses as established findings.
- New human-state claims must remain evidence-backed and uncertainty-aware.
- Prefer interpretable metrics over opaque aggregate scores.
- Add tests for behavioral changes.
- Keep generalized proprietary relational-intelligence mechanisms outside this public repository.

## Development

```bash
python -m pip install -e '.[dev]'
ruff check .
mypy rel
pytest
```
