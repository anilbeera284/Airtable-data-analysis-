import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data from CSV file
df = pd.read_csv('airtable_data.csv')

# Convert 'Enrollment Date' to datetime
df['Enrollment Date'] = pd.to_datetime(df['Enrollment Date'], errors='coerce')

# Drop rows with invalid 'Enrollment Date'
df = df.dropna(subset=['Enrollment Date'])

# Extract the year and quarter from 'Enrollment Date'
df['Year'] = df['Enrollment Date'].dt.year

# Map months to quarters
def month_to_quarter(month):
    if month in [1, 2, 3]:
        return 'Q1'
    elif month in [4, 5, 6]:
        return 'Q2'
    elif month in [7, 8, 9]:
        return 'Q3'
    else:
        return 'Q4'

df['Quarter'] = df['Enrollment Date'].dt.month.apply(month_to_quarter)

# Group by 'Year' and 'Quarter' and count the number of enrollments
grouped = df.groupby(['Year', 'Quarter']).size().unstack(fill_value=0)

# Calculate total enrollments for each quarter
totals = grouped.sum(axis=0)

# Plotting the data
fig, ax = plt.subplots(figsize=(15, 8))

# Define the colors for each quarter
colors = ['blue', 'green', 'orange', 'red']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
bar_width = 0.2
n_quarters = len(quarters)

# Get unique years
years = grouped.index
positions = range(len(years))

# Plot each quarter separately
for i, quarter in enumerate(quarters):
    offsets = [p + i * bar_width for p in positions]
    bars = ax.bar(offsets, grouped[quarter], width=bar_width, color=colors[i], label=f'{quarter} (Total: {totals[quarter]})')
    
    # Adding labels to the bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=10)

# Customize the plot
plt.title('Enrollment Over Time by Quarter')
plt.xlabel('Year')
plt.ylabel('Number of Enrollments')
plt.xticks([p + bar_width * (n_quarters / 2) for p in positions], years, rotation=45)

# Adding legend
ax.legend(title='Quarter')

plt.tight_layout()
plt.show()
