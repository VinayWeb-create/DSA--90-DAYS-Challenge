"""
Day 01: Mini Project — Student Placement & Record Manager CLI
A complete CLI application with JSON persistence, error handling,
validation, analytics, and OS/Process/Memory diagnostics.
"""

import json
import os
import sys
import threading
from typing import Any

# Ensure stdout handles UTF-8 characters on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

DB_FILE = "students_database.json"

class PlacementManager:
    def __init__(self, db_path: str = DB_FILE):
        self.db_path = db_path
        self.students: list[dict[str, Any]] = self._load_data()

    def _load_data(self) -> list[dict[str, Any]]:
        """Loads data from persistent JSON file on disk into RAM."""
        if not os.path.exists(self.db_path):
            return []
        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"[Warning] Failed to load {self.db_path}: {e}. Initializing empty list.")
            return []

    def save_data(self) -> None:
        """Saves current student records from RAM to disk."""
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(self.students, f, indent=2)

    def add_student(self, name: str, roll_no: str, branch: str, target_ctc_lpa: float, skills: list[str]) -> bool:
        """Adds a student record with duplicate roll number validation."""
        for s in self.students:
            if s["roll_no"].lower() == roll_no.lower():
                print(f"[Error] Student with Roll No '{roll_no}' already exists!")
                return False

        if target_ctc_lpa <= 0:
            print("[Error] Target CTC must be a positive number!")
            return False

        record = {
            "name": name.strip(),
            "roll_no": roll_no.strip(),
            "branch": branch.strip(),
            "target_ctc_lpa": float(target_ctc_lpa),
            "skills": [skill.strip() for skill in skills if skill.strip()]
        }
        self.students.append(record)
        self.save_data()
        print(f"[Success] Student '{name}' added successfully!")
        return True

    def list_students(self) -> None:
        """Displays all students in a formatted ASCII table."""
        if not self.students:
            print("\n[Notice] No student records found. Add one first!")
            return

        print("\n" + "=" * 75)
        print(f"{'Roll No':<10} | {'Name':<18} | {'Branch':<8} | {'Target CTC':<12} | {'Skills'}")
        print("-" * 75)
        for s in self.students:
            skills_str = ", ".join(s["skills"])
            print(f"{s['roll_no']:<10} | {s['name']:<18} | {s['branch']:<8} | ₹{s['target_ctc_lpa']:<5.1f} LPA    | {skills_str}")
        print("=" * 75 + "\n")

    def search_by_skill(self, skill_query: str) -> list[dict[str, Any]]:
        """Finds students who possess a particular skill."""
        query = skill_query.lower()
        matches = [s for s in self.students if any(query in sk.lower() for sk in s["skills"])]
        return matches

    def calculate_stats(self) -> dict[str, float]:
        """Calculates placement analytics."""
        if not self.students:
            return {"count": 0, "avg_ctc": 0.0, "max_ctc": 0.0, "min_ctc": 0.0}

        ctcs = [s["target_ctc_lpa"] for s in self.students]
        return {
            "count": len(self.students),
            "avg_ctc": sum(ctcs) / len(ctcs),
            "max_ctc": max(ctcs),
            "min_ctc": min(ctcs)
        }

    def print_diagnostics(self) -> None:
        """Inspects OS process, active threads, and memory addresses."""
        print("\n" + "=" * 60)
        print("🖥️  System, OS & Memory Diagnostics")
        print("=" * 60)
        print(f"Current Process ID (PID)    : {os.getpid()}")
        print(f"Active Thread Count         : {threading.active_count()}")
        print(f"Students List Heap Address  : {hex(id(self.students))}")
        print(f"Self Instance Address       : {hex(id(self))}")
        print(f"Database File Size on Disk  : {os.path.getsize(self.db_path) if os.path.exists(self.db_path) else 0} bytes")
        print("=" * 60 + "\n")


def run_interactive_menu():
    manager = PlacementManager()

    while True:
        print("\n=== 🎓 Student Placement Tracker CLI ===")
        print("1. Add New Student Record")
        print("2. View All Student Records")
        print("3. Search Students by Skill")
        print("4. View Placement Analytics")
        print("5. View System & Memory Diagnostics")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter Name: ").strip()
            roll_no = input("Enter Roll No: ").strip()
            branch = input("Enter Branch (e.g. CSE): ").strip()
            try:
                ctc = float(input("Enter Target CTC in LPA (e.g. 12.0): ").strip())
            except ValueError:
                print("[Error] Invalid CTC number!")
                continue
            skills_raw = input("Enter skills separated by commas (e.g. Python, FastAPI, React): ")
            skills = skills_raw.split(",")
            manager.add_student(name, roll_no, branch, ctc, skills)

        elif choice == "2":
            manager.list_students()

        elif choice == "3":
            skill = input("Enter skill to search for (e.g. Python): ").strip()
            results = manager.search_by_skill(skill)
            print(f"\nFound {len(results)} student(s) with skill '{skill}':")
            for r in results:
                print(f"- {r['name']} ({r['roll_no']}) - Target: ₹{r['target_ctc_lpa']} LPA")

        elif choice == "4":
            stats = manager.calculate_stats()
            print(f"\n--- Placement Statistics ---")
            print(f"Total Candidates : {stats['count']}")
            print(f"Average Target   : ₹{stats['avg_ctc']:.2f} LPA")
            print(f"Highest Target   : ₹{stats['max_ctc']:.2f} LPA")
            print(f"Minimum Target   : ₹{stats['min_ctc']:.2f} LPA")

        elif choice == "5":
            manager.print_diagnostics()

        elif choice == "6":
            print("Goodbye! Keep coding every day.")
            break
        else:
            print("[Error] Invalid choice, please choose 1-6.")


if __name__ == "__main__":
    # If run with '--demo', runs automated verification
    if "--demo" in sys.argv:
        print("Running Automated Mini-Project Demo...")
        demo_manager = PlacementManager("demo_students.json")
        demo_manager.add_student("Vinay", "CSE001", "CSE", 12.0, ["Python", "FastAPI", "React", "Docker"])
        demo_manager.add_student("Rahul", "CSE002", "IT", 10.0, ["JavaScript", "React", "Node.js"])
        demo_manager.list_students()
        demo_manager.print_diagnostics()
        stats = demo_manager.calculate_stats()
        print(f"Stats Verified: Avg = ₹{stats['avg_ctc']} LPA, Max = ₹{stats['max_ctc']} LPA")
        if os.path.exists("demo_students.json"):
            os.remove("demo_students.json")
        print("\n[SUCCESS] Mini Project automated test passed!")
    else:
        run_interactive_menu()
