import json
import mysql.connector
from Encrypt import decrypt_password  # Import the decryption function
from configparser import ConfigParser

# Initialize ConfigParser
config = ConfigParser()

def load_config():
    # Read the configuration file
    config.read('..//Configurations//dBConfig.ini')
    print(config)
    return config

def create_connection():
    # Load configuration from config.json
    config = load_config()
    db_username = config['Database']['user']
    # db_encrypted_password = config['Database']['password']
    db_password = config['Database']['password']
    db_name = config['Database']['database']

    # Decrypt the password
    # db_password = decrypt_password(db_encrypted_password)
    print(f"d{db_username},{db_name},{db_password}")

    # connection = mysql.connector.connect(
    #     host='localhost',
    #     user='root',
    #     password='root',
    #     database='mysql'
    # )
    # Establish connection to the MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        user=db_username,
        password=db_password,
        database=db_name
    )
    return connection

# Example usage
connection = create_connection()
if connection.is_connected():
    print("Connected to the database successfully!")
    connection.close()