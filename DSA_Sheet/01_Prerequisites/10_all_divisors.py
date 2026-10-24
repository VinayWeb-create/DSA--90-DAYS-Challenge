# Problem 10: Find All Divisors of a Number
# Reference: https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1
#
# Given a number N, find all its divisors in sorted order.
# ──────────────────────────────────────────────────────────────────

def find_all_divisors(n):
    divisors=[]
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
    return divisors

# ─── Test Cases ───
if __name__ == "__main__":
    print(find_all_divisors(12))   # Expected: [1, 2, 3, 4, 6, 12]
    print(find_all_divisors(7))    # Expected: [1, 7]
    print(find_all_divisors(36))   # Expected: [1, 2, 3, 4, 6, 9, 12, 18, 36]
