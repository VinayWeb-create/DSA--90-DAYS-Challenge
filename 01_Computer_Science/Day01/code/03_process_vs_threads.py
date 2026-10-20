"""
Day 01: Process vs. Thread Demonstration
Visualizing concurrent execution inside the same Python process.
"""

import threading
import time
import os

def worker(worker_name: str, task_count: int, delay: float):
    process_id = os.getpid()
    thread_id = threading.get_ident()
    print(f"[{worker_name}] Starting on Process ID: {process_id}, Thread ID: {thread_id}")

    for step in range(1, task_count + 1):
        time.sleep(delay)
        print(f"[{worker_name}] Completed task {step}/{task_count}")

    print(f"[{worker_name}] Finished successfully!")

def main():
    print("=" * 60)
    print("Day 01: Process and Concurrent Threads Execution")
    print(f"Main Process ID: {os.getpid()}")
    print("=" * 60)

    # Creating two worker threads inside the current process
    t1 = threading.Thread(target=worker, args=("Worker-Thread-1", 3, 0.4))
    t2 = threading.Thread(target=worker, args=("Worker-Thread-2", 3, 0.6))

    # Both threads start concurrently
    t1.start()
    t2.start()

    # Main thread waits for both workers to complete
    t1.join()
    t2.join()

    print("\n[Main Thread] All background workers have finished.")

if __name__ == "__main__":
    main()
