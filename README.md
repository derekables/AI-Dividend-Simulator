# AI Dividend Simulator

A minimal, opinionated simulator for exploring what a public claim on AI-generated surplus could look like in practice.

This project is not just a generic dividend calculator. It is a model for a broader idea: that AI-generated returns, built atop human contribution, social data, public infrastructure, and public labor, should not be treated as purely private rent. The simulator is designed to make that claim legible, testable, and discussable.

This repo sits at the intersection of:

- AI as infrastructure
- public ownership of AI-generated surplus
- universal or systemic payouts funded by AI rents
- policy design for shared prosperity and accountability
- personal and civic tools that help people understand and act in this new economy

## Mission

If AI is trained on all of us—our posts, our code, our culture, our labor, our social signals—then the surplus it generates should not be captured exclusively by those with capital and compute. This repo models the argument that some portion of AI-generated value can be treated as a public claim rooted in human contribution and civic legitimacy.

The simulator is not meant to be a final economic system. It is a research and advocacy tool: a place to test assumptions, compare scenarios, and build the logic for future policy and product work.

## Core idea

At its heart, the simulator models the simple relationship:

D = (τ × R) / N

Where:

- D = dividend or per-person public payout
- R = total AI-generated returns (profits, rents, surplus)
- N = eligible population or claimant base
- τ = share of AI-generated returns allocated to a public claim

This formula is the starting point, not the end of the model. From there, the project can layer in:

- compute as a public utility
- data and model contribution claims
- displacement and inequality adjustments
- regional and lifecycle differences
- public trust, governance, and access structures
- civic tools and personal agents that help people reason about the system

## Why this matters

The goal is to make a specific claim legible:

- AI-generated surplus is not neutral
- it is built on social and economic inputs far larger than capital alone
- and therefore the question is not only “how do we tax AI?”
- but also “what public claim should society have on the surplus that AI produces?”

The dividend calculator is the first visible expression of that idea. The broader project aims to make the underlying principle operational: public claims, policy design, and institutional structure around AI-generated value.

## One repo, staged architecture

This repo is intentionally designed as a single project home for both:

- the working simulator itself
- the broader policy and advocacy platform vision

That means the codebase should grow in layers, rather than pretending to be fully built before it is.

### Layer 1: simulator core (implemented now)

This is the working financial and conceptual core of the project. It models the basic dividend logic and scenario inputs.

### Layer 2: policy and scenario modeling (next)

This layer expands the model beyond a single formula into real scenario design, policy assumptions, and distribution logic.

### Layer 3: product interface (next)

A frontend, API, and scenario runner make the model usable by humans and by other tools.

### Layer 4: advocacy and civic platform (future)

This layer includes broader public-facing materials, policy framing, communication artifacts, and alignment with an NGO or civic operating system.

### Layer 5: personal agents and operational tools (future)

This could include agents, dashboards, recommendation systems, and tools that help individuals, communities, and institutions understand and act within the system.

## Repository structure

Current and planned project structure:

```text
ai-dividend-simulator/
├── README.md
├── Current-Status.md
├── LICENSE
├── docs/
│   ├── architecture.md
│   ├── economic-models.md
│   ├── policy-model.md
│   ├── roadmap.md
│   ├── conversation-history.md
│   └── manifesto.md        # planned public-facing narrative
├── simulator/
│   ├── core.py              # current economic core
│   ├── scenarios.py         # planned scenario models
│   ├── models.py            # planned structured model layer
│   ├── cli.py               # planned command-line interface
│   ├── ai_rent.py           # planned rent and surplus model
│   ├── compute_rent.py      # planned compute/public utility logic
│   ├── data_dividend.py     # planned data contribution model
│   └── __init__.py
├── frontend/
│   ├── index.html
│   ├── app.js
│   ├── style.css
│   └── assets/
├── api/
│   └── server.py            # planned API layer
├── tests/
│   └── # planned validation and regression coverage
├── platform/
│   └── # future civic/advocacy/product layer
├── docs/roadmap.md
└── docs/architecture.md
```

## Project posture

This repository should remain:

- intellectually ambitious
- technically modest at first
- honest about what is built versus what is planned
- designed for gradual expansion without losing coherence

The project is not yet a full public policy engine or NGO platform. It is a strong conceptual prototype and a foundation for building one.

## Recommended framing for contributors

When working in this repo, keep the following in mind:

- build the simulation engine
- document the policy logic
- separate implemented work from future work
- treat the dividend model as a public-claims engine, not a sterile spreadsheet formula
- keep the long-term mission visible without overclaiming current capability

## Summary

This repo exists to model a public claim on AI-generated surplus rooted in human and social contribution, rather than just a generic dividend calculator.

The calculator is where we started. The broader project is the idea that AI-generated value should be understood as a collective social product, and that a public share of that value may be justified through a structured system of claims, governance, and distribution.

This repo is the home for that work.

---

AI Dividend Simulator
A project for exploring public ownership, shared surplus, and policy design in the age of AI.
