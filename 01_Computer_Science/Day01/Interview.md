# Day 01: ₹12 LPA Interview Questions & Model Answers

Master these questions. Practice saying the answers out loud until you can explain them clearly and confidently without looking at notes.

---

### Question 1: What is the fundamental difference between a Process and a Thread?
**Model Answer:**  
"A **process** is an independent executing program allocated its own isolated virtual address space, file handles, and system resources by the operating system. Because processes are isolated, one crashing does not bring down another.
A **thread**, on the other hand, is the smallest schedulable execution unit inside a process. Threads within the same process share the same heap memory, data segment, and open files, but maintain their own independent stack and program counter.
Threads are much cheaper to create and context-switch than processes, but require synchronization mechanisms like mutex locks to prevent race conditions when modifying shared heap memory."

---

### Question 2: Explain Stack vs. Heap memory. Where do Python variables live?
**Model Answer:**  
"The **Stack** is organized as a strict Last-In-First-Out (LIFO) structure managed directly by the CPU instruction set. When a function is invoked, a stack frame containing return addresses, function arguments, and local primitive references is pushed. When the function returns, the frame is popped immediately, making stack allocation and deallocation virtually instant.
The **Heap** is an unstructured pool of free memory used for dynamic allocation, where objects can outlive the scope of the function that instantiated them.
In Python, **all objects (strings, integers, lists, instances) are allocated on the Heap**. The local variable names in your code simply reside in the Stack frame as references (pointers) pointing to those heap memory addresses."

---

### Question 3: What causes a Stack Overflow error versus an Out-of-Memory (OOM) error?
**Model Answer:**  
"A **Stack Overflow** occurs when the call stack exceeds its allocated memory ceiling, almost always due to infinite or excessively deep recursion without reaching a base case.
An **Out-of-Memory (OOM)** error occurs when the heap space runs out of available RAM because the application is allocating objects faster than the Garbage Collector can reclaim them, or because of memory leaks where stale objects remain referenced by global variables or circular references."

---

### Question 4: How does CPU caching (L1/L2/L3) relate to RAM and why does data locality matter?
**Model Answer:**  
"CPU registers and L1/L2/L3 caches sit physically on the CPU die and have latencies of 1 to 10 CPU cycles, whereas main memory (RAM) takes hundreds of cycles to respond.
When the CPU accesses memory, it doesn't just fetch a single byte; it fetches an entire **Cache Line** (usually 64 bytes).
Data locality matters because contiguous data structures (like arrays/lists) benefit from **spatial locality**—accessing index `0` brings neighboring elements into cache, making subsequent iterations near-instant. Disjoint pointer-based structures (like linked lists) suffer from cache misses because nodes are scattered across random heap locations."

---

### Question 5: When would you choose Multiprocessing over Multithreading in Python?
**Model Answer:**  
"In CPython, the **Global Interpreter Lock (GIL)** allows only one thread to execute Python bytecode at a time per process.
- For **I/O-bound tasks** (network calls, database queries, file reads), **Multithreading** or `asyncio` is ideal because threads release the GIL while waiting for the OS I/O to complete.
- For **CPU-bound tasks** (data processing, heavy mathematical computations, image transformation), multithreading will not utilize multiple CPU cores. In that case, **Multiprocessing** must be used so each process gets its own Python interpreter, memory space, and GIL, running truly in parallel across multiple CPU cores."
