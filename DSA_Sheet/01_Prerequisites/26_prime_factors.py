# Problem 26: Prime Factors of a Number
# Reference: https://prepinsta.com/cpp-program/finding-prime-factors-of-a-number/
#
# Given a number N, find all its prime factors.
# ──────────────────────────────────────────────────────────────────

def prime_factors(n):
    factors = []
    
    # Divide out all 2s
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2

    # Check odd numbers from 3 onwards
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 2
        
    # If n is still greater than 2, the remainder is prime
    if n > 2:
        factors.append(n)

    return factors

# ─── Test Cases ───
if __name__ == "__main__":
    print(prime_factors(12))    # Expected: [2, 3]
    print(prime_factors(315))   # Expected: [3, 5, 7]
    print(prime_factors(13))    # Expected: [13]
