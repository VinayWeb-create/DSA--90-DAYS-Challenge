# Problem 20: Armstrong Numbers Between Two Intervals
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-find-armstrong-numbers-between-two-intervals/
#
# Given two numbers L and R, find all Armstrong numbers between them (inclusive).
# ──────────────────────────────────────────────────────────────────

def armstrong_in_range(l, r):
    arr=[]
    for i in range(l,r+1):
        digits=len(str(i))
        duplicate=i
        sum=0
        while duplicate!=0:
            d=duplicate%10
            sum+=d**digits
            duplicate//=10
        if sum==i:
            arr.append(i)
    return arr



# ─── Test Cases ───
if __name__ == "__main__":
    print(armstrong_in_range(1, 500))       # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
    print(armstrong_in_range(100, 999))     # Expected: [153, 370, 371, 407]
    print(armstrong_in_range(1000, 9999))   # Expected: [1634, 8208, 9474]
