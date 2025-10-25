import streamlit as st
import mysql.connector
from db_connection import get_connection
import pandas as pd

st.set_page_config(page_title="AeroSwift Dashboard", page_icon="🏠")
st.title("🏠 Welcome to AeroSwift Logistics Platform")

conn = get_connection()
if not conn:
    st.error("Database connection failed.")
    st.stop()

cursor = conn.cursor(dictionary=True)

# Total summary cards
cursor.execute("SELECT COUNT(*) AS total_customers FROM Customer")
customers = cursor.fetchone()["total_customers"]

cursor.execute("SELECT COUNT(*) AS total_orders FROM OrderTable")
orders = cursor.fetchone()["total_orders"]

cursor.execute("SELECT COUNT(*) AS total_drones FROM Drone")
drones = cursor.fetchone()["total_drones"]

cursor.execute("SELECT COUNT(*) AS total_deliveries FROM Delivery")
deliveries = cursor.fetchone()["total_deliveries"]

col1, col2, col3, col4 = st.columns(4)
col1.metric("👤 Customers", customers)
col2.metric("🧾 Orders", orders)
col3.metric("🚁 Drones", drones)
col4.metric("📦 Deliveries", deliveries)

st.divider()

# Delivery status summary
st.subheader("📊 Delivery Status Overview")
cursor.execute("SELECT Status, COUNT(*) AS count FROM Delivery GROUP BY Status")
data = cursor.fetchall()
df = pd.DataFrame(data)
st.bar_chart(df.set_index("Status"))

cursor.close()
conn.close()
