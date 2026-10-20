# Roadmap

This roadmap reflects the repo’s actual direction: a single project home for a public-interest AI dividend simulator, a policy model, and the broader civic/product vision that grows out of it.

## Phase 0 — Clarify the mission and repo boundaries

- [x] Define the project as a public-claims model on AI-generated surplus
- [x] Frame the dividend calculator as a first step, not the end state
- [x] Keep a single repository for simulator, policy logic, and public-facing vision
- [ ] Document the distinction between:
  - implemented work
  - planned work
  - aspirational future work

## Phase 1 — Stabilize the simulator core

- [ ] Improve the basic economic engine in `simulator/core.py`
- [ ] Add structured data models for inputs, outputs, and scenarios
- [ ] Document assumptions clearly
- [ ] Constrain the model so it stays understandable and transparent
- [ ] Validate the formula and edge cases against realistic scenarios

## Phase 2 — Build scenario and policy modeling

- [ ] Add scenario definitions for: low vs high public share, inequality, displacement, adoption speed, etc.
- [ ] Expand the model from a single dividend formula into richer policy logic
- [ ] Define public claim, claimant base, and eligibility assumptions explicitly
- [ ] Add documentation for tradeoffs and limits of the model
- [ ] Develop economic-model and policy-model docs as primary references

## Phase 3 — Make the simulator usable

- [ ] Add a command-line interface or runner
- [ ] Improve the frontend for scenario comparison and explanation
- [ ] Create a simple API layer for agent and tooling integration
- [ ] Separate prototype UI from final product UI language
- [ ] Ensure the tool remains accessible to non-experts

## Phase 4 — Build the platform layer

- [ ] Add a more deliberate civic/product layer around the simulator
- [ ] Develop materials for policy education and public communication
- [ ] Create tools and narratives that explain why a public claim on AI surplus is legitimate
- [ ] Design for use by researchers, activists, civic technologists, and policy operators

## Phase 5 — Personal agent and institutional integration

- [ ] Explore integration with personal assistants and autonomous tools
- [ ] Allow agents to explain scenarios and support user decision-making
- [ ] Build dashboards or assistive tools around the model
- [ ] Consider how this can connect to broader governance, mutual aid, or public-interest infrastructure work

## Phase 6 — Expand toward the broader mission

- [ ] Model more complex economic and social dynamics
- [ ] Add regional, lifecycle, and labor-distribution variants
- [ ] Test design choices around eligibility, governance, and social legitimacy
- [ ] Consider how the simulator can support an NGO or civic platform built around shared AI surplus

## Core rule for this roadmap

The project should grow in a way that keeps the mission coherent:

- the simulator is the technical foundation
- the policy model explains the normative claim
- the product layer makes it useful
- the civic vision gives it purpose

This repo is not only a calculator. It is a public-interest research and design project around the question:

What would it mean to treat AI-generated surplus as a social product with a public claim behind it?

That is the long-term arc of the roadmap.
