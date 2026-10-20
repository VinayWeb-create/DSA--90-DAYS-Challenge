# Day 01: Quick Revision Notes & Cheatsheet

---

## 📌 1. Execution Flow Formula
$$\text{Source Code (.py)} \xrightarrow{\text{Compilation}} \text{Bytecode (.pyc)} \xrightarrow{\text{CPython VM}} \text{Machine Code} \xrightarrow{\text{Loaded in RAM}} \text{CPU ALU Executed}$$

---

## 📌 2. Storage Hierarchy
1. **Registers:** 0.5 ns, directly inside CPU ALU.
2. **L1/L2/L3 Cache:** 1–10 ns, on-chip SRAM.
3. **RAM (Main Memory):** 10–60 ns, volatile DDR4/DDR5.
4. **SSD (NVMe):** 50–100 $\mu$s, non-volatile NAND flash.
5. **HDD:** 5–10 ms, rotating magnetic disk.

---

## 📌 3. Quick Comparison: Process vs. Thread
- **Process:** Isolated virtual address space, heavy creation, safe from other crashes (e.g., Chrome, VS Code).
- **Thread:** Shared heap, private stack, lightweight, requires locks for shared writes (e.g., download worker, UI renderer).

---

## 📌 4. Quick Comparison: Stack vs. Heap
- **Stack (LIFO):** Function call frames, primitive local pointers, auto cleanup upon return, fast, causes `StackOverflowError`.
- **Heap (Dynamic):** Objects, lists, dictionaries, dynamic memory, managed by Garbage Collector, causes `OutOfMemoryError`.

---

## 📌 5. Core Python Types
| Type | Mutability | Example | Description |
|---|---|---|---|
| `int` | Immutable | `x = 42` | Arbitrary precision integer |
| `float` | Immutable | `pi = 3.14159` | Double-precision IEEE 754 |
| `str` | Immutable | `name = "Vinay"` | Unicode string sequence |
| `bool` | Immutable | `active = True` | Boolean flag (subclass of int) |
| `list` | Mutable | `nums = [1, 2, 3]` | Dynamic array on heap |
| `dict` | Mutable | `user = {"id": 1}` | Hash map on heap |
| `tuple` | Immutable | `coords = (10, 20)` | Fixed-size sequence |
| `set` | Mutable | `tags = {"cs", "py"}` | Unique hash set |
