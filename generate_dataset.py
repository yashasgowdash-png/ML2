import numpy as np
import pandas as pd

np.random.seed(42)

n = 5000

data = {
    "Student_ID": np.arange(1, n + 1),
    "Age": np.random.randint(18, 25, n),
    "Study_Hours": np.round(np.random.uniform(1, 10, n), 1),
    "Attendance": np.round(np.random.uniform(60, 100, n), 1),
    "Assignments": np.random.randint(3, 11, n),
    "Marks": np.round(np.random.uniform(40, 100, n), 1)
}

df = pd.DataFrame(data)

df.loc[np.random.choice(n, 100, replace=False), "Study_Hours"] = np.nan
df.loc[np.random.choice(n, 80, replace=False), "Attendance"] = np.nan
df.loc[np.random.choice(n, 70, replace=False), "Assignments"] = np.nan
df.loc[np.random.choice(n, 50, replace=False), "Marks"] = np.nan

df.to_csv("student_data.csv", index=False)

print("Dataset created successfully")
print(df.head())
print("Rows:", len(df))