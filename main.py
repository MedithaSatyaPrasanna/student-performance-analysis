import numpy as np
import matplotlib.pyplot as plt
# Load student data
data = np.genfromtxt(
    "data/students.csv",
    delimiter=",",
    skip_header=1,
    usecols=(0, 2, 3, 4, 5, 6)
)

# Extract columns
student_ids = data[:, 0]
marks = data[:, 1:4]
attendance = data[:, 4]
study_hours = data[:, 5]

# Calculate total and average marks
total_marks = np.sum(marks, axis=1)
average_marks = np.mean(marks, axis=1)

# Display analysis
print("\n===== STUDENT PERFORMANCE ANALYSIS =====")

print("\nTotal Students:", len(student_ids))
print("Class Average:", round(np.mean(average_marks), 2))
print("Highest Average:", round(np.max(average_marks), 2))
print("Lowest Average:", round(np.min(average_marks), 2))

print("\n===== SUBJECT-WISE ANALYSIS =====")

subjects = ["Maths", "Science", "English"]

for i in range(len(subjects)):
    print(subjects[i])
    print("Average:", round(np.mean(marks[:, i]), 2))
    print("Highest:", np.max(marks[:, i]))
    print("Lowest:", np.min(marks[:, i]))
    print()

print("===== ATTENDANCE ANALYSIS =====")
print("Average Attendance:", round(np.mean(attendance), 2), "%")

print("\n===== STUDY HOURS ANALYSIS =====")
print("Average Study Hours:", round(np.mean(study_hours), 2))
# Student Ranking

ranking = np.argsort(average_marks)[::-1]

print("\n===== STUDENT RANKING =====")

for i, index in enumerate(ranking):
    print(
        f"Rank {i + 1}: Student ID {int(student_ids[index])} "
        f"- Average: {average_marks[index]:.2f}"
    )
# Student Performance Classification

print("\n===== PERFORMANCE CLASSIFICATION =====")

for i in range(len(student_ids)):

    if average_marks[i] >= 85:
        category = "Excellent"

    elif average_marks[i] >= 70:
        category = "Good"

    elif average_marks[i] >= 50:
        category = "Average"

    else:
        category = "Needs Improvement"

    print(
        f"Student ID: {int(student_ids[i])} "
        f"| Average: {average_marks[i]:.2f} "
        f"| Category: {category}"
    )
# NumPy Vectorized Performance Classification

categories = np.where(
    average_marks >= 85, "Excellent",
    np.where(
        average_marks >= 70, "Good",
        np.where(
            average_marks >= 50, "Average",
            "Needs Improvement"
        )
    )
)

print("\n===== NUMPY PERFORMANCE CLASSIFICATION =====")

for i in range(len(student_ids)):
    print(student_ids[i], "-", categories[i])
# Students Requiring Academic Attention

at_risk = np.where(
    (average_marks < 50) | (attendance < 75)
)[0]

print("\n===== STUDENTS REQUIRING ATTENTION =====")

for index in at_risk:
    print(
        f"Student ID: {int(student_ids[index])} "
        f"| Average: {average_marks[index]:.2f} "
        f"| Attendance: {attendance[index]}%"
    )
# Percentile Analysis

print("\n===== PERCENTILE ANALYSIS =====")

print("25th Percentile:", np.percentile(average_marks, 25))
print("50th Percentile:", np.percentile(average_marks, 50))
print("75th Percentile:", np.percentile(average_marks, 75))
# Subject-wise Average Marks Visualization

subject_averages = np.mean(marks, axis=0)

plt.bar(subjects, subject_averages, color="green")

plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.ylim(0, 100)
plt.grid(axis="y")

for i in range(len(subjects)):
    plt.text(
        i,
        subject_averages[i] + 1,
        round(subject_averages[i], 2),
        ha="center"
    )

plt.show()
# Performance Distribution Pie Chart

category_names = [
    "Excellent",
    "Good",
    "Average",
    "Needs Improvement"
]

category_counts = [
    np.sum(categories == "Excellent"),
    np.sum(categories == "Good"),
    np.sum(categories == "Average"),
    np.sum(categories == "Needs Improvement")
]

plt.pie(
    category_counts,
    labels=category_names,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Performance Distribution")

plt.show()
# Student Average Marks Visualization

plt.figure(figsize=(10, 5))

plt.bar(student_ids, average_marks, color="skyblue")

plt.title("Student-wise Average Marks")
plt.xlabel("Student ID")
plt.ylabel("Average Marks")

plt.ylim(0, 100)
plt.grid(axis="y")

for i in range(len(student_ids)):
    plt.text(
        student_ids[i],
        average_marks[i] + 1,
        round(average_marks[i], 2),
        ha="center"
    )

plt.show()
# Study Hours vs Average Marks Scatter Plot

plt.figure(figsize=(8, 5))

plt.scatter(
    study_hours,
    average_marks,
    color="blue",
    marker="o",
    s=100
)

plt.title("Study Hours vs Average Marks")
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")

plt.ylim(0, 100)
plt.grid()

plt.show()