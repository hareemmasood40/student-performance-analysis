"""One-off script to generate a realistic practice dataset for the student performance project."""
import random
import csv

random.seed(42)

genders = ["Male", "Female"]
parental_education = ["High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree"]

rows = []
for i in range(1, 61):
    gender = random.choice(genders)
    parent_ed = random.choice(parental_education)
    test_prep = random.choice(["Completed", "No"])
    study_hours = round(random.uniform(1, 15), 1)

    base = 55
    base += study_hours * 1.8
    base += 8 if test_prep == "Completed" else 0
    base += {"High School": 0, "Associate's Degree": 3, "Bachelor's Degree": 6, "Master's Degree": 9}[parent_ed]

    math = max(35, min(100, round(base + random.uniform(-10, 10))))
    reading = max(35, min(100, round(base + random.uniform(-8, 12))))
    writing = max(35, min(100, round(base + random.uniform(-8, 12))))

    rows.append([i, gender, parent_ed, test_prep, study_hours, math, reading, writing])

with open("03_projects/student_performance_project/student_scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["student_id", "gender", "parental_education", "test_prep_course",
                      "study_hours_per_week", "math_score", "reading_score", "writing_score"])
    writer.writerows(rows)

print("Generated 60 rows")
