# simulator/core.py

from dataclasses import dataclass

@dataclass
class AIRevenueStreams:
    profit: float          # AI corporate profits (per year)
    compute_surplus: float # surplus from compute as a public utility (per year)
    data_licensing: float  # revenue from data licensing (per year)

    @property
    def total(self) -> float:
        return self.profit + self.compute_surplus + self.data_licensing


@dataclass
class DividendScenario:
    population: int        # number of eligible people
    tau: float             # public share of AI rents (0.0 - 1.0)
    revenue_streams: AIRevenueStreams

    def annual_dividend_per_person(self) -> float:
        """
        Base formula:
        D = (tau * R) / N
        """
        R = self.revenue_streams.total
        N = self.population
        return (self.tau * R) / N if N > 0 else 0.0

    def monthly_dividend_per_person(self) -> float:
        return self.annual_dividend_per_person() / 12.0


def example_scenario() -> DividendScenario:
    streams = AIRevenueStreams(
        profit=1_000_000_000.0,        # 1B in AI profits
        compute_surplus=500_000_000.0, # 500M in compute surplus
        data_licensing=250_000_000.0   # 250M in data licensing
    )

    scenario = DividendScenario(
        population=10_000_000, # 10M people
        tau=0.3,               # 30% public share
        revenue_streams=streams
    )

    return scenario


if __name__ == "__main__":
    scenario = example_scenario()
    annual = scenario.annual_dividend_per_person()
    monthly = scenario.monthly_dividend_per_person()

    print(f"Annual dividend per person: ${annual:,.2f}")
    print(f"Monthly dividend per person: ${monthly:,.2f}")
