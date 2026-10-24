# Problem 18: Check Whether a Number is Palindrome
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-check-whether-a-number-is-palindrome-or-not/
#
# A number is a palindrome if it reads the same forwards and backwards.
# ──────────────────────────────────────────────────────────────────

def is_palindrome(n):
    duplicate=n
    rev=0
    while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
    if duplicate==rev:
        return True
    else:
        return False


# ─── Test Cases ───
if __name__ == "__main__":
    print(is_palindrome(121))     # Expected: True
    print(is_palindrome(123))     # Expected: False
    print(is_palindrome(1221))    # Expected: True
