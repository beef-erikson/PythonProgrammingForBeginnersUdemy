"""Function that calculates a simple interest formula.
"""


def simple_interest(principal: float, interest: float, duration_in_years: int):
    """A simple interest formula to print gain using the parameters provided.
    """
    print(f"Your investment: ${principal * (interest / 100) * duration_in_years + principal} "
          f"in {duration_in_years} years")


simple_interest(10000, 5, 5)
