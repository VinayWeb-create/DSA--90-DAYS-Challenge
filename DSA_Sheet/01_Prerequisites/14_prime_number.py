# Problem 14: Prime Number
# Reference: https://prepinsta.com/cpp-program/prime-number/
#
# Given a number, check whether it is a prime number or not.
# A prime number is greater than 1 and has no divisors other than 1 and itself.
# ──────────────────────────────────────────────────────────────────

def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
    return True


# ─── Test Cases ───
if __name__ == "__main__":
    print(is_prime(7))    # Expected: True
    print(is_prime(10))   # Expected: False
    print(is_prime(1))    # Expected: False
    print(is_prime(2))    # Expected: True
