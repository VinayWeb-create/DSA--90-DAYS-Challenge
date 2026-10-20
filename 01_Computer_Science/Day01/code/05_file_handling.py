"""
Day 01: File Handling & Persistence
Transferring data between volatile RAM and persistent storage (SSD/HDD).
"""

import os

def main():
    print("=" * 60)
    print("Day 01: File Handling & Storage Persistence")
    print("=" * 60)

    filename = "day01_demo_output.txt"

    # 1. Writing data to file
    print(f"Writing to '{filename}'...")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Line 1: 90-Day Challenge Day 01\n")
        f.write("Line 2: Computer Science Foundations\n")
        f.write("Line 3: Target: ₹12 LPA Software Engineer Offer\n")

    # 2. Appending data
    print("Appending new record...")
    with open(filename, "a", encoding="utf-8") as f:
        f.write("Line 4: Author: Vinay (@codvinu.ai)\n")

    # 3. Reading data back into RAM
    print("\nReading data from file:")
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)

    # 4. Clean up file info
    size = os.path.getsize(filename)
    print(f"File size on disk: {size} bytes")

if __name__ == "__main__":
    main()
