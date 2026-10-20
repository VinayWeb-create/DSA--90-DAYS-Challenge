"""
Day 01: Control Flow, Loops, and Functions Call Stack
"""

import math

def calculate_circle_area(radius: float) -> float:
    """Calculates area of a circle with input validation."""
    if radius < 0:
        raise ValueError("Radius cannot be negative!")
    return math.pi * (radius ** 2)

def evaluate_eligibility(age: int) -> str:
    """Evaluates voting and job placement eligibility."""
    if age >= 21:
        return "Eligible for ₹12 LPA Engineering Roles & Voting"
    elif age >= 18:
        return "Eligible for Voting & University Placement"
    else:
        return "Minor / In School"

def main():
    print("=" * 60)
    print("Day 01: Control Flow & Function Call Execution")
    print("=" * 60)

    # Decision Making
    candidate_age = 21
    print(f"Candidate Age {candidate_age}: {evaluate_eligibility(candidate_age)}")

    # For Loop
    print("\n--- For Loop (5 Days Progression) ---")
    for day in range(1, 6):
        print(f"Progressing through Day {day}")

    # While Loop
    print("\n--- While Loop (Countdown) ---")
    countdown = 5
    while countdown > 0:
        print(f"Countdown: {countdown}")
        countdown -= 1

    # Function call
    radius = 7.0
    area = calculate_circle_area(radius)
    print(f"\nCircle with radius {radius} has Area = {area:.2f}")

if __name__ == "__main__":
    main()
