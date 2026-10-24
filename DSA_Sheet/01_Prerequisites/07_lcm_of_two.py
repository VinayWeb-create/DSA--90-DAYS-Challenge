# Problem 07: LCM of Two Numbers
# Reference: https://www.geeksforgeeks.org/dsa/program-to-find-lcm-of-two-numbers/
#
# Given two numbers, find their Least Common Multiple (LCM).
# ──────────────────────────────────────────────────────────────────

def find_lcm(a, b):
    if a>b:
        max=a
    else:
        max=b
    while True:
        if max%a==0 and max%b==0:
            return max
        max+=1


# ─── Test Cases ───
if __name__ == "__main__":
    print(find_lcm(4, 6))     # Expected: 12
    print(find_lcm(12, 15))   # Expected: 60
    print(find_lcm(7, 3))     # Expected: 21
