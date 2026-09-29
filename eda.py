import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

print(df.head())
print(df.shape)
print(df.info())

print(df.isnull().sum())

df = df.dropna()

print(df.describe())

numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    plt.figure(figsize=(8, 5))
    plt.hist(df[column], bins=20)
    plt.title("Distribution of " + column)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance"], df["Marks"])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["Assignments"], df["Marks"])
plt.title("Assignments vs Marks")
plt.xlabel("Assignments")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(df["Student_ID"], df["Marks"])
plt.title("Marks by Student")
plt.xlabel("Student ID")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(
    ["Study Hours", "Attendance", "Assignments", "Marks"],
    [
        df["Study_Hours"].mean(),
        df["Attendance"].mean(),
        df["Assignments"].mean(),
        df["Marks"].mean()
    ]
)
plt.title("Average Student Performance")
plt.ylabel("Average Value")
plt.show()

correlation = df[numeric_columns].corr()

print(correlation)

plt.figure(figsize=(10, 7))
plt.imshow(correlation, cmap="coolwarm", interpolation="none")
plt.colorbar()
plt.xticks(range(len(numeric_columns)), numeric_columns, rotation=45)
plt.yticks(range(len(numeric_columns)), numeric_columns)
plt.title("Correlation Matrix")
plt.show()