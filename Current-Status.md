# Current Status

Date: 2026-10-20

## Repository purpose

This repository is a public-interest research project for understanding and modeling a public claim on AI-generated surplus.

The core idea is not simply to compute a dividend. It is to model a broader claim: that a significant portion of AI-generated value is socially produced, built on human contribution, public infrastructure, and collective data and labor, and therefore should not be treated as purely private rent.

The project begins with a minimal formula:

D = (τ × R) / N

Where:
- D = dividend or per-person public payout
- τ = share of AI-generated returns allocated to a public claim
- R = total AI-generated returns
- N = eligible population or claimant base

This formula is the first implementation layer. It is the minimum viable expression of a broader idea: public claims on AI surplus, informed by human contribution, social legitimacy, and governance design.

## Current implementation status

### What exists

The repo currently contains:
- a small Python economic core in `simulator/core.py`
- a simple static web UI in `frontend/index.html` and `frontend/app.js`
- conceptual docs under `docs/`
- a license and a basic README

The current implementation is best understood as:
- a working prototype for dividend calculation
- a conceptual engine for exploring AI surplus claims
- a foundation for future policy and civic modeling

### What is planned next

The project is intentionally staged and should continue to grow in layers:
- simulator core refinement
- richer scenario and policy modeling
- CLI/API/frontend integration
- public-facing documentation and policy framing
- broader civic and personal-agent layers

### What does not yet exist

The repo is still early-stage and does not yet fully embody the broader vision. Important gaps include:
- no fully structured Python package layout
- no tests
- no robust CLI or scenario runner
- no production API server
- no complete scenario library
- no full policy-governance implementation
- no complete civic platform layer

## Architecture reality

This repository is intentionally a single-project home for multiple layers of work:

1. The simulator layer
   - the working formula and basic input/output model
2. The policy layer
   - the claim that AI surplus is socially produced and therefore subject to public governance
3. The interface layer
   - frontend and API for usability and integration
4. The civic/advocacy layer
   - narratives, communication, and institutional framing

That structure is deliberate. The repo should not pretend to be a full public policy platform before it has built the underlying simulator and policy logic.

## Current project posture

At present, this project is best understood as:
- a conceptual prototype
- a public-claims model in early development
- a small but meaningful foundation for a larger civic and policy project
- a tool for exploring what a legitimate public claim on AI surplus might look like

It is not yet a final economic engine or a complete NGO platform. That is fine. The repo should remain explicit about this boundary.

## Where we should go next

### Priority 1: clarify the public-claims model

The project should keep making the core claim explicit:
- AI-generated surplus is not purely private
- it is built on social and economic inputs beyond capital alone
- a public share may be justified on grounds of contribution, infrastructure, and collective legitimacy

### Priority 2: strengthen the simulator core

The next meaningful step is to expand the simulator from a simple formula into a structured model with:
- explicit scenario definitions
- revenue stream breakdowns
- inequality and displacement adjustments
- multi-year projections
- region- or claimant-base variants

### Priority 3: build the product layer

The next implementation steps should include:
- CLI or runner
- more usable frontend
- structured API
- scenario comparison tools
- clearer user-facing explanations

### Priority 4: connect policy to implementation

The docs and code should remain closely aligned so that the economic model and policy argument reinforce one another.

### Priority 5: keep documentation honest

Documentation should clearly differentiate between:
- implemented now
- planned next
- aspirational future

## Recommended update practice

After any major change, update this file with:
- what changed,
- what remains incomplete,
- what assumptions were affected,
- and which milestone is next.

This should remain a lightweight but regular habit in the repo.

## Summary

The repo’s purpose is broader than a generic dividend calculator. It is the foundation for exploring a public claim on AI-generated surplus rooted in human contribution, social data, public infrastructure, and collective labor.

The dividend model is how we start. The larger project is to understand and make operational the political, economic, and civic logic behind that claim.

This file should be treated as a working reference for the project’s actual current posture and future direction.
