# Problem 27: Strong Number
# Reference: https://prepinsta.com/cpp-program/cpp-program-to-check-whether-a-number-is-a-strong-number-or-not/
#
# A Strong Number is a number where the sum of factorial of each digit equals the number.
# Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145
# ──────────────────────────────────────────────────────────────────


def is_strong_number(n: int)->bool:
    if n<=0:
        return False
    temp=n
    total_sum=0
    while n>0:
        d=n%10
        fact=1
        for i in range(1,d+1):
            fact*=i
        total_sum+=fact
        n//=10
    return temp==total_sum

# ─── Test Cases ───
if __name__ == "__main__":
    print(is_strong_number(145))   # Expected: True
    print(is_strong_number(40585)) # Expected: True
    print(is_strong_number(123))   # Expected: False
