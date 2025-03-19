import pandas as pd
import matplotlib.pyplot as plt
import ast

# Step 1: Load data from CSV file
df = pd.read_csv('airtable_data.csv')

# Function to clean the 'Contact Status' column
def clean_contact_status(status):
    try:
        # Convert string representation of list to actual list
        status_list = ast.literal_eval(status)
        if isinstance(status_list, list):
            # Return the first element if it's a list
            return status_list[0]
        return status
    except (ValueError, SyntaxError):
        # Return the original status if it's not a list
        return status

# Clean the 'Contact Status' column
df['Contact Status'] = df['Contact Status'].apply(clean_contact_status)

# Define the contact statuses of interest
statuses_of_interest = ['Graduate ', 'Open Yet Active', 'Enrolled', 'Withdraw - Complete', 'Did Not Start']

# Filter the data to include only the specified contact statuses
df_filtered = df[df['Contact Status'].isin(statuses_of_interest)].copy()

# Convert 'Enrollment Date' to datetime
df_filtered['Enrollment Date'] = pd.to_datetime(df_filtered['Enrollment Date'], errors='coerce')

# Drop rows with invalid 'Enrollment Date'
df_filtered = df_filtered.dropna(subset=['Enrollment Date'])

# Extract the year from 'Enrollment Date'
df_filtered['Year'] = df_filtered['Enrollment Date'].dt.year

# Group by 'Year' and 'Contact Status' and count the number of enrollments
grouped = df_filtered.groupby(['Year', 'Contact Status']).size().unstack(fill_value=0)

# Reindex the grouped data to ensure all contact statuses are represented
grouped = grouped.reindex(columns=statuses_of_interest, fill_value=0)

# Plotting the data
fig, ax = plt.subplots(figsize=(15, 8))

# Define the colors for each contact status
colors = plt.cm.tab20.colors[:len(statuses_of_interest)]

# Plot each year separately
years = grouped.index
bar_width = 0.15
positions = range(len(years))

for i, status in enumerate(statuses_of_interest):
    offsets = [p + i * bar_width for p in positions]
    bars = ax.bar(offsets, grouped[status], width=bar_width, color=colors[i], label=status)
    
    # Adding labels to the bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=10)

# Customize the plot
plt.title('Enrollment Variations by Contact Status Across Years')
plt.xlabel('Year')
plt.ylabel('Number of Enrollments')
plt.xticks([p + bar_width * 2 for p in positions], years, rotation=45)

# Adding legend
ax.legend(title='Contact Status')

plt.tight_layout()
plt.show()
