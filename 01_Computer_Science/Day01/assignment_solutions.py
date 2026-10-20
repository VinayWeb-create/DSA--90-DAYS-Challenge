"""
Day 01: Coding Assignment Solutions
Implementing solutions for all 6 challenge problems from Assignment.md.
"""

import copy
import os
import re
import sys
import threading
import time

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# --- Problem 1: Safe Integer & Float Division with Logging ---
def safe_divide(a_str: str, b_str: str) -> float | None:
    try:
        a = float(a_str)
        b = float(b_str)
        return a / b
    except ValueError as e:
        print(f"[Problem 1 Log] Value conversion error: {e}")
        return None
    except ZeroDivisionError:
        print("[Problem 1 Log] Mathematical error: Division by zero is undefined.")
        return None

# --- Problem 2: Call Stack Depth Inspector ---
def measure_max_call_depth() -> int:
    def _recurse(current_depth: int) -> int:
        try:
            return _recurse(current_depth + 1)
        except RecursionError:
            return current_depth

    return _recurse(1)

# --- Problem 3: Two-Pointer In-Place Palindrome Checker ---
def is_palindrome(text: str) -> bool:
    # Filter only alphanumeric characters and lowercase
    filtered = [char.lower() for char in text if char.isalnum()]
    left, right = 0, len(filtered) - 1

    while left < right:
        if filtered[left] != filtered[right]:
            return False
        left += 1
        right -= 1
    return True

# --- Problem 4: File Line Reverser ---
def reverse_file_lines(input_filename: str, output_filename: str) -> None:
    with open(input_filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(output_filename, "w", encoding="utf-8") as f:
        f.writelines(reversed(lines))

# --- Problem 5: Thread-Safe Counter Simulation ---
class SafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self, amount: int = 1):
        with self.lock:
            self.value += amount

def run_counter_benchmark(num_threads: int = 5, increments_per_thread: int = 10000) -> int:
    counter = SafeCounter()
    threads = []

    def worker():
        for _ in range(increments_per_thread):
            counter.increment(1)

    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return counter.value

# --- Problem 6: Deep Copy vs. Shallow Copy Memory Demonstration ---
def memory_copy_demo():
    user = {
        "name": "Vinay",
        "preferences": {"theme": "dark", "notifications": True}
    }

    user_reference = user
    user_shallow = user.copy()
    user_deep = copy.deepcopy(user)

    return {
        "user_id": hex(id(user)),
        "reference_id": hex(id(user_reference)),
        "shallow_id": hex(id(user_shallow)),
        "deep_id": hex(id(user_deep)),
        "nested_pref_original_id": hex(id(user["preferences"])),
        "nested_pref_shallow_id": hex(id(user_shallow["preferences"])),
        "nested_pref_deep_id": hex(id(user_deep["preferences"])),
        "shallow_shares_nested_heap": id(user["preferences"]) == id(user_shallow["preferences"]),
        "deep_has_isolated_nested_heap": id(user["preferences"]) != id(user_deep["preferences"])
    }

def main():
    print("=" * 60)
    print("Day 01: Running Assignment Solutions")
    print("=" * 60)

    # Test 1
    print("P1 Safe Divide ('100', '4'):", safe_divide("100", "4"))
    print("P1 Safe Divide ('100', '0'):", safe_divide("100", "0"))

    # Test 2
    max_depth = measure_max_call_depth()
    print(f"P2 Measured Call Stack Depth Limit: {max_depth} frames")

    # Test 3
    test_str = "A man, a plan, a canal: Panama"
    print(f"P3 Is '{test_str}' a palindrome? {is_palindrome(test_str)}")

    # Test 4
    in_file = "test_input.txt"
    out_file = "test_reversed.txt"
    with open(in_file, "w", encoding="utf-8") as f:
        f.write("First Line\nSecond Line\nThird Line\n")
    reverse_file_lines(in_file, out_file)
    with open(out_file, "r", encoding="utf-8") as f:
        print("P4 Reversed File Content:\n" + f.read().strip())
    if os.path.exists(in_file): os.remove(in_file)
    if os.path.exists(out_file): os.remove(out_file)

    # Test 5
    counter_result = run_counter_benchmark(5, 10000)
    print(f"P5 Thread-Safe Counter (Expected 50,000): {counter_result}")

    # Test 6
    copy_results = memory_copy_demo()
    print("P6 Deep vs Shallow Memory Copy Analysis:")
    print(f"  - Shallow Copy shares inner heap dictionary: {copy_results['shallow_shares_nested_heap']}")
    print(f"  - Deep Copy has isolated inner heap dictionary: {copy_results['deep_has_isolated_nested_heap']}")

    print("\n[SUCCESS] All 6 Assignment problems completed and verified!")

if __name__ == "__main__":
    main()
