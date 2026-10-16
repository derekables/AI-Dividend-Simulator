# Architecture Overview

## 1. High-Level Components

The AI Dividend Simulator is composed of:

1. **Economic Engine (`/simulator`)**
   - Models AI-generated returns.
   - Applies public share parameters.
   - Computes per-person dividends.
   - Supports scenario analysis.

2. **Policy Layer (`/docs/policy-model.md`)**
   - Describes institutional mechanisms.
   - Defines collection, governance, and distribution structures.
   - Connects simulator outputs to real-world policy levers.

3. **Frontend (`/frontend`)**
   - Simple UI for:
     - entering parameters,
     - visualizing outcomes,
     - comparing scenarios.

4. **API (`/api`)**
   - Optional layer for:
     - programmatic access,
     - integration with personal OS tools (e.g., AblesLab),
     - agentic simulations.

5. **Narrative Layer (`/docs/manifesto.md`, `/docs/roadmap.md`)**
   - Frames the project in human, political, and ethical terms.
   - Serves as a bridge between code and policy.

## 2. Economic Engine Design

Core modules:

- `core.py`
  - Main entry point.
  - Orchestrates calculations.
- `models.py`
  - Data structures:
    - `EconomyState`
    - `DividendScenario`
    - `AIRevenueStreams`
- `ai_rent.py`
  - Models AI corporate profits and rents.
- `compute_rent.py`
  - Models compute as a public utility:
    - infrastructure costs,
    - pricing above marginal cost,
    - surplus available for dividends.
- `data_dividend.py`
  - Models payments for access to public data pools.
- `scenarios.py`
  - Predefined scenario sets:
    - low τ vs high τ,
    - high concentration vs broad distribution,
    - different AI adoption curves.

## 3. Core Flow

1. **Input**
   - AI corporate profits.
   - compute rents.
   - data licensing fees.
   - population.
   - τ (public share of AI rents).
   - optional:
     - displacement index,
     - inequality index.

2. **Processing**
   - Aggregate total AI-generated returns \(R\).
   - Apply τ to determine public share.
   - Divide by population \(N\) to compute base dividend.
   - Adjust for:
     - displacement,
     - inequality,
     - policy choices.

3. **Output**
   - monthly dividend per person.
   - annual dividend per person.
   - total fund size.
   - scenario comparisons.
   - optional:
     - agent-access credits,
     - infrastructure access metrics.

## 4. Integration with Personal OS (AblesLab)

The simulator can be:

- embedded as a module in a personal OS,
- exposed via API,
- or wrapped in an agent that:

  - explains scenarios,
  - helps users plan around different futures,
  - allocates dividends into autonomous projects.

Example flows:

- “Given these AI profit projections, what does my monthly dividend look like under τ = 0.2 vs 0.4?”
- “If I allocate 20% of my dividend to compute and tools, what can my agent build or run?”

## 5. Design Principles

- **Minimal first, extensible later.**
- **Transparent math.**
- **Human-readable outputs.**
- **Policy-aware, not policy-dictating.**
- **Agent-friendly.**
