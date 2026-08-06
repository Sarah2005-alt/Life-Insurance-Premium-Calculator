# Life Insurance Premium Calculator

This is a small Python project I built to combine what I'm learning in
actuarial science with some hands-on coding practice. It calculates a
fair life insurance premium and checks the math using a simulation.

## What it does

Given someone's age, a policy term (in years), a coverage amount, and
an interest rate, the program:

1. Calculates the theoretical premium using expected value math (the
   probability of dying each year, weighted by the payout, discounted
   back to today's money)
2. Double-checks that number by simulating 10,000 fake policyholders
   and seeing what the average payout actually comes out to
3. Prints both results so you can compare them
4. Exports a full rate table (ages 18-76) to an Excel file, so you can
   see how the premium changes across different ages

## Why two methods?

The math formula gives the "correct" theoretical answer, but I wanted
proof it was actually right, not just trust the formula blindly. The
simulation is a reality check — if thousands of randomly simulated
people average out close to the formula's answer, that's good evidence
the math is doing what it's supposed to.

## Data source

The mortality probabilities (chance of dying at each age) come from
the Social Security Administration's 2023 Period Life Table, Female
column:
https://www.ssa.gov/oact/STATS/table4c6.html

I only used ages 18-80 from the table, and only the female column, to
keep the project manageable in scope.

## Why the age range stops at 76

This isn't a bug — it's intentional. The mortality data only goes up
to age 80, and since the policy term is 5 years, the oldest person the
calculator can handle is 76 (76 + 5 - 1 = 80). Also, real term-life
insurance rarely covers people much older than that anyway, so I didn't
see a need to extend the data further.

## How to run it

1. Install the one thing it needs:
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

## Example output

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

## Limitations

- Only uses female mortality data, not male
- The simulation result changes slightly every time you run it, since
  it's based on randomness — that's expected, not a bug
- Only works for starting ages 18-76 given the 5-year term

## How I used AI

I used Claude to help me learn how to translate the actuarial math I
already knew into working Python code, since I hadn't built something
like this before. It helped me understand concepts like discounting
and Monte Carlo simulation in plain terms, and helped me debug an issue
where the Excel export crashed for older ages. I tested the code myself
after every change, rewrote the comments in my own words, and made the
final decisions on scope (like sticking with one gender and capping the
age range) rather than just accepting the first version I was given.
