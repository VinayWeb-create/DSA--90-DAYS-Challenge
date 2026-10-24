# Problem 19: Check Whether a Number is Armstrong
# Reference: https://prepinsta.com/cpp-program/to-check-whether-a-number-is-armstrong-number-or-not/
#
# An Armstrong number of n digits is a number where the sum of each digit
# raised to the power of n equals the number itself.
# Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
# ──────────────────────────────────────────────────────────────────

def is_armstrong(n):
    digits=len(str(n))
    duplicate=n
    sum=0
    while n!=0:
        d=n%10
        sum+=d**digits
        n=n//10
    if sum==duplicate:
        return True
    else:
        return False


# ─── Test Cases ───
if __name__ == "__main__":
    print(is_armstrong(153))    # Expected: True
    print(is_armstrong(370))    # Expected: True
    print(is_armstrong(123))    # Expected: False
    print(is_armstrong(9474))   # Expected: True
