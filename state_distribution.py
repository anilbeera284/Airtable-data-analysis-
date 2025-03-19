import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data from CSV file
df = pd.read_csv('airtable_data.csv')

# Step 2: Calculate the distribution of students by state
state_distribution = df['State'].value_counts()

# Step 3: Plotting the distribution
fig, ax = plt.subplots(figsize=(10, 6))
state_distribution.plot(kind='bar', ax=ax)
plt.title('Enrollment by State')
plt.xlabel('State')
plt.ylabel('Number of Students')
plt.xticks(rotation=45, fontsize=8)

# Adding labels on top of the bars
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=10)

plt.tight_layout()
plt.show()
