"""
Day 01: Execution Model, Variables, Types and Memory Addresses
Demonstrating how variables and primitive types are represented and addressed.
"""

def main():
    print("=" * 60)
    print("Day 01: Python Variables, Types & Memory Addresses")
    print("=" * 60)

    # 1. Variables and Data Types
    age: int = 21
    name: str = "Vinay"
    height: float = 5.8
    is_student: bool = True
    fruits: list[str] = ["apple", "banana", "orange"]

    # 2. Type and Memory ID inspection
    print(f"age         : {age} | Type: {type(age)} | Memory: {hex(id(age))}")
    print(f"name        : {name} | Type: {type(name)} | Memory: {hex(id(name))}")
    print(f"height      : {height} | Type: {type(height)} | Memory: {hex(id(height))}")
    print(f"is_student  : {is_student} | Type: {type(is_student)} | Memory: {hex(id(is_student))}")
    print(f"fruits      : {fruits} | Type: {type(fruits)} | Memory: {hex(id(fruits))}")

    # 3. Arithmetic and Comparison Operators
    a, b = 10, 3
    print("\n--- Operators Demonstration ---")
    print(f"Addition ({a} + {b})       : {a + b}")
    print(f"Subtraction ({a} - {b})    : {a - b}")
    print(f"Multiplication ({a} * {b}) : {a * b}")
    print(f"Division ({a} / {b})       : {a / b:.4f}")
    print(f"Modulus ({a} % {b})        : {a % b}")
    print(f"Equality ({a} == {b})      : {a == b}")
    print(f"Greater than ({a} > {b})   : {a > b}")

if __name__ == "__main__":
    main()
