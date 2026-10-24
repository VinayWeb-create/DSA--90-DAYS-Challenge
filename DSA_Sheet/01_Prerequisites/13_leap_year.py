# Problem 13: Check Leap Year
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-check-whether-a-year-is-a-leap-year-or-not/
#
# Given a year, check whether it is a leap year or not.
# Rules: Divisible by 4 AND (not divisible by 100 OR divisible by 400).
# ──────────────────────────────────────────────────────────────────

def is_leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

# ─── Test Cases ───
if __name__ == "__main__":
    print(is_leap_year(2024))   # Expected: True
    print(is_leap_year(1900))   # Expected: False
    print(is_leap_year(2000))   # Expected: True
    print(is_leap_year(2023))   # Expected: False
