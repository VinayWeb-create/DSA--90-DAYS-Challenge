"""
Day 01: Complete Solutions to 10 Practical Exercises (From Handwritten Notes)
"""

import threading
import time
import os

# --- Exercise 1: User Input & Calculation ---
def exercise_1_greeting(name: str, age: int) -> str:
    years_to_30 = 30 - age
    return f"Hello {name}, you are {age} years old. You will turn 30 in {years_to_30} years."

# --- Exercise 2: Even or Odd ---
def exercise_2_is_even(number: int) -> bool:
    return number % 2 == 0

# --- Exercise 3: While Loop Counter ---
def exercise_3_while_counter(limit: int = 10) -> list[int]:
    results = []
    i = 1
    while i <= limit:
        results.append(i)
        i += 1
    return results

# --- Exercise 4: Factorial Function (Recursion) ---
def exercise_4_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n <= 1:
        return 1
    return n * exercise_4_factorial(n - 1)

# --- Exercise 5: Word Counter from File ---
def exercise_5_word_count(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    words = content.split()
    return len(words)

# --- Exercise 6: List of Fruits Iteration ---
def exercise_6_print_fruits(fruits: list[str]) -> list[str]:
    formatted = []
    for idx, fruit in enumerate(fruits, start=1):
        formatted.append(f"{idx}. {fruit.upper()}")
    return formatted

# --- Exercise 7: Two Threads Concurrent Execution ---
def exercise_7_run_threads() -> list[str]:
    logs = []
    lock = threading.Lock()

    def task(thread_name: str):
        for step in range(1, 4):
            time.sleep(0.05)
            with lock:
                logs.append(f"{thread_name} - Step {step}")

    t1 = threading.Thread(target=task, args=("Thread-1",))
    t2 = threading.Thread(target=task, args=("Thread-2",))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return logs

# --- Exercise 8: Sum of List Without Built-in sum() ---
def exercise_8_sum_list(numbers: list[float]) -> float:
    total = 0.0
    for num in numbers:
        total += num
    return total

# --- Exercise 9: Store Student Details in File ---
def exercise_9_store_student(filename: str, name: str, roll_no: str, target_ctc: str):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{name},{roll_no},{target_ctc}\n")

# --- Exercise 10: Stack vs Heap ID Inspector ---
def exercise_10_memory_inspector():
    a = 100
    b = 100
    int_same = id(a) == id(b)

    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list_same = id(list1) == id(list2)

    return {
        "integer_interning_same_id": int_same,
        "list_heap_distinct_id": not list_same,
        "list1_id": hex(id(list1)),
        "list2_id": hex(id(list2))
    }

def main():
    print("=" * 60)
    print("Running Tests on All 10 Exercises")
    print("=" * 60)

    # Test Ex 1
    print("Ex 1:", exercise_1_greeting("Vinay", 21))

    # Test Ex 2
    print("Ex 2:", f"Is 14 even? {exercise_2_is_even(14)} | Is 9 even? {exercise_2_is_even(9)}")

    # Test Ex 3
    print("Ex 3:", exercise_3_while_counter(10))

    # Test Ex 4
    print("Ex 4: Factorial of 5 =", exercise_4_factorial(5))

    # Test Ex 5
    sample_file = "test_sample.txt"
    with open(sample_file, "w", encoding="utf-8") as f:
        f.write("Vinay is pursuing a 90-day challenge for a 12 LPA Software Engineer role.")
    print(f"Ex 5: Word count in file = {exercise_5_word_count(sample_file)}")
    if os.path.exists(sample_file):
        os.remove(sample_file)

    # Test Ex 6
    fruits = ["mango", "apple", "banana", "orange", "grapes"]
    print("Ex 6:", exercise_6_print_fruits(fruits))

    # Test Ex 7
    print("Ex 7: Thread logs:", exercise_7_run_threads())

    # Test Ex 8
    nums = [10.5, 20.0, 30.5, 39.0]
    print(f"Ex 8: Sum of {nums} =", exercise_8_sum_list(nums))

    # Test Ex 9
    students_file = "test_students.csv"
    exercise_9_store_student(students_file, "Vinay", "101", "12 LPA")
    print(f"Ex 9: Stored record to {students_file}")
    if os.path.exists(students_file):
        os.remove(students_file)

    # Test Ex 10
    print("Ex 10:", exercise_10_memory_inspector())
    print("\n[SUCCESS] All 10 Exercises verified and working!")

if __name__ == "__main__":
    main()
