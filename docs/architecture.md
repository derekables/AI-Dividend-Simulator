# Architecture Overview

## Purpose

This repository is designed as a single unified project for understanding and operationalizing a public claim on AI-generated surplus.

The core objective is not simply to compute dividends. It is to model the social, economic, and political logic behind a claim that some share of AI-generated value belongs to the public because that value is built on human contribution, social data, public infrastructure, and collective labor.

The project is intentionally staged:

- the simulator is the working proof-of-concept
- the policy model gives it legitimacy and structure
- the product layer makes it usable
- the civic/advocacy layer gives it social purpose

## Architecture principles

1. One repo, layered scope
   - The simulator, policy documents, and broader platform vision live together in one project.
   - The architecture should reflect that progression without pretending the later layers are already built.

2. Honest maturity boundaries
   - Some components are implemented.
   - Some are planned and intentionally scoped.
   - Some are aspirational but part of the long-term vision.

3. Public-claims framing
   - The system should model claims on AI surplus, not just a generic distribution formula.
   - The public claim should be rooted in human and social contribution.

4. Extensible by default
   - The foundational engine should stay readable and minimally complex.
   - Additional policy, scenario, and civic layers can be added over time.

## High-level architecture

### 1. Simulation layer

This layer contains the economic engine and scenario logic.

Responsibilities:

- model AI-generated returns
- calculate the public share of surplus
- apply population and claimant assumptions
- compare scenarios and policy assumptions
- produce dividend outputs and system metrics

Current implementation status:

- the simulator core exists in `simulator/core.py`
- the repository is intentionally minimal and conceptual at this stage

Planned modules:

- `simulator/core.py` — core calculations and orchestration
- `simulator/models.py` — structured data models and scenario definitions
- `simulator/scenarios.py` — prebuilt scenario comparisons
- `simulator/ai_rent.py` — AI profit and rent analysis
- `simulator/compute_rent.py` — public utility and compute assumptions
- `simulator/data_dividend.py` — data and contribution-based allocation logic
- `simulator/cli.py` — command-line usage

### 2. Policy and governance layer

This layer explains how the numerical outputs connect to actual institutions and social legitimacy.

Responsibilities:

- frame the model as a public claim, not just a private payout
- connect economic outputs to policy design
- specify what share of AI surplus may be publicly claimed and why
- assess governance, eligibility, and distribution design

Relevant docs:

- `docs/policy-model.md`
- `docs/economic-models.md`
- `docs/manifesto.md` (planned)

### 3. Frontend and interaction layer

This layer makes the model understandable to users.

Responsibilities:

- user input for economic assumptions
- display of annual and monthly payouts
- comparison of policy scenarios
- explanation of outputs in accessible terms

Current implementation status:

- basic HTML/JS frontend exists under `frontend/`
- this is a prototype and not yet a fully integrated application

### 4. API and integration layer

This layer makes the simulator usable by other tools and agents.

Responsibilities:

- expose model outputs programmatically
- enable agent-based scenario analysis
- support integration with personal operating systems and civic tools

Planned implementation:

- `api/server.py`
- structured API schema for scenario execution and reporting

### 5. Civic and advocacy layer

This layer is the social purpose of the repo.

Responsibilities:

- explain public ownership in plain language
- turn economic logic into a policy argument
- support narratives about shared AI surplus and democratic governance
- connect the simulator to real advocacy and institutional work

This is not a first-layer software requirement; it is the long-term framing that gives the technical work meaning.

## Current implementation snapshot

As of the current repo state, the project is best described as:

- a minimal but meaningful simulator prototype
- a policy and concept engine in progress
- a communication artifact for public-interest AI design
- a foundation for more elaborate scenario modeling

It is not yet a complete policy platform or a final civic app. That is acceptable. The important thing is that the architecture keeps pace with the project’s actual maturity.

## Conceptual data model

The simulator should eventually distinguish between:

- economic inputs
  - AI profits
  - compute rents
  - data licensing revenue
  - labor and social contribution
  - eligible population
- policy parameters
  - public share τ
  - claimant rules
  - distribution logic
  - governance model
- outputs
  - annual dividend
  - monthly dividend
  - fund size
  - scenario comparison
  - inequality/displacement adjustments

## Design boundaries

The key design boundary is this:

- the simulator may be used as a neutral research tool
- the policy model gives the system normative content
- the broader platform vision sets the social and governance ambition

The project should not collapse these layers into one vague “everything” bucket. They should remain distinct even within a single repo.

## Intended evolution

The repo should evolve in phases:

1. stabilize the core simulator
2. add richer scenario and policy layers
3. connect the simulator to a usable web interface/API
4. develop the civic and advocacy layer around it
5. support agent and personal OS integrations as the project matures

## Summary

This repository is a single-project architecture for a public-interest AI dividend concept: a simulator first, a policy engine next, and a broader civic platform later.

The architecture should remain honest, extendable, and clear about the difference between:

- what exists now,
- what is being built next,
- and what the long-term mission ultimately aims to become.
