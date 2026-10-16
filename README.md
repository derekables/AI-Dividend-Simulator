# AI Dividend Simulator

A minimal, opinionated simulator for exploring what an **AI-funded dividend** could look like in practice.

This project exists at the intersection of:

- AI as infrastructure
- public ownership of AI-generated surplus
- universal, systemic payouts (dividends) funded by AI rents
- personal autonomous operating systems that help individuals navigate and benefit from this new economy

## Vision

If AI is trained on all of us—our posts, our lyrics, our teenage MySpace pages, our code, our culture—then the surplus it generates should not be owned exclusively by those who had capital at the right time.

This repo is a first step toward:

- making the **economic logic** of an AI dividend legible,
- giving people tools to **simulate scenarios**, and
- building foundations for **policy, products, and personal agents** that assume shared ownership of AI’s upside.

## Core Idea

At its heart, the simulator models a simple relationship:



\[
D = \frac{\tau R}{N}
\]



Where:

- \(R\): total AI-generated returns (profits, rents, surplus)
- \(N\): number of eligible people
- \(\tau\): share of AI rents allocated to a public dividend

From there, we can layer:

- compute as a public utility,
- data dividends,
- displacement and inequality metrics,
- and agent-access credits.

## Repo Structure

Planned structure:

```text
ai-dividend-simulator/
│
├── README.md
├── /docs
│   ├── manifesto.md
│   ├── architecture.md
│   ├── policy-model.md
│   ├── economic-models.md
│   └── roadmap.md
│
├── /simulator
│   ├── core.py
│   ├── models.py
│   ├── scenarios.py
│   ├── compute_rent.py
│   ├── data_dividend.py
│   └── ai_rent.py
│
├── /frontend
│   ├── index.html
│   ├── app.js
│   └── styles.css
│
├── /api
│   └── server.py
│
└── LICENSE
