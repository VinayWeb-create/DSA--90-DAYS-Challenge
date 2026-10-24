# Problem 22: Nth Term of Fibonacci Series
# Reference: https://prepinsta.com/cpp-program/finding-the-nth-term-of-the-fibonacci-series/
#
# Given N, find the Nth term of the Fibonacci series (0-indexed).
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...
# ──────────────────────────────────────────────────────────────────

def nth_fibonacci(n):
    if n==0:
        return 0
    a,b=0,1
    arr=[a,b]
    for i in range(2,n+1):
        c=a+b
        arr.append(c)
        a,b=b,c
    return arr[n]

# ─── Test Cases ───
if __name__ == "__main__":
    print(nth_fibonacci(0))    # Expected: 0
    print(nth_fibonacci(5))    # Expected: 5
    print(nth_fibonacci(10))   # Expected: 55
    print(nth_fibonacci(1))    #Expected: 1
