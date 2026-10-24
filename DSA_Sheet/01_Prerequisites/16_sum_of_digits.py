# Problem 16: Sum of Digits of a Number
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-find-the-sum-of-digits-of-a-number/
#
# Given a number, find the sum of its digits.
# ──────────────────────────────────────────────────────────────────

def sum_of_digits(n):
    sum=0
    while n!=0:
        sum+=n%10
        n=n//10
    return sum



# ─── Test Cases ───
if __name__ == "__main__":
    print(sum_of_digits(123))    # Expected: 6
    print(sum_of_digits(9999))   # Expected: 36
    print(sum_of_digits(0))      # Expected: 0
