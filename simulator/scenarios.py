# simulator/scenarios.py

from dataclasses import dataclass
from typing import List

from simulator.core import DividendScenario, build_scenario


@dataclass
class ScenarioBundle:
    name: str
    description: str
    scenarios: List[DividendScenario]


def baseline_scenario() -> DividendScenario:
    return build_scenario(
        name="baseline",
        description="A moderate public claim on AI-generated surplus.",
        profit=1_000_000_000.0,
        compute_surplus=500_000_000.0,
        data_licensing=250_000_000.0,
        population=10_000_000,
        tau=0.30,
    )


def high_public_claim_scenario() -> DividendScenario:
    return build_scenario(
        name="high_public_claim",
        description="A more ambitious public share of AI surplus.",
        profit=1_000_000_000.0,
        compute_surplus=500_000_000.0,
        data_licensing=250_000_000.0,
        population=10_000_000,
        tau=0.60,
    )


def low_public_claim_scenario() -> DividendScenario:
    return build_scenario(
        name="low_public_claim",
        description="A conservative public share with a smaller public claim on returns.",
        profit=1_000_000_000.0,
        compute_surplus=500_000_000.0,
        data_licensing=250_000_000.0,
        population=10_000_000,
        tau=0.15,
    )


def default_scenario_bundle() -> ScenarioBundle:
    return ScenarioBundle(
        name="default_comparison",
        description="Three scenario presets to compare different public share assumptions.",
        scenarios=[
            low_public_claim_scenario(),
            baseline_scenario(),
            high_public_claim_scenario(),
        ],
    )


if __name__ == "__main__":
    bundle = default_scenario_bundle()
    for scenario in bundle.scenarios:
        print(f"{scenario.name}: ${scenario.annual_dividend_per_person():,.2f}/year per person")
