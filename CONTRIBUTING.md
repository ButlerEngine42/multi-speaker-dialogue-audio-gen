# Contributing to multi-speaker-dialogue-audio-gen

Thanks for wanting to help build the dialogue audio generator. This project
is a **plugin host**: the core does dialogue parsing, speaker routing, and
timeline assembly; everything that actually makes noise is an extension
module loaded at runtime.

## Repo layout

```
src/msdag/            # core host package
  host/               # bootstrap, plugin loader, registry
  dialogue/           # script parsing + speaker tagging
  render/             # timeline assembly, mixing, export
  backends/           # built-in TTS backends (plugin-shaped)
  contracts/          # shared ABCs + dataclasses every plugin imports
  utils/              # logging, audio io, config
  models/             # voice / speaker dataclasses
plugins/              # out-of-tree extension modules (drop-in)
config/               # default + user config
tests/                # pytest suite
```

## Adding a backend plugin

1. Subclass `msdag.contracts.backend.SynthesisBackend`.
2. Declare `PLUGIN_META` with `name`, `version`, `api_version`.
3. Drop the module under `plugins/` or install it as a package exposing
   the `msdag.backends` entry-point group.
4. The loader picks it up on next start — no core edits required.

## Dev setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
pytest -q
```

## Style

- Python 3.11+, type hints everywhere, `ruff` + `mypy` clean.
- No blocking calls on the render thread — synthesis is async.
- Every plugin boundary is a dataclass or an ABC, never a dict of vibes.

## PRs

Keep them small. One plugin, one fix, one contract change. If you're touching
`contracts/`, bump `API_VERSION` and note it in the PR body.