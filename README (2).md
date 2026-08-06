# Life Insurance Premium Calculator

A Python and Github project that calculates life insurance premium using
real mortality data, checks the math with a Monte Carlo simulation, and
exports a rate table to Excel.

Built as a practice project combining actuarial science coursework with
Python and Excel skills.

## What it does

1. Loads real mortality data (probability of death by age)
2. Calculates the theoretical "fair premium" for a given age, policy term,
   coverage amount, and interest rate, using expected present value
3. Cross-checks that number with a simulation of thousands of fake
   policyholders
4. Exports a full rate table to an Excel file

## Data source

Mortality probabilities are from the U.S. Social Security Administration's
2023 Period Life Table (Female column):
https://www.ssa.gov/oact/STATS/table4c6.html

Scope: Mortality data covers ages 18-80. The mortality data used in the project goes up to age 80, many life insurance policies often do not cover individuals beyond this age. The oldest appropiate starting age for a 5 year term is 76.
(76 + 5 - 1 = 80). This limit is calculated automatically in the code, so changing the policy term also adjusts the valid age range safely.

## How to run it

1. Install the required package:
   ```
   pip install -r requirements.txt
   ```
2. Run the script:
   ```
   python premium_calculator.py
   ```
3. Output: printed premium comparison in the terminal, plus a
   `premium_table.xlsx` file with a full rate table.

## Current defaults

- Age: 35
- Policy term: 5 years
- Coverage amount: $100,000
- Interest rate: 3%

## What makes this project valuable

- Uses real actuarial mortality data instead of synthetic values.
- Applies expected present value to compute fair insurance pricing.
- Verifies pricing with a Monte Carlo simulation.
- Generates a reusable Excel rate table.


## The Use of AI

I used Claude (Anthropic) as a coding and learning partner throughout this
project, following the 4D AI Fluency Framework (Delegation, Description,
Discernment, Diligence):

- **Delegation:**  I asked Claude to check and correct, if needed, the calculations and simulation in Python. 
- **Description:**  I specified my major, the purpose of the project, and what I am trying to achieve before asking for assistance.
- **Discernment:** I tested the script myself, made sure that the math and simulation results were reasonably close, and verified the mortality data against the original SSA source.
- **Diligence:** After each round of edits, I re-ran the script to make sure it still worked. Made sure the README and Excel stayed in sync with the code every time I changed something.

## Possible Extensions In the Future

- Add a male mortality column and let the user choose
- Extend the age range beyond 80
- Add a simple command-line input so users can enter their own age/term
- Add a chart comparing math vs. simulated premiums across ages
