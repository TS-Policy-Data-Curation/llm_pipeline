import mysql.connector
import os
from langchain_community.vectorstores import SingleStoreDB

# returns a MySQL database connection object
def connect_to_db():
    """Connect to the SingleStore database."""
    return mysql.connector.connect(
        host=os.environ['SINGLESTORE_HOST'],       # e.g., 'localhost' or the IP address of your SingleStore instance
        user=os.environ['SINGLESTORE_USER'],       # e.g., 'root' or your SingleStore username
        password=os.environ['SINGLESTORE_PASSWORD'],  # Your password
        database=os.environ['SINGLESTORE_DATABASE']   # The database you are working with
    )