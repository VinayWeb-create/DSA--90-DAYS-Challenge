# Problem 24: Power of a Number
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-find-the-power-of-a-number/
#
# Given base and exponent, calculate base^exponent (without using built-in pow).
# ──────────────────────────────────────────────────────────────────

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result



# ─── Test Cases ───
if __name__ == "__main__":
    print(power(2, 10))    # Expected: 1024
    print(power(5, 3))     # Expected: 125
    print(power(7, 0))     # Expected: 1
