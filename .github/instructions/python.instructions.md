---
applyTo: "pyproject.toml,source/conf.py"
---

When editing Python or build configuration files in this repository:

- Keep compatibility with Python 3.12 or newer as defined in `pyproject.toml`.
- Prefer small, targeted configuration changes over broad refactors.
- Keep dependency declarations and related documentation in sync.
- Avoid adding tooling that duplicates the existing `uv` and Sphinx workflow unless the change explicitly requires it.
