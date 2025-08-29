# importing libraries -
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# loading dataset -

df = pd.read_csv("student_dataset_large.csv")
print(df.head())
print(df.tail())

# basic exploration -
print(df.shape)
print(df.info())
print(df.describe())


# student per department -
student_counts = df['Department'].value_counts()
print(student_counts)

# statistics -

# mean, median, mode of maths -
print(df["Maths"].mean())
print(df["Maths"].median())
print(df["Maths"].mode())

#mean, median,mode of Science -
print(df["Science"].mean())
print(df["Science"].median())
print(df["Science"].mode())


#mean, median, mode of English -
print(df["English"].mean())
print(df["English"].median())
print(df["English"].mode())


# mean,median,mode of Attendance -
print(df["Attendance"].mean())
print(df["Attendance"].median())
print(df["Attendance"].mode())

# finding top 5 student with highest total marks -

# creating a new column of total marks -
df['Total_Marks'] = df[['Maths', 'Science', 'English']].sum(axis = 1,skipna = True)  # using Axis = 1 bcoz we need column wise addition

# using nlargest() function to return top n rows -
top5_students = df.nlargest(5, 'Total_Marks')[
    ['Student_ID', 'Name', 'Department', 'Maths', 'Science', 'English', 'Total_Marks']
]

print("Top 5 Students with Highest Total Marks:\n")
print(top5_students)

# sorting and filtering -

# Sorting student by attendance -
df_sorted = df.sort_values(by="Attendance")
print(df_sorted)

# filtering student from CSE department with maths > 80 -
fill2 = df[(df["Department"] == "CSE") & (df["Maths"] > 80 )]
print(fill2)

# data Cleaning -

# identify and handle NAN values -
print(df.isna().sum())

# filling  duplicate records -
df['Maths'].fillna(df['Attendance'].mean(), inplace=True)
df['Science'].fillna(df['Science'].mean(), inplace=True)
df['English'].fillna(df['English'].mean(), inplace=True)

# correcting inconsistent department names -
df["Department"] = np.where(df["Department"] == "Mechanical", "Mech",
                    np.where(df["Department"] == "Eee", "EEE", df["Department"]))    # last me use krne ka matalb he jo reh jata he EEE or mech ke baad wo same rhe df["Department"]

print(df[["Student_ID","Name","Age","Gender","Department"]].head())


# renaming column name of maths as mathematics -
df.rename(columns = {"Maths" : "Mathematics"}, inplace = True)
print(df.head())

# feature engineering -


# adding a new column "grade" based on total -
df["Grade"] = np.where(df["Total_Marks"] >= 240, "A",
                             np.where(df["Total_Marks"] <= 180, "B","C"))
print(df[["Student_ID","Name","Age","Gender","Science","English","Attendance","Total_Marks","Grade"]].head())

# creating a stream column using mapping -
df["Stream"] = df["Department"].map({"CSE" : "Tech", "EEE" : "Tech", "Mech" : "core", "MBA" : "Management"})
print(df.head())

# visualization -

# Average maths marks per Department -
avg_math_marks_dept = df.groupby("Department")["Mathematics"].mean()

# Barplot of average maths marks per department  -
plt.bar(avg_math_marks_dept.index, avg_math_marks_dept.values, color="orange")
plt.title("average maths marks per department")
plt.xlabel("Department")
plt.ylabel("Average maths marks")
plt.show()

# histogram of age distribution -
plt.hist(df["Age"], bins=10, color="lightgreen", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Student")
plt.show()

# Scatterplot of Attendance vs Total_marks -
plt.scatter(df["Attendance"], df["Total_Marks"], color="blue", alpha=0.6)
plt.title("Attendance vs Total Marks")
plt.xlabel("Attendance")
plt.ylabel("Total Marks")
plt.show()

# pie chart of  Gender distribution
gender_counts = df["Gender"].value_counts()  # gender counts krega

plt.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Gender Distribution")
plt.show()