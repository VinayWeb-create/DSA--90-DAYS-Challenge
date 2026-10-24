# Problem 25: Factors of a Number
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-find-the-factors-of-a-number/
#
# Given a number N, find all its factors (divisors).
# ──────────────────────────────────────────────────────────────────

def find_factors(n):
    factors=[]
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)
    return factors
   


# ─── Test Cases ───
if __name__ == "__main__":
    print(find_factors(12))    # Expected: [1, 2, 3, 4, 6, 12]
    print(find_factors(7))     # Expected: [1, 7]
    print(find_factors(100))   # Expected: [1, 2, 4, 5, 10, 20, 25, 50, 100]
