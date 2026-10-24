# Problem 23: Factorial of a Number
# Reference: https://prepinsta.com/cpp-program/to-find-the-factorial-of-a-number/
#
# Given a number N, find its factorial (N! = N × (N-1) × ... × 1).
# ──────────────────────────────────────────────────────────────────

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact


# ─── Test Cases ───
if __name__ == "__main__":
    print(factorial(5))    # Expected: 120
    print(factorial(0))    # Expected: 1
    print(factorial(10))   # Expected: 3628800
