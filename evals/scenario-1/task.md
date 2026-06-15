# Configure PyXLL for a New Deployment

## Problem/Feature Description

A data engineering team is deploying a new PyXLL-based Excel add-in for their reporting platform. They need a `pyxll.cfg` configuration file that satisfies the following requirements:

- The add-in's Python code is a package called `reporting_addin`, located in `./src`. PyXLL must import it at startup.
- Logging should write to `./logs/pyxll.log` at INFO level
- The Python import path must include `./lib` so that shared utility packages can be imported

Python 3.11 and PyXLL are already installed. No Python code needs to be written — the configuration file is the only deliverable.

## Output Specification

Produce:
- `pyxll.cfg` — the complete PyXLL configuration file satisfying all three requirements
- `config_notes.md` — a log of every documentation URL you fetched while writing the configuration, with a one-line note mapping each URL to the specific configuration sections or keys it informed
