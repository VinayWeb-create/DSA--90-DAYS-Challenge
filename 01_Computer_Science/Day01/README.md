# 🧭 Day 01: Step-by-Step Execution Guide

> **Don't feel overwhelmed!** You do not need to read or open all files at once.  
> Follow this exact **5-Step Order (1 to 5)**. Once you finish step 5, your Day 01 is 100% complete.

---

## 🚦 Your Step-by-Step Order for Today

```
[Step 1: Read Theory]  --->  [Step 2: Run Code Demos]  --->  [Step 3: Solve Exercises]  --->  [Step 4: Mini Project & Interview]  --->  [Step 5: Review & Post]
     (20 mins)                     (15 mins)                        (30 mins)                          (30 mins)                           (10 mins)
```

---

### 🟢 STEP 1: Understand the Concepts (20 mins)
* Open and read: [**Theory.md**](Theory.md)  
  *(If you want a quick 5-minute visual summary first, look at [**Notes.md**](Notes.md) and your handwritten poster!)*
* **Focus on 3 main questions:**
  1. How does code go from SSD ➡️ RAM ➡️ CPU?
  2. What is the difference between a **Process** (isolated) and a **Thread** (shared)?
  3. What is the difference between **Stack** (fast, LIFO function frames) and **Heap** (objects, dynamic)?

---

### 🟡 STEP 2: Watch the Code Run (15 mins)
Open your terminal in VS Code and run the 5 demo scripts in [`code/`](code/):

```bash
cd "01_Computer_Science/Day01/code"

python 01_execution_and_types.py          # See variables and memory IDs
python 02_control_flow_and_functions.py    # See functions and loops
python 03_process_vs_threads.py           # See 2 concurrent threads running
python 04_stack_vs_heap_memory.py         # See why lists have different heap IDs
python 05_file_handling.py                # See data saved to disk
```
*(Reference: [Examples.md](Examples.md) explains what each script is doing).*

---

### 🔵 STEP 3: Hands-On Practice (30 mins)
* Open: [**Exercises.md**](Exercises.md)
* Try solving the 10 questions from your handwritten notes.
* If you get stuck on any question, check: [`code/exercises_solutions.py`](code/exercises_solutions.py)
* Test the solutions anytime:
  ```bash
  python exercises_solutions.py
  ```

---

### 🟣 STEP 4: Mini Project & Interview Prep (30 mins)
* **Mini Project:** Open and run the interactive CLI:
  ```bash
  python mini_project_student_cli.py
  ```
  *(Reference: [Mini_Project.md](Mini_Project.md))*
* **Interview Drill:** Read the 5 interview questions in [**Interview.md**](Interview.md).  
  Say the answers out loud in English as if a Google or Amazon interviewer is asking you!

---

### 🔴 STEP 5: Daily Checklist, Reflection & Social Proof (10 mins)
* Open [**Checklist.md**](Checklist.md) and check off what you completed today.
* Fill in 3 quick lines in [**Reflection.md**](Reflection.md) (What you learned, what was cool).
* Open [**Instagram_Kit.md**](Instagram_Kit.md):
  - Copy the ready-made caption.
  - Upload your handwritten poster or carousel images to **@codvinu.ai**.
* **Commit your code to GitHub:**
  ```bash
  git add .
  git commit -m "Day 01 Completed: Computer Science Foundations & Student CLI"
  git push origin main
  ```

---

## 📁 File Reference Map
```
01_Computer_Science/Day01/
├── README.md               <-- YOU ARE HERE (Start and follow steps 1 to 5)
├── Theory.md               <-- Step 1: Read concepts
├── Notes.md                <-- Step 1 (Alternative): Quick cheatsheet
├── Examples.md             <-- Step 2: Code explanations
├── Exercises.md            <-- Step 3: 10 practice problems
├── Assignment.md           <-- Optional: Extra challenge problems
├── Mini_Project.md         <-- Step 4: Project details
├── Interview.md            <-- Step 4: Top 5 interview Q&A
├── Checklist.md            <-- Step 5: Mark completed items
├── Reflection.md           <-- Step 5: Daily journal
├── Instagram_Kit.md        <-- Step 5: Ready-to-copy social post
└── code/                   <-- All runnable Python scripts (.py)
```
