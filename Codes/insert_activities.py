import pandas as pd
from sqlalchemy import create_engine

# Database configuration (replace with your actual credentials)
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_NAME = 'studentactivitydb'

# Create the database connection
engine = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

# Read the CSV file
csv_file = '..\\Data\\Activities.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

# Map CSV columns to the database schema
df.rename(columns={
    'ActivityID': 'Activity_Id',
    'ActivityName': 'Name',
    'Activity Description': 'Description',
    'Learning Outcomes/Competencies': 'Outcome',
    'Graded Description Grade 1': 'Grade_1',
    'Graded Description Grade 2': 'Grade_2',
    'Graded Description Grade 3': 'Grade_3',
    'Graded Description Grade 4': 'Grade_4',
    'Graded Description Grade 5': 'Grade_5'
}, inplace=True)

# Insert data into the Activities table
df.to_sql('Activities', con=engine, if_exists='append', index=False)

print("Data inserted successfully.")
