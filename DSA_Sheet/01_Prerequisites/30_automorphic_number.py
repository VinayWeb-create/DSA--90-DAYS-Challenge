# Problem 30: Check Whether a Number is Automorphic
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-check-whether-a-number-is-an-automorphic-number-or-not/
#
# An Automorphic number is a number whose square ends with the number itself.
# Example: 25 → 25² = 625 → ends with 25 ✓
# Example: 76 → 76² = 5776 → ends with 76 ✓
# ──────────────────────────────────────────────────────────────────

def is_automorphic(n):
    # Write your code here
    pass


# ─── Test Cases ───
if __name__ == "__main__":
    print(is_automorphic(25))    # Expected: True
    print(is_automorphic(76))    # Expected: True
    print(is_automorphic(13))    # Expected: False
    print(is_automorphic(5))     # Expected: True
