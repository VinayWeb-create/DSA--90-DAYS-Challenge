# Day 01: Mini Project — Student Placement & Record Manager CLI

## 🎯 Project Overview
Build a production-quality Command-Line Interface (CLI) application in Python that manages engineering placement records, persists them to local storage, performs data validation, handles runtime errors, and visualizes system memory allocation.

---

## 🛠️ Features to Implement
1. **Interactive Menu Loop:**
   - 1. Add New Student Record (Name, Roll No, Branch, Target CTC, Skills)
   - 2. View All Student Records (Formatted table)
   - 3. Search Student by Roll Number or Skill
   - 4. Calculate Placement Statistics (Average Target CTC, Highest Target CTC)
   - 5. System Memory & Process Diagnostics (View current process ID, thread count, and memory addresses)
   - 6. Exit & Save
2. **Persistent Storage:**
   - Automatically load and save data from/to `students_database.json`.
3. **Robust Error Handling:**
   - Validate numerical inputs (e.g. Target CTC must be positive float).
   - Guard against duplicate Roll Numbers.
   - Graceful file I/O recovery if file doesn't exist.
4. **Clean Code Architecture:**
   - Modular functions with type annotations.
   - Separation of Business Logic and Display Logic.

---

## 📂 Implementation File
The complete working code is available in:  
[`mini_project_student_cli.py`](mini_project_student_cli.py)

Run it with:
```bash
python mini_project_student_cli.py
```
