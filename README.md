# Life-Insurance-Premium-Calculator
A project combining actuarial math and Python that calculates fair life insurance premiums, checks the math with a simulation, and exports a rate table to Excel.
# What It Does
1. Loads real mortality data
2. Calculates the theoretical "fair premium" for a given age, policy term, coverage amount, and interest rate, using expected present value
3. Cross checks the result with a simulation of 10.000 fake policyholders and calculates what the average payout is
4. Prints both results so the user can compare them
5. Exports a full rate table to an Excel file
# Data Source
The mortality probabilities come from the U.S. Social Security Administration's 2023 Period Life Table, Female column: https://www.ssa.gov/oact/STATS/table4c6.html
Scope: The mortality data used in the project cover females between the ages of 18 and 80. Many life insurance policies do not cover individuals beyond the age of 80; the oldest appropriate age for a 5 year term is 76 for this project. (76 + 5 - 1 = 80)
This limit is calculated automatically in the code, so changing the policy term also adjusts the valid age range safely
# Why Two Methods?
I developed a second method to verify the formula since I didn't want to rely solely on it. In summary, the simulation fakes thousands of random people and tests what actually happens to them.  It's a good confirmation that the math is correct if that average is close to what the formula predicts.
# How To Run It
1. Install the required package:
   ```
   pip install openpyxl
   ```
2. Run the file:
   ```
   python life_premium_calculator.py
   ```
3. To try different numbers, open the file and change the settings
   near the top (`AGE`, `TERM_YEARS`, `COVERAGE_AMOUNT`, `INTEREST_RATE`),
   then run it again.
## Example Output

```
Individual's age: 35
Policy term: 5 years
Coverage if they pass away: $100,000.00
Interest rate: 3.0%

(The calculation) premium: $618.07
(10,000-person simulation): $616.42

Difference between the two methods: $1.65
Saved Excel file: premium_table.xlsx
```
That small difference between the two numbers is expected, not an error. The simulation relies on randomness, so it won't match the formula exactly every time, but it will land close to it. It shows that the simulation confirms that the formula is correct.

# How I Used AI
I used Claude to help me learn how to translate the actuarial math I already knew into working Python code. I tested and edited the code myself along the way.
