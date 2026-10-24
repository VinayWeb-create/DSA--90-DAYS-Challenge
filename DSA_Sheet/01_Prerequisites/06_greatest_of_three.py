# Problem 06: Greatest of Three Numbers
# Reference: https://prepinsta.com/cpp-program/to-find-the-greatest-of-three-numbers/
#
# Given three numbers, find the greatest among them.
# ──────────────────────────────────────────────────────────────────

def greatest_of_three(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c


# ─── Test Cases ───
if __name__ == "__main__":
    print(greatest_of_three(5, 10, 3))    # Expected: 10
    print(greatest_of_three(20, 3, 15))   # Expected: 20
    print(greatest_of_three(7, 7, 7))     # Expected: 7
