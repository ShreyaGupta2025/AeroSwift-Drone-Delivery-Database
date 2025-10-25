import mysql.connector
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("host"),
            user=os.getenv("root"),
            password=os.getenv("password"),
            database=os.getenv("database"),
        )
        return connection
    except mysql.connector.Error as err:
        st.error(f"Database connection failed: {err}")
        return None
