# Economic Models

## 1. Base Dividend Model

### Formula



\[
D = \frac{\tau R}{N}
\]



Where:

- \(R\): total AI-generated returns (profits, rents, surplus),
- \(N\): population,
- \(\tau\): public share of AI rents.

### Interpretation

- Linear, transparent, and easy to explain.
- Serves as the baseline for more complex models.

## 2. AI Revenue Streams

\(R\) can be decomposed into:



\[
R = R_{\text{profit}} + R_{\text{compute}} + R_{\text{data}}
\]



- \(R_{\text{profit}}\): AI corporate profits and rents.
- \(R_{\text{compute}}\): surplus from compute as a public utility.
- \(R_{\text{data}}\): licensing fees for access to public data pools.

Each component can be modeled separately and then aggregated.

## 3. Displacement and Inequality Adjustments

Optional adjustments:

- **Displacement index** \( \delta \)
  - Measures the degree of labor displacement by AI.
  - Can be used to:
    - increase τ,
    - or add targeted supplements.

- **Inequality index** \( \iota \)
  - Measures income or wealth inequality.
  - Can inform:
    - progressive weighting,
    - or additional infrastructure credits.

Example extended formula:



\[
D' = \frac{\tau (1 + \alpha \delta + \beta \iota) R}{N}
\]



Where:

- \(\alpha, \beta\): policy parameters controlling sensitivity to displacement and inequality.

## 4. Growth and Sustainability

We can model:

- AI adoption curves,
- profit growth rates,
- compute cost trends,
- and data licensing dynamics.

This allows:

- projections over time,
- stress tests,
- and scenario comparisons.

## 5. Scenario Types

Examples:

- **Low τ, high concentration**
  - Small public share.
  - Large private capture.
  - Modest dividends.

- **High τ, broad distribution**
  - Large public share.
  - Strong dividends.
  - Potential impact on private investment.

- **Compute-heavy models**
  - Emphasis on compute utility surplus.
  - Strong link to infrastructure access.

- **Data-heavy models**
  - Emphasis on data licensing.
  - Strong link to public data governance.

The simulator’s job is to make these scenarios **visible and explorable**.
