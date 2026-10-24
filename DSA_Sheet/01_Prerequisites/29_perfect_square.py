# Problem 29: Check for Perfect Square
# Reference: https://prepinsta.com/cpp-program/to-check-for-perfect-square/
#
# Given a number, check whether it is a perfect square.
# ──────────────────────────────────────────────────────────────────

from math import sqrt
def is_perfect_square(n: int)->bool:
    if n>=0:
        squre_digit=int(sqrt(n))
        return squre_digit*squre_digit==n
    return False
# ─── Test Cases ───
if __name__ == "__main__":
    print(is_perfect_square(25))    # Expected: True
    print(is_perfect_square(14))    # Expected: False
    print(is_perfect_square(1))     # Expected: True
    print(is_perfect_square(0))     # Expected: True
