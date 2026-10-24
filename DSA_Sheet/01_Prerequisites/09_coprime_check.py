# Problem 09: Check if Two Numbers are Co-Prime
# Reference: https://www.geeksforgeeks.org/dsa/check-two-numbers-co-prime-not/
#
# Two numbers are co-prime if their GCD is 1. Check if given two numbers are co-prime.
# ──────────────────────────────────────────────────────────────────

def are_coprime(a, b):
    if a<b:
        min=a
    else:
        min=b
    for i in range(min,0,-1):
        if a%i==0 and b%i==0:
            Gcd=i
            break

    if Gcd==1:
        return True
    else:
        return False





# ─── Test Cases ───
if __name__ == "__main__":
    print(are_coprime(14, 15))   # Expected: True
    print(are_coprime(12, 8))    # Expected: False
    print(are_coprime(7, 13))    # Expected: True
