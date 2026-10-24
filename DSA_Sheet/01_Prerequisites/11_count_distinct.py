# Problem 11: Count Distinct Elements in an Array
# Reference: https://www.geeksforgeeks.org/dsa/count-distinct-elements-in-an-array/
#
# Given an array, count the number of distinct/unique elements.
# ──────────────────────────────────────────────────────────────────

def count_distinct(arr):
    distinct=0
    for i in range(len(arr)):   
        for j in range(i+1,len(arr)):
            if arr[i]!=arr[i+1]:
                distinct+=1
                break
    return distinct

# ─── Test Cases ───
if __name__ == "__main__":
    print(count_distinct([1, 2, 1, 3, 4, 2]))       # Expected: 4
    print(count_distinct([1, 1, 1, 1]))              # Expected: 1
    print(count_distinct([1, 2, 3, 4, 5]))           # Expected: 5
