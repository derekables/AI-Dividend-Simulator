# Current Status

Date: 2026-10-19

## Repository purpose

This repository is a minimal exploratory simulator for an AI-funded dividend concept. The core idea is that if AI-generated surplus is built on public data, public infrastructure, and public labor, some share of that surplus should flow back to people as a universal dividend.

The essential formula in the project is:

D = (τ × R) / N

Where:
- D = dividend per person
- τ = public share of AI-generated rents
- R = total AI-generated returns
- N = eligible population

The project is intentionally opinionated and conceptual rather than a production economic system. It aims to make the policy logic legible, testable, and discussable.

## Current implementation status

### What exists

The repo currently contains:
- a small Python economic core in `simulator/core.py`
- a simple static web UI in `frontend/index.html` and `frontend/app.js`
- a set of conceptual docs under `docs/`
- a license and a basic README

The Python engine currently models:
- AI revenue streams as `AIRevenueStreams`
- a dividend scenario as `DividendScenario`
- annual and monthly dividends per person

The frontend allows users to enter:
- AI profit
- compute surplus
- data licensing revenue
- population
- public share τ

...and then shows annual and monthly dividend figures.

### What does not exist yet

The repo is still early-stage and has several gaps:
- no Python package metadata (`pyproject.toml`, `requirements.txt`, etc.)
- no tests
- no CLI wrapper or scenario runner beyond the simple script in `simulator/core.py`
- no API server under `/api`
- no scenario module (`scenarios.py`)
- no `models.py` or other detailed economic components described in docs
- no `/docs/manifesto.md` even though the docs and README reference it

## Architecture reality vs. documented plan

The current repository is a proof-of-concept, but some documentation still reads like a planned future architecture rather than the repo's actual state.

Examples of mismatch:
- `docs/architecture.md` describes modules such as `models.py`, `ai_rent.py`, `compute_rent.py`, `data_dividend.py`, and `scenarios.py`, but these files do not currently exist.
- `README.md` describes a planned directory structure including `api/`, `manifesto`, and additional simulator modules that are not yet implemented.
- `frontend/index.html` references `styles.css`, while the actual file is named `style.css`.

This is not a failure; it is a normal early-stage state. But it does mean the architecture should be cleaned up so the docs match the actual project reality.

## Current project posture

At present, this project is best understood as:
- a conceptual prototype,
- a thought experiment with a working calculation,
- a small, modular base for future scenario modeling,
- and a communication artifact for policy and product discussions.

It is not yet a full economic engine or a polished product. That is fine, but it should be made explicit in the docs so expectations are aligned.

## Where we should go next

### Priority 1: clarify the architecture

Create a single source of truth for the architecture that reflects what exists now and what is intentionally planned next.

Recommended approach:
- keep a minimal core engine in `simulator/`
- clearly distinguish between:
  - implemented now,
  - planned next,
  - aspirational later
- remove references to nonexistent files unless we are actually building them

### Priority 2: build the real core model

The next meaningful step is to expand the simulator from a simple formula to a more structured model. Proposed additions:
- explicit `Scenario` definitions
- revenue stream breakdowns with better naming and semantics
- optional adjustments for inequality and displacement
- multi-year projections
- per-country or per-region variants

### Priority 3: add a proper Python project structure

This will make the project easier to run and maintain.

Suggested shape:
- `simulator/core.py` for core logic
- `simulator/scenarios.py` for scenario definitions
- `simulator/models.py` for data structures
- optional `simulator/cli.py` for command-line usage
- `tests/` for validation
- `pyproject.toml` or `requirements.txt` for reproducibility

### Priority 4: connect the frontend to the actual model

The static HTML/JS frontend should either:
- call a Python backend,
- or use a structured JS model that mirrors the Python logic,
- or be clearly marked as a demo UI, not a final product

Right now the frontend is a good demo, but it is not yet tied to a broader system architecture.

### Priority 5: sharpen the documentation

The repository needs more explicit documentation around:
- what is implemented vs. planned
- the economic assumptions behind the formula
- known limits of the model
- how future modules fit together
- what success looks like for the project at each phase

## Recommended next documentation updates

These should be treated as part of regular project hygiene:
1. Keep this `Current-Status.md` file updated after any major change.
2. Make `README.md` match the actual repo structure.
3. Update `docs/architecture.md` to reflect reality.
4. Add a short `docs/assumptions.md` or equivalent if the economic model becomes more complex.
5. Add a `docs/roadmap.md` phase status section for completed vs. pending work.

## Working principle for this repo

This repo should remain intentionally minimal but honest.

That means:
- small wins are valuable,
- architecture should remain readable,
- and documentation should be updated when the model changes.

The goal is not to build a giant system immediately. The goal is to create a clear foundation for serious thinking and future expansion.

## Summary

Current state: promising concept, minimal working simulator, clear theoretical framing, but still early and somewhat aspirational in its documentation.

Likely next move: convert the repo from a conceptual prototype into a better-defined, well-documented model with explicit phases, clearer architecture, and stronger maintainability practices.

This file should be reviewed and updated after major changes so the project status stays accurate over time.

## Update practice

After any major change, update this file with:
- what changed,
- what remains incomplete,
- what architecture assumptions were affected,
- and what next milestone is being targeted.

This should be a lightweight but regular habit in the repository.

---

Status file created for repo maintenance and future planning.
