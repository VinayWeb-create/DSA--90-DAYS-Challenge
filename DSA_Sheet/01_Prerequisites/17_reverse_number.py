# Problem 17: Reverse of a Number
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-find-the-reverse-of-a-number/
#
# Given a number, reverse its digits.
# ──────────────────────────────────────────────────────────────────

def reverse_number(n):
    rev=0
    while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev


# ─── Test Cases ───
if __name__ == "__main__":
    print(reverse_number(1234))    # Expected: 4321
    print(reverse_number(100))     # Expected: 1
    print(reverse_number(7))       # Expected: 7
