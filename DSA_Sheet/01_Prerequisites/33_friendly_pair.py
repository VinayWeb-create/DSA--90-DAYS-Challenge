# Problem 33: Check Whether Two Numbers are Friendly Pair (Amicable Numbers)
# Reference: https://prepinsta.com/cpp-program/to-check-whether-two-numbers-are-friendly-pairamicable-number-or-not/
#
# Two numbers are a Friendly Pair if the ratio of each number to the sum of its
# divisors (abundancy) is the same for both.
# Abundancy of N = σ(N) / N, where σ(N) is the sum of ALL divisors of N.
# ──────────────────────────────────────────────────────────────────

def are_friendly_pair(a, b):
    # Write your code here
    pass


# ─── Test Cases ───
if __name__ == "__main__":
    print(are_friendly_pair(6, 28))       # Expected: True  (both have abundancy 2)
    print(are_friendly_pair(30, 140))     # Expected: True  (both have abundancy 12/5)
    print(are_friendly_pair(5, 10))       # Expected: False
