#!/usr/bin/env python3

from simulator.core import compare_scenarios
from simulator.scenarios import default_scenario_bundle


if __name__ == "__main__":
    bundle = default_scenario_bundle()
    results = compare_scenarios(bundle.scenarios)

    print(f"Scenario comparison: {bundle.name}")
    print("-" * 60)
    for result in results:
        print(f"Scenario: {result.name}")
        print(f"  Description: {result.description}")
        print(f"  Annual dividend per person: ${result.annual_dividend_per_person:,.2f}")
        print(f"  Monthly dividend per person: ${result.monthly_dividend_per_person:,.2f}")
        print(f"  Public fund: ${result.public_fund:,.2f}")
        print()
