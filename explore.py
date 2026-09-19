import pandas as pd

df = pd.read_csv("03_projects/student_performance_project/student_scores.csv")

print(df.head())
print(df.shape)
print(df.describe())
print(df.groupby("test_prep_course")[["math_score", "reading_score", "writing_score"]].mean())
print(df.groupby("parental_education")[["math_score", "reading_score", "writing_score"]].mean().sort_values("math_score"))
print(df[["study_hours_per_week", "math_score", "reading_score", "writing_score"]].corr())
