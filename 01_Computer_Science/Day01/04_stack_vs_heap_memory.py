"""
Day 01: Stack vs. Heap Memory Visualization
Demonstrating how references, primitive interning, and heap objects work.
"""

import sys

def stack_frame_demo(a: int, b: int) -> int:
    """
    Every time this function is called, a new Stack Frame is allocated.
    Local pointers a, b, and local_sum exist in this stack frame.
    """
    local_sum = a + b
    print(f"  [Inside stack_frame_demo] local_sum={local_sum}, Address={hex(id(local_sum))}")
    return local_sum

def main():
    print("=" * 60)
    print("Day 01: Stack vs. Heap Memory Deep Dive")
    print("=" * 60)

    # 1. Integer Interning (Small integers -5 to 256 share the same heap object)
    x = 100
    y = 100
    print(f"x = 100 (Address: {hex(id(x))})")
    print(f"y = 100 (Address: {hex(id(y))})")
    print(f"Are memory addresses identical? {id(x) == id(y)} (Python caches small integers!)\n")

    # 2. Heap Mutable Objects (Lists are distinct objects in Heap even with same values)
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(f"list1 = [1, 2, 3] (Address: {hex(id(list1))}, Size: {sys.getsizeof(list1)} bytes)")
    print(f"list2 = [1, 2, 3] (Address: {hex(id(list2))}, Size: {sys.getsizeof(list2)} bytes)")
    print(f"Are list memory addresses identical? {id(list1) == id(list2)} (Distinct heap allocations!)\n")

    # 3. Stack Frame Execution
    print("Calling stack_frame_demo(10, 20):")
    result = stack_frame_demo(10, 20)
    print(f"Returned result: {result}")

if __name__ == "__main__":
    main()
