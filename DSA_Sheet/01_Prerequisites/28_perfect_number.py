# Problem 28: Perfect Number
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-check-whether-a-number-is-perfect-number-or-not/
#
# A Perfect Number is a number where the sum of its proper divisors (excluding itself) equals the number.
# Example: 6 = 1 + 2 + 3
# ──────────────────────────────────────────────────────────────────

def is_perfect_number(n: int)->bool:
    if n<=0:
        return False
    temp=n
    sum_of_divisiors=0
    for i in range(1,n-1):
        if n%i==0:
            sum_of_divisiors+=i
    return temp==sum_of_divisiors


# ─── Test Cases ───
if __name__ == "__main__":
    print(is_perfect_number(6))     # Expected: True
    print(is_perfect_number(28))    # Expected: True
    print(is_perfect_number(12))    # Expected: False
