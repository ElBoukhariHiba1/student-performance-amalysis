import pandas as pd

data = pd.read_csv("students.csv")

print(data)
data["Average"] = data[["Math", "Physics", "Programming", "English"]].mean(axis=1)

print("\nStudent Averages:")
print(data[["Name", "Average"]])
top_student = data.loc[data["Average"].idxmax()]
low_student = data.loc[data["Average"].idxmin()]

print("\nBest Student:")
print(top_student["Name"], "-", top_student["Average"])

print("\nLowest Average:")
print(low_student["Name"], "-", low_student["Average"])
subject_averages = data[["Math", "Physics", "Programming", "English"]].mean()

print("\nAverage by Subject:")
print(subject_averages)

best_subject = subject_averages.idxmax()
worst_subject = subject_averages.idxmin()

print("\nBest Subject:", best_subject)
print("Lowest Subject:", worst_subject)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.bar(data["Name"], data["Average"])

plt.title("Student Average Scores")
plt.xlabel("Students")
plt.ylabel("Average Score")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("student-average-scores.png")
plt.show()
plt.figure(figsize=(8, 5))

subject_averages.plot(kind="bar")

plt.title("Average Score by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Score")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("subject_averages.png")

report = f"""
========== STUDENT PERFORMANCE REPORT ==========

Number of Students: {len(data)}

Class Average: {data["Average"].mean():.2f}

Highest Average: {data["Average"].max():.2f}

Lowest Average: {data["Average"].min():.2f}

Best Student: {top_student["Name"]}

Lowest Student: {low_student["Name"]}

Best Subject: {best_subject}

Lowest Subject: {worst_subject}

================================================
"""

print(report)

with open("report.txt", "w") as file:
    file.write(report)

print("Report saved successfully!")
plt.show()
