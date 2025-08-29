# Student_Data_Analysis

Project Overview

This project demonstrates data analysis and visualization using Python with the libraries Pandas, NumPy, Matplotlib, and Seaborn.

The dataset student_dataset_large.csv contains information about students, including:

Student_ID

Name

Age

Gender

Department

Maths, Science, English marks

Attendance

The main objectives of this project are:

Explore student data and perform basic statistical analysis.

Clean and preprocess the dataset.

Generate insights like top-performing students, department-wise performance, attendance trends, and gender distribution.

Visualize data using bar charts, histograms, scatter plots, and pie charts.

Dataset

The dataset contains the following columns:

Column	Description
Student_ID	Unique ID of the student
Name	Student Name
Age	Student Age
Gender	Male/Female
Department	Department Name (CSE, EEE, Mech, MBA)
Maths	Marks in Maths
Science	Marks in Science
English	Marks in English
Attendance	Attendance percentage

Sample of the dataset:

   Student_ID   Name   Age Gender Department  Maths  Science  English  Attendance
0          101  John   20   Male       CSE     85       90       88         95
1          102  Jane   21 Female       EEE     78       85       80         90
2          103  Mike   22   Male      Mech     92       88       85         98

Key Steps in the Project

Data Import & Exploration

Load CSV using pd.read_csv().

Check first rows (head()), last rows (tail()), shape, info, and summary statistics (describe()).

Count students per department.

Statistical Analysis

Mean, median, mode of Maths, Science, English, and Attendance.

Identify top 5 students with highest total marks.

Sort and filter students based on attendance, marks, or department.

Data Cleaning

Handle missing values by filling with mean.

Correct inconsistent department names (Mechanical → Mech, Eee → EEE).

Rename columns for clarity (Maths → Mathematics).

Feature Engineering

Create Total_Marks column.

Assign Grade based on Total_Marks (A/B/C).

Map Department to Stream (Tech/Core/Management).

Data Visualization

Bar chart: Average Maths marks per department.

Histogram: Age distribution of students.

Scatter plot: Attendance vs Total Marks.

Pie chart: Gender distribution.

Required Libraries
pip install pandas numpy matplotlib seaborn

Sample Visuals
1. Department-wise Average Maths Marks

2. Age Distribution

3. Attendance vs Total Marks

4. Gender Distribution

Note: Replace the above URLs with actual images saved in the repo folder /images/.

How to Run the Project

Clone the repository:

git clone https://github.com/your-username/student-data-analysis.git


Navigate to the project folder:

cd student-data-analysis


Run the Python script:

python student_analysis.py


All visualizations will be displayed and can be saved locally.

Conclusion

This project demonstrates data exploration, cleaning, feature engineering, and visualization on student data. Insights like top-performing students, department-wise performance, attendance trends, and gender distribution can help teachers and management make data-driven decisions.
