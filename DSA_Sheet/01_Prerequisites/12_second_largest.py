# Problem 12: Find Second Largest Element in an Array
# Reference: https://www.geeksforgeeks.org/dsa/find-second-largest-element-array/
#
# Given an array, find the second largest element.
# ──────────────────────────────────────────────────────────────────

def second_largest(arr):
    largest=0
    for i in arr:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest and i!=largest:
            second_largest=i
    if second_largest==0:
        return None
    else:
        return second_largest


# ─── Test Cases ───
if __name__ == "__main__":
    print(second_largest([12, 35, 1, 10, 34, 1]))   # Expected: 34
    print(second_largest([10, 5, 10]))               # Expected: 5
    print(second_largest([10, 10, 10]))              # Expected: None (no second largest)
