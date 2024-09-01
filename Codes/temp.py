import os
import logging
from datetime import datetime
from configparser import ConfigParser
from cryptography.fernet import Fernet

# Function to decrypt a message

key = 'sQNBm5F7996yhp1QhwlrUTAXfPFS-s7Bho4itka4kq8='
encrypted_password = "gAAAAABm0_Sxnhikeljc9C-KVknQr24iAnSTgV5B_lltqTP0xNMGx-2CQqysRTvM03YcyIwX-2ge1O9pNMKljNjk6Ausk_-FpQ=="
print(key)
fernet = Fernet(key)
decrypted_password = fernet.decrypt(encrypted_password).decode()
print("Password decrypted successfully.")
print(decrypted_password)