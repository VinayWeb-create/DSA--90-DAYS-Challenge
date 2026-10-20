# Day 01: Coding Assignment (Increasing Difficulty)

Complete these 6 challenge problems. Write clean, PEP8-compliant code with type hints.

---

### Problem 1: Safe Integer Parsing with Error Handling
Write a function `safe_divide(a_str: str, b_str: str) -> float | None` that converts strings to floats, divides `a` by `b`, and returns the result. If a conversion fails (ValueError) or division by zero occurs (ZeroDivisionError), handle the exception gracefully and return `None` with an informative error log.

---

### Problem 2: Call Stack Depth Inspector
Write a recursive function `measure_max_call_depth(current_depth: int = 1) -> int` that continues recursing until Python raises a `RecursionError`. Catch the exception and return the maximum call stack depth before overflow.

---

### Problem 3: Palindrome Checker (Strings & Memory)
Write an in-place two-pointer palindrome checker `is_palindrome(text: str) -> bool` that ignores spaces, punctuation, and letter casing.  
*Example:* `"A man, a plan, a canal: Panama"` -> `True`.  
*Constraint:* Do not create unnecessary reversed copies of the string in memory.

---

### Problem 4: File Line Reverser
Write a script `reverse_file_lines(input_filename: str, output_filename: str) -> None` that reads a file and writes its lines in reverse order into the output file.

---

### Problem 5: Thread-Safe Counter Simulation
Create a shared counter variable initialized to 0. Spawn 5 threads, where each thread increments the counter 10,000 times. Observe what happens without a lock versus with `threading.Lock()`.

---

### Problem 6: Deep Copy vs. Shallow Copy Memory Demonstration
Create a nested dictionary representing a user profile:
```python
user = {"name": "Vinay", "preferences": {"theme": "dark", "notifications": True}}
```
Demonstrate what happens when you do:
1. Direct assignment (`user2 = user`)
2. Shallow copy (`user3 = user.copy()`)
3. Deep copy (`user4 = copy.deepcopy(user)`)  
Inspect `id()` of the outer dictionary and the inner `preferences` dictionary for each case.
