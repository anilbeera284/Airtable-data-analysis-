from airtable import Airtable
import pandas as pd
import requests

# Your Airtable API token
AIRTABLE_API_TOKEN = 'patVgol0dmzPWMLa3.31616dd2dc4ca5743c670fcef92fd060453d20ac0e0707ab3386070dcc8313de'  # Replace with the new token
# Your Airtable Base ID
BASE_ID = 'app0lYmNo01Eelrpd'
# The table name containing the view
TABLE_NAME = 'Students'  # Table name
# The specific view you want to fetch records from
VIEW_NAME = '2023 Spreadsheet Analytics View'

print("Starting script...")

# Initialize Airtable connection
try:
    airtable = Airtable(BASE_ID, TABLE_NAME, api_key=AIRTABLE_API_TOKEN)
    print("Airtable connection initialized...")
    
    # Fetch all records from the specific view
    print(f"Fetching records from view: {VIEW_NAME}...")
    records = airtable.get_all(view=VIEW_NAME)
    print(f"Records fetched: {len(records)}")

    # Extract fields from records
    data = [record['fields'] for record in records]
    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data)
    # Display the DataFrame
    print(df)
    # Optionally, save the DataFrame to a CSV file
    df.to_csv('airtable_data.csv', index=False)

except requests.exceptions.HTTPError as e:
    print(e)
    print("Ensure your API token has the correct permissions and that the Base ID, Table Name, and View Name are correct.")
except Exception as e:
    print(e)
    print("An unexpected error occurred.")
