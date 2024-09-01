import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import random
import string

# Database configuration
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_NAME = 'studentactivitydb'

# Create SQLAlchemy engine
engine = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

# Function to generate unique 5-digit IDs
def generate_unique_ids(num_ids):
    ids = set()
    while len(ids) < num_ids:
        ids.add(random.randint(10000, 99999))
    return list(ids)

# Function to generate random 6-digit passwords
def generate_random_passwords(num_passwords):
    return [''.join(random.choices(string.digits, k=6)) for _ in range(num_passwords)]

# Generate IDs for 68 users (58 students + 8 teachers + 1 principal + 1 administrator)
user_ids = generate_unique_ids(68)

# Generate random 6-digit passwords for each user
passwords = generate_random_passwords(68)

# Create data for Persona table
persona_data = {
    'User_Id': user_ids,
    'Role_Id': [4] * 60 + [3] * 8 + [2] + [1],  # 4 for students, 3 for teachers, 2 for principal, 1 for administrator
    'Password': passwords
}

# Create DataFrame
persona_df = pd.DataFrame(persona_data)

# Insert DataFrame into database
try:
    # Ensure the table exists before inserting
    persona_df.to_sql('Persona', con=engine, if_exists='append', index=False)
    print("Persona data inserted successfully.")
except SQLAlchemyError as e:
    print(f"An error occurred: {e}")
