# Problem 01: Check Whether a Number is Positive or Negative
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-check-whether-a-number-is-positive-or-negative/
#
# Given a number, check whether it is positive, negative, or zero.
# ──────────────────────────────────────────────────────────────────

def check_positive_negative(n):
    if n==0:
        return("Zero")
    elif n>0:
        return("Positive")
    else:
        return("Negative")


# ─── Test Cases ───
if __name__ == "__main__":
    print(check_positive_negative(5))    # Expected: "Positive"
    print(check_positive_negative(-3))   # Expected: "Negative"
    print(check_positive_negative(0))    # Expected: "Zero"
