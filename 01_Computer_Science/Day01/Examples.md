# Day 01: Practical Code Examples & Memory Execution Flow

This document details practical, production-style examples for all foundational concepts with exact output and memory analysis.

---

## Example 1: Variables, Types & Memory Addresses (`id()`)

In Python, **everything is an object**. When you write `x = 10`, Python creates an integer object `10` in heap memory, and `x` is a reference (pointer) stored in the current stack frame.

```python
# Variables and Data Types
age = 21                      # int
name = "Vinay"                # str
height = 5.8                  # float
is_student = True             # bool
skills = ["Python", "React"]  # list (mutable heap object)

print(f"age: {age}, Type: {type(age)}, Memory Address: {hex(id(age))}")
print(f"name: {name}, Type: {type(name)}, Memory Address: {hex(id(name))}")
print(f"skills: {skills}, Type: {type(skills)}, Memory Address: {hex(id(skills))}")
```

### Memory Insight:
- `id(variable)` returns the unique memory address of the object in RAM.
- `hex(id(variable))` displays it in standard hexadecimal memory format (e.g., `0x7ffb3c029140`).

---

## Example 2: Control Flow & Decision Logic

```python
# Decision Making & Loops
applicant_age = 21

if applicant_age >= 18:
    status = "Eligible for Engineering Placement"
else:
    status = "Underage / Student"

print(f"Status: {status}")

# For Loop (Definite Iteration)
print("\n--- Iterating 5 Days of Challenge ---")
for day in range(1, 6):
    print(f"Day {day:02d}: Discipline > Motivation")

# While Loop (Condition-based Iteration)
print("\n--- While Loop Countdown ---")
count = 3
while count > 0:
    print(f"T-minus {count}...")
    count -= 1
print("Launch!")
```

---

## Example 3: Functions & Call Stack Frame Execution

When `calculate_net_salary` is called, the CPU pushes a new frame onto the **Call Stack**. When the function returns, this frame is immediately popped, reclaiming memory.

```python
def calculate_pf(basic_salary: float) -> float:
    # Stack frame 2: calculate_pf
    pf_rate = 0.12
    return basic_salary * pf_rate

def calculate_net_salary(ctc: float) -> float:
    # Stack frame 1: calculate_net_salary
    basic = ctc * 0.50
    pf = calculate_pf(basic)
    net = ctc - pf
    return net

monthly_ctc = 100000.0  # ₹1 Lakh/month
take_home = calculate_net_salary(monthly_ctc)
print(f"Monthly CTC: ₹{monthly_ctc:,.2f} -> Take Home: ₹{take_home:,.2f}")
```

### Stack Frame Execution Trace:
1. `__main__` is on the bottom of the stack.
2. `calculate_net_salary()` frame pushed on top.
3. `calculate_pf()` frame pushed on top of `calculate_net_salary()`.
4. `calculate_pf()` returns `6000.0` -> Frame popped.
5. `calculate_net_salary()` returns `94000.0` -> Frame popped.
6. Execution returns to `__main__`.

---

## Example 4: Multithreading (Concurrent Workers)

Here, two threads run **concurrently** inside the same Python process, sharing the same process memory space.

```python
import threading
import time

def worker_task(thread_name: str, delay: float):
    print(f"[{thread_name}] Started working...")
    for i in range(1, 4):
        time.sleep(delay)
        print(f"[{thread_name}] Completed step {i}")
    print(f"[{thread_name}] Finished!")

# Create two lightweight worker threads
t1 = threading.Thread(target=worker_task, args=("Thread-A (Job Applications)", 0.5))
t2 = threading.Thread(target=worker_task, args=("Thread-B (DSA Practice)", 0.7))

# Start both threads
t1.start()
t2.start()

# Wait for both threads to finish (join)
t1.join()
t2.join()

print("All concurrent threads completed successfully!")
```

---

## Example 5: Persistent File I/O (`open` with context manager)

```python
# Writing to permanent storage (SSD/HDD)
file_path = "day01_log.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("Day 01: Computer Science Foundations Initialized.\n")
    file.write("Goal: ₹12 LPA Software Engineer + OneBridge Social SaaS.\n")

# Reading from storage back into RAM
with open(file_path, "r", encoding="utf-8") as file:
    contents = file.read()

print("File Contents from Storage:\n" + contents)
```
