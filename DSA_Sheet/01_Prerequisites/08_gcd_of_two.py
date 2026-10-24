# Problem 08: GCD or HCF of Two Numbers
# Reference: https://www.geeksforgeeks.org/dsa/program-to-find-gcd-or-hcf-of-two-numbers/
#
# Given two numbers, find their Greatest Common Divisor (GCD) / Highest Common Factor (HCF).
# ──────────────────────────────────────────────────────────────────

def find_gcd(a, b):
    if a<b:
        min=a
    else:
        min=b
    for i in range(min,0,-1):
        if a%i==0 and b%i==0:
            return i


# ─── Test Cases ───
if __name__ == "__main__":
    print(find_gcd(12, 8))    # Expected: 4
    print(find_gcd(15, 25))   # Expected: 5
    print(find_gcd(7, 3))     # Expected: 1
