# Day 01: Computer Science Foundations (Theory)

> "A software engineer who doesn't understand memory is like a driver who doesn't understand the engine—they can steer, but when the car stalls on a highway at 100 km/h, they have no idea what went wrong."

---

## 1. How Computers Execute Programs

Every software application—from a simple `print("Hello World")` to complex backend microservices—must transition from human-readable text into physical electrical signals that a silicon chip can process.

### The Complete Execution Pipeline:
```
+------------------------+
| Source Code (.py)     |  (Human-readable text stored on SSD/HDD)
+------------------------+
            |
            v  [Interpreter / Compiler / CPython Virtual Machine]
+------------------------+
| Bytecode / Machine Code|  (Intermediate .pyc bytecode or direct binary)
+------------------------+
            |
            v  [OS Loader loads program into RAM]
+------------------------+
|       RAM (Memory)     |  (Instructions + Data stored in memory addresses)
+------------------------+
            |
            v  [Bus Transfer]
+------------------------+
|       CPU (Registers)  |  (Fetch -> Decode -> Execute cycle in ALU)
+------------------------+
```

### The CPU Instruction Cycle:
1. **Fetch:** The CPU's Program Counter (PC) holds the address in RAM of the next instruction. The instruction is fetched into the CPU Instruction Register.
2. **Decode:** The CPU Control Unit decodes what operation needs to be done (e.g., ADD, JUMP, STORE).
3. **Execute:** The Arithmetic Logic Unit (ALU) performs the computation and updates registers or memory.

**Real-World Analogy:**  
Think of a master chef cooking a recipe:
- The **SSD/HDD** is the bookshelf where recipe books are stored permanently.
- The **RAM** is the kitchen counter where the chef places only the ingredients and open recipe page currently in use.
- The **CPU** is the chef's hands and brain executing one recipe step at a time.

---

## 2. Hardware Triad: CPU, RAM, and Storage

| Component | Nature | Speed | Cost per GB | Purpose |
|---|---|---|---|---|
| **CPU** | Computational engine | Nanoseconds | Extremely High | Brain of the computer; executes instructions. |
| **RAM (Random Access Memory)** | Volatile (data lost when powered off) | ~10–50 Nanoseconds | Medium | Working memory holding active programs and OS. |
| **Storage (SSD / HDD)** | Non-volatile (permanent persistence) | Microseconds (SSD) to Milliseconds (HDD) | Low | Stores OS files, installed apps, documents, media. |

### Why can't CPU execute directly from SSD?
A standard SSD has access latency around 50–100 microseconds (0.0001 seconds), whereas CPU registers operate in ~0.5 nanoseconds. Executing directly from SSD would slow your computer down by a factor of **100,000x**. Therefore, the Operating System always loads active programs and data into RAM first!

---

## 3. Binary & Memory Addressing

Computers operate on transistors that are either **OFF (0)** or **ON (1)**.
- **1 Bit (Binary Digit):** Smallest unit of data (0 or 1).
- **1 Byte:** 8 bits ($2^8 = 256$ possible values, from `00000000` to `11111111`, decimal 0 to 255).
- **ASCII Encoding:** How characters become numbers and binary:
  - `'A'` = Decimal 65 = Binary `01000001`
  - `'a'` = Decimal 97 = Binary `01100001`
  - `'0'` = Decimal 48 = Binary `00110000`

---

## 4. Processes vs. Threads

This is one of the most frequently asked questions in product company interviews (Amazon, Microsoft, Razorpay, Swiggy).

```
+-----------------------------------------------------------+
| PROCESS (e.g. Chrome / Python App)                        |
|                                                           |
|  [Code Segment]     [Data Segment]     [Heap (Shared)]    |
|                                                           |
|   +------------------+  +------------------+              |
|   | Thread 1         |  | Thread 2         |              |
|   | Stack (LIFO)     |  | Stack (LIFO)     |              |
|   | Registers / PC   |  | Registers / PC   |              |
|   +------------------+  +------------------+              |
+-----------------------------------------------------------+
```

### Definitions:
* **Process:** An instance of a computer program being executed by the OS. It has its **own isolated memory space** (virtual memory). One process cannot corrupt or read another process's memory without OS-level Inter-Process Communication (IPC).
* **Thread:** The smallest unit of execution inside a process (often called a "lightweight process"). Multiple threads within the same process **share the same Heap memory, code segment, and file handles**, but each thread has its **own Stack and Program Counter**.

### Process vs. Thread Comparison Table:
| Feature | Process | Thread |
|---|---|---|
| **Definition** | An independent executing program | A concurrent worker inside a process |
| **Memory Isolation** | Completely isolated; OS protected | Shares heap memory with other threads in the process |
| **Creation Overhead** | Heavy (requires full virtual memory map) | Lightweight (only allocates stack & registers) |
| **Context Switching** | Expensive (flushes CPU cache, page tables) | Fast & cheap |
| **Failure Impact** | If one process crashes, others continue | If a thread crashes (segfault), entire process can die |
| **Communication** | IPC (Sockets, Pipes, Shared Memory) | Direct memory access (variables on the heap) |
| **Real-world Example** | Chrome browser, VS Code, Python script | Chrome Tab UI worker, Download worker, Video decoder |

---

## 5. Memory Layout: Stack vs. Heap

When the OS allocates RAM to a process, it divides it into distinct segments:

```
High Memory Address
+----------------------------------+
|          HEAP (Grows Downward)   |  <-- Dynamic memory, objects, lists, dicts
|          |                       |
|          v                       |
|                                  |
|          ^                       |
|          |                       |
|          STACK (Grows Upward)    |  <-- Function frames, local variables, return pointers
+----------------------------------+
Low Memory Address
```

### 1. The Stack (LIFO - Last In, First Out)
* **What lives here:** Function call stack frames, primitive local variables, function arguments, return memory addresses.
* **Management:** Fully automated by the CPU stack pointer. When a function is called, a frame is **pushed**. When the function returns, the frame is **popped**.
* **Speed:** Blazing fast (contiguous memory, already mapped in CPU cache).
* **Limitation:** Fixed size. If you call infinite recursive functions without a base case, you get a `StackOverflowError` (RecursionError in Python).

### 2. The Heap (Dynamic Memory)
* **What lives here:** Objects whose size isn't known at compile-time or that need to outlive the function that created them (e.g., Python lists, dictionaries, custom class instances).
* **Management:** Managed by language runtime / Garbage Collector (GC) in Python/Java, or manual (`malloc`/`free`) in C.
* **Speed:** Slower than stack because the allocator must search for free contiguous memory blocks, and pointers must be dereferenced.
* **Limitation:** Can lead to memory leaks or fragmentation if unreferenced objects are not cleaned up.

### Stack vs. Heap Comparison:
| Aspect | Stack Memory | Heap Memory |
|---|---|---|
| **Structure** | Strict LIFO (Stack of plates) | Hierarchical / Free-store pool (Warehouse) |
| **Speed** | Extremely Fast | Slower (requires pointer traversal) |
| **Lifetime** | Determined by function scope | Determined by object references & Garbage Collector |
| **Allocation** | Compile time / deterministic function entry | Runtime dynamic allocation |
| **Failure Mode** | Stack Overflow (Recursion limit) | Out Of Memory (OOM) |

---

## 6. Real-World Architectural Perspective: OneBridge Social

Why does all of this matter to building **OneBridge Social** or getting a **₹12 LPA** role?

1. **FastAPI Web Server:**
   - FastAPI / Uvicorn runs as a **Process**.
   - If configured with 4 workers, the OS runs 4 separate Python **Processes** to utilize all 4 CPU cores.
   - Inside each worker, asynchronous tasks or thread pools handle incoming HTTP requests concurrently.
2. **Memory Leak in Production:**
   - If you append user session objects to a global list in your backend without clearing them, they sit in the **Heap**.
   - Python's Garbage Collector cannot delete them because they are still referenced by the global variable.
   - Over 48 hours, RAM usage climbs from 200MB to 4GB until the Linux kernel kills your process with `Out of Memory (OOMKilled)`.
3. **Understanding the fundamentals lets you diagnose, optimize, and prevent these production crashes before they happen!**
