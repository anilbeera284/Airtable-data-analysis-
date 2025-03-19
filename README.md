📊 Students Enrollment Data Analysis
Overview
This repository contains Python scripts for extracting, analyzing and visualizing student enrollment data sourced from Airtable. The analyses include trends over time, state-wise distributions, course-type breakdown and more aimed at providing insights for educational data monitoring and decision-making.

🧩 Features
✅ Airtable data extraction via API
📅 Enrollment trends over quarters and years
🌎 State-wise student distribution
🎯 Contact status variation across years
📚 Course-type enrollments (monthly for 2023–2024)
📊 Visualizations using Matplotlib

File Name and Description
1. airtable_data_extraction.py - Extracts data from Airtable and saves to airtable_data.csv
2. enrollment_quarters.py - Plots number of enrollments per quarter across years
3. state_distribution.py - Bar chart of student distribution by state
4. contact_status_variation.py - Shows enrollment variation by contact status over years
5. monthly_course_enrollments.py - Stacked bar chart of course-type enrollments (2023–2024)

🛠️ Technologies Used
   Python 3
   Pandas
   Matplotlib
   Airtable API
   Visual studio code(optional for running scripts interactively)
   
🚀 Getting Started
1. Clone the Repository
   git clone https://github.com/anilbeera284/enrollment-data-analysis.git
   cd enrollment-data-analysis
2. Install Dependencies
   pip install pandas matplotlib requests
3. Configure Airtable API
   Open airtable_data_extraction.py
   Replace 'YOUR_API_KEY' and 'YOUR_BASE_ID' with your actual Airtable credentials.
4. Run Scripts
   Each script can be executed individually:
   python airtable_data_extraction.py
   python enrollment_quarters.py
   python state_distribution.py
   python contact_status_variation.py
   python monthly_course_enrollments.py

📝 License
   This project is licensed under the MIT License. Feel free to use and modify.

🙌 Acknowledgements
    Airtable API for data access
   Pandas & Matplotlib for data analysis and visualization
