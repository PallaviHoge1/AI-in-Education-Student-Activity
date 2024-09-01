import os
import logging
from datetime import datetime
from configparser import ConfigParser

# Initialize ConfigParser
config = ConfigParser()

# Get current date and format it as day_month_year
current_date = datetime.now().strftime("%d_%m_%y")

# Create dynamic filename for logging
log_filename = f"..//Logs//EncryptionLogs//encryption_{current_date}.txt"

# Logger configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename)
    ]
)

try:
    from cryptography.fernet import Fernet
    # Read the configuration file
    config.read('..//Configurations//encryptConfig.ini')
    file_name = config['Encryption']['name']
    Role = "Teacher"
    Name = "nName"
    KEY_PATH = f"..//Keys//{Role}//{Name}//secret.key"

    # Function to generate a key and save it into a file
    def generate_key():
        try:
            key = Fernet.generate_key()
            try:
                with open(KEY_PATH, "wb") as key_file:
                    key_file.write(key)
            except Exception as e:
                os.makedirs(os.path.dirname(KEY_PATH), exist_ok=True)
                with open(KEY_PATH, "wb") as key_file:
                    key_file.write(key) 
            print(key)
            logging.info("Encryption key generated and saved successfully.")   
        except Exception as e:
            logging.error(f"Failed to generate key: {e}")    

    # Function to load the previously generated key
    def load_key():
        try:
            key = open(KEY_PATH, "rb").read()
            logging.info("Encryption key loaded successfully.")
            return key
        except Exception as e:
            logging.error(f"Failed to load key: {e}")

    # Function to encrypt a message
    def encrypt_password(password: str) -> bytes:
        try:
            key = load_key()
            fernet = Fernet(key)
            encrypted_password = fernet.encrypt(password.encode())
            logging.info("Password encrypted successfully.")
            return encrypted_password
        except Exception as e:
            logging.error(f"Failed to encrypt password: {e}")

    # Function to decrypt a message
    def decrypt_password(encrypted_password: bytes) -> str:
        try:
            key = load_key()
            logging.info(key)
            fernet = Fernet(key)
            decrypted_password = fernet.decrypt(encrypted_password).decode()
            logging.info("Password decrypted successfully.")
            return decrypted_password
        except Exception as e:
            logging.error(f"Failed to decrypt password: {e}")

    # Example usage
    if __name__ == "__main__":
        try:
            # Generate and write a new key (only run this once to create the key file)
            generate_key()
            encryption_option = int(input("What do you want to encrypt? \n1. Db Password\n2. User Password\nType 1 or 2: "))
            password = input("Please input your password: ")
            encrypted = encrypt_password(password)
            print(f"Encrypted: {encrypted}")

            decrypted = decrypt_password(encrypted)
            print(f"Decrypted: {decrypted}")
        except Exception as e:
            logging.critical(f"An unexpected error occurred: {e}")

except Exception as e:
    logging.error(f"An unexpected error occurred in model import: {e}")