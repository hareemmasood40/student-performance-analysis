import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("03_projects/student_performance_project/student_scores.csv")

avg_scores = df.groupby("test_prep_course")[["math_score", "reading_score", "writing_score"]].mean()

avg_scores.plot(kind="bar")
plt.title("Average Scores by Test Prep Course Completion")
plt.ylabel("Average Score")
plt.xlabel("Test Prep Course")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("03_projects/student_performance_project/test_prep_chart.png")
plt.show()
