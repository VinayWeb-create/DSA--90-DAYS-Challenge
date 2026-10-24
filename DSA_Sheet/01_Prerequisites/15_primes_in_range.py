# Problem 15: Prime Numbers in a Given Range
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-find-prime-numbers-in-a-given-range/
#
# Given two numbers L and R, find all prime numbers between L and R (inclusive).
# ──────────────────────────────────────────────────────────────────

def primes_in_range(l,r):
    primes=[]
    for i in range(l,r+1):
        if i<2:
            continue
        is_prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            primes.append(i)
    return primes

# ─── Test Cases ───
if __name__ == "__main__":
    print(primes_in_range(1, 20))    # Expected: [2, 3, 5, 7, 11, 13, 17, 19]
    print(primes_in_range(10, 30))   # Expected: [11, 13, 17, 19, 23, 29]
    print(primes_in_range(1, 2))     # Expected: [2]
