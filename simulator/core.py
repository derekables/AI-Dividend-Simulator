# simulator/core.py

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional


@dataclass
class AIRevenueStreams:
    """Annual revenue streams feeding the AI surplus pool."""

    profit: float = 0.0
    compute_surplus: float = 0.0
    data_licensing: float = 0.0

    @property
    def total(self) -> float:
        return self.profit + self.compute_surplus + self.data_licensing


@dataclass
class DividendScenario:
    """A single public-claims dividend scenario.

    This is the minimal domain model for the simulator. It captures the core
    economic structure needed to model a public claim on AI-generated surplus.
    """

    population: int = 0
    tau: float = 0.0
    revenue_streams: AIRevenueStreams = field(default_factory=AIRevenueStreams)
    name: str = "scenario"
    description: str = ""
    inequality_adjustment: float = 1.0
    displacement_adjustment: float = 1.0

    @property
    def total_revenue(self) -> float:
        return self.revenue_streams.total

    @property
    def public_fund(self) -> float:
        return self.tau * self.total_revenue

    def annual_dividend_per_person(self) -> float:
        """Base annual dividend per individual: D = (tau * R) / N."""
        if self.population <= 0:
            return 0.0
        return (self.tau * self.total_revenue) / self.population

    def monthly_dividend_per_person(self) -> float:
        return self.annual_dividend_per_person() / 12.0

    def adjusted_annual_dividend_per_person(self) -> float:
        """A simple scenario adjustment layer that can capture drag from inequality
        or social displacement without changing the formula itself.
        """
        base = self.annual_dividend_per_person()
        adjusted = base * self.inequality_adjustment * self.displacement_adjustment
        return adjusted

    def adjusted_monthly_dividend_per_person(self) -> float:
        return self.adjusted_annual_dividend_per_person() / 12.0


@dataclass
class ScenarioComparison:
    name: str
    description: str
    annual_dividend_per_person: float
    monthly_dividend_per_person: float
    public_fund: float
    total_revenue: float


def build_scenario(
    *,
    name: str = "scenario",
    description: str = "",
    profit: float = 0.0,
    compute_surplus: float = 0.0,
    data_licensing: float = 0.0,
    population: int = 0,
    tau: float = 0.0,
    inequality_adjustment: float = 1.0,
    displacement_adjustment: float = 1.0,
) -> DividendScenario:
    return DividendScenario(
        name=name,
        description=description,
        population=population,
        tau=tau,
        revenue_streams=AIRevenueStreams(
            profit=profit,
            compute_surplus=compute_surplus,
            data_licensing=data_licensing,
        ),
        inequality_adjustment=inequality_adjustment,
        displacement_adjustment=displacement_adjustment,
    )


def example_scenario() -> DividendScenario:
    return build_scenario(
        name="baseline",
        description="A balanced scenario with a moderate public claim on AI surplus.",
        profit=1_000_000_000.0,
        compute_surplus=500_000_000.0,
        data_licensing=250_000_000.0,
        population=10_000_000,
        tau=0.30,
    )


def compare_scenarios(scenarios: Iterable[DividendScenario]) -> List[ScenarioComparison]:
    comparisons: List[ScenarioComparison] = []
    for scenario in scenarios:
        comparisons.append(
            ScenarioComparison(
                name=scenario.name,
                description=scenario.description,
                annual_dividend_per_person=scenario.adjusted_annual_dividend_per_person(),
                monthly_dividend_per_person=scenario.adjusted_monthly_dividend_per_person(),
                public_fund=scenario.public_fund,
                total_revenue=scenario.total_revenue,
            )
        )
    return comparisons


if __name__ == "__main__":
    scenario = example_scenario()
    annual = scenario.annual_dividend_per_person()
    monthly = scenario.monthly_dividend_per_person()
    adjusted_annual = scenario.adjusted_annual_dividend_per_person()

    print(f"Scenario: {scenario.name}")
    print(f"Annual dividend per person: ${annual:,.2f}")
    print(f"Monthly dividend per person: ${monthly:,.2f}")
    print(f"Adjusted annual dividend per person: ${adjusted_annual:,.2f}")
    print(f"Public fund size: ${scenario.public_fund:,.2f}")
