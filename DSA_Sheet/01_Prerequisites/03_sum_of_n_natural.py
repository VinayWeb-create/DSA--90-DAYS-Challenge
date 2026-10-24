# Problem 03: Sum of N Natural Numbers
# Reference: https://prepinsta.com/cpp-program/to-find-the-sum-of-n-natural-numbers/
#
# Given a number N, find the sum of first N natural numbers (1 + 2 + ... + N).
# ──────────────────────────────────────────────────────────────────

def sum_of_n_natural(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum



# ─── Test Cases ───
if __name__ == "__main__":
    print(sum_of_n_natural(5))    # Expected: 15
    print(sum_of_n_natural(10))   # Expected: 55
    print(sum_of_n_natural(1))    # Expected: 1
