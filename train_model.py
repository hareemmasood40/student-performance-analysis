import pandas as pd

df = pd.read_csv("03_projects/student_performance_project/student_scores.csv")

df["average_score"] = (df["math_score"] + df["reading_score"] + df["writing_score"]) / 3
threshold = df["average_score"].median()
print("Threshold:", threshold)
df["result"] = df["average_score"].apply(lambda x: "Pass" if x >= threshold else "Fail")


print(df[["student_id", "average_score", "result"]].head(10))
print(df["result"].value_counts())
features = df[["gender", "parental_education", "test_prep_course", "study_hours_per_week"]]
features_encoded = pd.get_dummies(features)

print(features_encoded.head())
print(features_encoded.columns.tolist())
from sklearn.model_selection import train_test_split

X = features_encoded
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42, max_depth=3)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)
new_student = pd.DataFrame({
    "study_hours_per_week": [10],
    "gender_Female": [True],
    "gender_Male": [False],
    "parental_education_Associate's Degree": [False],
    "parental_education_Bachelor's Degree": [True],
    "parental_education_High School": [False],
    "parental_education_Master's Degree": [False],
    "test_prep_course_Completed": [True],
    "test_prep_course_No": [False],
})

prediction = model.predict(new_student)
print("Prediction for new student:", prediction)
