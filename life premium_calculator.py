"""
Life Insurance Premium Calculator
----------------------------------

The Idea:
We don't know when someone will pass away. 
However, we know the probability of passing away each year (based on a mortality table).
Therefore, rather than making assumptions, we calculate the expected cost of insurance and base the rate on that estimate.

We also need to account for the time value of money: Money in the future is worth less than money today, 
so we shrink each year's expected cost based on how far away it is.
"""

import random
from openpyxl import Workbook

# ===================================================================
# Change these to get different outputs
# ===================================================================

AGE = 35                
TERM_YEARS = 5             # length of the policy, in years
COVERAGE_AMOUNT = 100_000  # payout if the person passes away during the term
INTEREST_RATE = 0.03       # annual interest rate (0.03 = 3%)

NUM_SIMULATED_PEOPLE = 10_000   # how many people to simulate for the example
NUM_SIMULATED_PEOPLE_TABLE = 2_000  # Reduced since the Excel table runs this many times per row

EXCEL_MIN_AGE = 18   # first age row in the Excel table
EXCEL_MAX_AGE = 76   # last age row in the Excel table
# 76 is not a random number. The mortality data used in the project goes up to age 80,
# many life insurance policies often do not cover individuals beyond this age. The oldest
# appropiate starting age for a 5 year term is 76.
# (76 + 5 - 1 = 80).

# Set this to a number to get the SAME random result every time you run the script.
# Set it to None to get a different result every run.
RANDOM_SEED = None

if RANDOM_SEED is not None:
    random.seed(RANDOM_SEED)
# ===================================================================


# -----------------------------------------------------------------
# The Mortality Table
# -----------------------------------------------------------------
# A mortality table is a table that shows the probability of death at each age.
# Real Data taken from the Social Security Administration's
# 2023 Period Life Table (Female column), published at:
# https://www.ssa.gov/oact/STATS/table4c6.html

mortality_table = {
    18: 0.000372,
    19: 0.000410,
    20: 0.000441,
    21: 0.000476,
    22: 0.000513,
    23: 0.000546,
    24: 0.000582,
    25: 0.000609,
    26: 0.000641,
    27: 0.000683,
    28: 0.000740,
    29: 0.000808,
    30: 0.000878,
    31: 0.000947,
    32: 0.001018,
    33: 0.001089,
    34: 0.001154,
    35: 0.001209,
    36: 0.001263,
    37: 0.001347,
    38: 0.001438,
    39: 0.001533,
    40: 0.001643,
    41: 0.001742,
    42: 0.001845,
    43: 0.001954,
    44: 0.002075,
    45: 0.002187,
    46: 0.002306,
    47: 0.002438,
    48: 0.002595,
    49: 0.002791,
    50: 0.003030,
    51: 0.003288,
    52: 0.003554,
    53: 0.003847,
    54: 0.004172,
    55: 0.004532,
    56: 0.004923,
    57: 0.005365,
    58: 0.005815,
    59: 0.006333,
    60: 0.006923,
    61: 0.007555,
    62: 0.008220,
    63: 0.008881,
    64: 0.009514,
    65: 0.010188,
    66: 0.010880,
    67: 0.011659,
    68: 0.012543,
    69: 0.013581,
    70: 0.014769,
    71: 0.016153,
    72: 0.017705,
    73: 0.019495,
    74: 0.021533,
    75: 0.023846,
    76: 0.026458,
    77: 0.029700,
    78: 0.033135,
    79: 0.036982,
    80: 0.041183,
}


# -----------------------------------------------------------------
# The Calculator
# -----------------------------------------------------------------
# The calculator assists the company in estimating the cost to charge an individual based
# on the age at which they begin the policy, which provides coverage if they pass away during
# the term.

def calculate_premium(start_age, term, coverage, interest_rate):
    """
    start_age:     age of the person today (e.g. 35)
    term:          length of policy in years (e.g. 5)
    coverage:      payout amount if they die (e.g. 100000)
    interest_rate: annual interest rate as a decimal (e.g. 0.03 for 3%)
    """

    total_premium = 0.0

    prob_still_alive = 1.0

    for year in range(term):
        current_age = start_age + year

        prob_die_this_year = mortality_table[current_age] * prob_still_alive

        expected_cost_this_year = prob_die_this_year * coverage
        discounted_cost = expected_cost_this_year / ((1 + interest_rate) ** (year + 1))

        total_premium += discounted_cost

        prob_still_alive = prob_still_alive * (1 - mortality_table[current_age])

    return total_premium


# -----------------------------------------------------------------
# The Simulation
# -----------------------------------------------------------------
# The system checks the calculations done by the calculator by simulating
# a large number of people and seeing what the average payout is.

import random  

def simulate_premium(start_age, term, coverage, interest_rate, num_people=10_000):
    """
    Same inputs as calculate_premium, plus:
    num_people: how many fake policyholders to simulate (bigger = more accurate)
    """

    total_payout = 0.0  

    for person in range(num_people):
        for year in range(term):
            current_age = start_age + year

            if random.random() < mortality_table[current_age]:
                discounted_payout = coverage / ((1 + interest_rate) ** (year + 1))
                total_payout += discounted_payout
                break  


    average_payout = total_payout / num_people
    return average_payout


if __name__ == "__main__":
    premium_math = calculate_premium(AGE, TERM_YEARS, COVERAGE_AMOUNT, INTEREST_RATE)

    premium_simulation = simulate_premium(
        AGE, TERM_YEARS, COVERAGE_AMOUNT, INTEREST_RATE, num_people=NUM_SIMULATED_PEOPLE
    )

    print(f"Individual's age: {AGE}")
    print(f"Policy term: {TERM_YEARS} years")
    print(f"Coverage if they pass away: ${COVERAGE_AMOUNT:,.2f}")
    print(f"Interest rate: {INTEREST_RATE*100}%")
    print()
    print(f"(The calculation) premium: ${premium_math:,.2f}")
    print(f"({NUM_SIMULATED_PEOPLE:,}-person simulation): ${premium_simulation:,.2f}")
    print()

    difference = abs(premium_math - premium_simulation)
    print(f"Difference between the two methods: ${difference:,.2f}")


# -----------------------------------------------------------------
# Export results to Excel
# -----------------------------------------------------------------
# The system calculates the premium for each age and exports it to Excel.
# It uses openpyxl
# (Please install it first if you don't have it, otherwise it will not work)

def export_premium_table_to_excel(filename, term, coverage, interest_rate):
    """
    Builds a table: for every age from EXCEL_MIN_AGE to EXCEL_MAX_AGE,
    what's the premium for this term/coverage/interest rate?
    Saves it as an Excel file.
    """

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Premium Table"

    sheet["A1"] = "Age"
    sheet["B1"] = "Math Premium ($)"
    sheet["C1"] = "Simulated Premium ($)"

    oldest_age_in_table = max(mortality_table.keys())
    last_valid_start_age = min(EXCEL_MAX_AGE, oldest_age_in_table - term + 1)

    row = 2
    for age in range(EXCEL_MIN_AGE, last_valid_start_age + 1):
        math_premium = calculate_premium(age, term, coverage, interest_rate)
        sim_premium = simulate_premium(
            age, term, coverage, interest_rate, num_people=NUM_SIMULATED_PEOPLE_TABLE
        )

        sheet[f"A{row}"] = age
        sheet[f"B{row}"] = round(math_premium, 2)
        sheet[f"C{row}"] = round(sim_premium, 2)

        row += 1  

    workbook.save(filename)
    print(f"Saved Excel file: {filename}")

if __name__ == "__main__":
    export_premium_table_to_excel(
        filename="premium_table.xlsx",
        term=5,
        coverage=100_000,
        interest_rate=0.03,
    )

