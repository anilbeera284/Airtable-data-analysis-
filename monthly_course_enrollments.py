import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data from CSV file
df = pd.read_csv('airtable_data.csv')

# Step 2: Convert 'Enrollment Date' to datetime format
df['Enrollment Date'] = pd.to_datetime(df['Enrollment Date'])

# Step 3: Filter data for the years 2023 and 2024 and create a copy of the filtered data
df_filtered = df[(df['Enrollment Date'].dt.year == 2023) | (df['Enrollment Date'].dt.year == 2024)].copy()

# Step 4: Extract month and year from the 'Enrollment Date'
df_filtered['Month-Year'] = df_filtered['Enrollment Date'].dt.to_period('M')

# Step 5: Group by month-year and course type and count the number of enrollments
monthly_course_enrollments = df_filtered.groupby(['Month-Year', 'Expected Highest Level of Training']).size().unstack().fillna(0)

# Step 6: Plotting the monthly enrollments by course
fig, ax = plt.subplots(figsize=(15, 8))
monthly_course_enrollments.plot(kind='bar', stacked=True, ax=ax)
plt.title('Monthly Enrollments by Course Type for 2023-2024')
plt.xlabel('Month-Year')
plt.ylabel('Number of Enrollments')
plt.xticks(rotation=45)

# Customize x-axis to remove zero labels
x_labels = [label.get_text() for label in ax.get_xticklabels()]
new_labels = [label if label != '0' else '' for label in x_labels]
ax.set_xticklabels(new_labels)

# Adding labels to the bars
for container in ax.containers:
    ax.bar_label(container, label_type='center', fontsize=10)

plt.legend(title='Course Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
