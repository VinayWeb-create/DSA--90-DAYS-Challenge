# Problem 04: Sum of Numbers in a Given Range
# Reference: https://prepinsta.com/cpp-program/to-find-the-sum-of-numbers-in-a-given-range/
#
# Given two numbers L and R, find the sum of all numbers from L to R (inclusive).
# ──────────────────────────────────────────────────────────────────

def sum_in_range(l, r):
    sum=0
    for i in range(l,r+1):
        sum+=i
    return sum


# ─── Test Cases ───
if __name__ == "__main__":
    print(sum_in_range(1, 5))     # Expected: 15
    print(sum_in_range(3, 7))     # Expected: 25
    print(sum_in_range(10, 10))   # Expected: 10
