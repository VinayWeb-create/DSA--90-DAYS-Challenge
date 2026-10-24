# Problem 02: Check Whether a Number is Even or Odd
# Reference: https://prepinsta.com/cpp-program/to-check-whether-a-number-is-even-or-odd/
#
# Given a number, check whether it is even or odd.
# ──────────────────────────────────────────────────────────────────


def check_even_odd(n):

    if n%2==0:
        return("Even")
    else:
        return("Odd")

# ─── Test Cases ───
if __name__ == "__main__":
    print(check_even_odd(4))   # Expected: "Even"
    print(check_even_odd(7))   # Expected: "Odd"
    print(check_even_odd(0))   # Expected: "Even"
