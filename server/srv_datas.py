from datetime import datetime
import os
"""
    Data for the Server part
"""

# ----------------------------------------------------

HOST = "127.0.0.1"
PORT = 65432
BUFFER_SIZE = 1024
ENCODE_FORMAT = "utf-8"

DB_FILES_DIRECTORY = os.path.join(os.path.dirname(__file__), '..', 'db_files')
USERS_DATABASE = os.path.join(DB_FILES_DIRECTORY, 'users.json')
MESSAGES_DATABASE = os.path.join(DB_FILES_DIRECTORY, 'messages.json')

# ----------------------------------------------------

CLOSE = "close"

# ----------------------------------------------------

START_TIME = datetime.now()
DATE = datetime.now().strftime("%Y-%m-%d")
VERSION = "0.1.8"

# ----------------------------------------------------







