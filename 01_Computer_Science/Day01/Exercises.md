# Day 01: Core Practical Exercises (From Handwritten Notes)

These 10 exercises match the exact foundational checklist from your handwritten study notes. Solve them directly in Python.

---

### Exercise 1: Input & Output (Console I/O)
* **Goal:** Take user's `name` and `age` as input from the console and print a greeting that calculates what year they turn 30.
* **Hint:** Remember that `input()` returns a `str`. Use `int()` to convert age.
* **Test Case:** Name: `Vinay`, Age: `21` -> Output: `"Hello Vinay, you are 21 years old. You will turn 30 in 9 years."`

---

### Exercise 2: Even or Odd (Arithmetic Operator `%` & Branching)
* **Goal:** Ask the user for an integer and determine whether it is Even or Odd.
* **Hint:** Check if `number % 2 == 0`.

---

### Exercise 3: While Loop Counter (Indefinite Iteration)
* **Goal:** Print numbers from 1 to 10 using a `while` loop, each on a new line, followed by `"Done!"`.
* **Hint:** Initialize `i = 1` and do `i += 1` inside the loop body to prevent an infinite loop.

---

### Exercise 4: Factorial Function (Recursion & Call Stack)
* **Goal:** Write a function `factorial(n: int) -> int` using recursion. Observe how function frames are stacked.
* **Hint:** Base case: if `n <= 1` return `1`. Recursive case: return `n * factorial(n - 1)`.
* **Edge Case:** Handle `0` properly.

---

### Exercise 5: File Word Counter (Storage to RAM Streaming)
* **Goal:** Create a file named `sample.txt`, write a paragraph into it, then write a function that reads the file and returns the total word count.
* **Hint:** Use `with open(...)`, `content.split()`, and `len()`.

---

### Exercise 6: List Traversal (Heap Object Iteration)
* **Goal:** Create a list of 5 fruits. Print each fruit in uppercase with its 1-based index (e.g., `1. APPLE`, `2. MANGO`).
* **Hint:** Use `for idx, fruit in enumerate(fruits, start=1):`.

---

### Exercise 7: Concurrent Worker Threads (`threading`)
* **Goal:** Spawn two threads (`Thread-Alpha` and `Thread-Beta`). Both should print a progress message 3 times with a 0.3-second delay between prints. Ensure the main program waits for both using `.join()`.
* **Hint:** `from threading import Thread` and `import time`.

---

### Exercise 8: Sum of List (Array Accumulator Pattern)
* **Goal:** Write a function `sum_list(numbers: list[float]) -> float` without using Python's built-in `sum()` function.
* **Hint:** Initialize an accumulator `total = 0.0` and loop through each item.

---

### Exercise 9: Student Record Storage (Persistence)
* **Goal:** Write a program that takes student records (Name, Roll Number, Target Package) and appends them to a file named `students.csv`.
* **Format:** `Vinay,101,12 LPA`

---

### Exercise 10: Stack vs. Heap ID Inspector (`id()`)
* **Goal:**
  1. Create two integer variables with the same value (`a = 100`, `b = 100`). Check if `id(a) == id(b)` (Python integer interning).
  2. Create two identical lists (`list1 = [1, 2, 3]`, `list2 = [1, 2, 3]`). Check if `id(list1) == id(list2)`. Explain why lists have different IDs even when contents are identical!
