# Problem 05: Greatest of Two Numbers
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-find-the-greatest-of-two-numbers/
#
# Given two numbers, find the greatest among them.
# ──────────────────────────────────────────────────────────────────

def greatest_of_two(a, b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return a


# ─── Test Cases ───
if __name__ == "__main__":
    print(greatest_of_two(5, 10))    # Expected: 10
    print(greatest_of_two(20, 3))    # Expected: 20
    print(greatest_of_two(7, 7))     # Expected: 7
