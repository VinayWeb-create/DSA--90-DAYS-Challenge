# Problem 21: Fibonacci Series up to N Numbers
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-print-fibonacci-series-up-to-n-numbers/
#
# Print the Fibonacci series up to N terms.
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...
# ──────────────────────────────────────────────────────────────────

def fibonacci_series(n):
    if n==1:
        return [0]
    a,b=0,1
    arr=[a,b]
    for i in range(2,n):
        c=a+b
        arr.append(c)
        a,b=b,c
    return arr

# ─── Test Cases ───
if __name__ == "__main__":
    print(fibonacci_series(5))    # Expected: [0, 1, 1, 2, 3]
    print(fibonacci_series(8))    # Expected: [0, 1, 1, 2, 3, 5, 8, 13]
    print(fibonacci_series(1))    # Expected: [0]
    print(fibonacci_series(10))   # Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]