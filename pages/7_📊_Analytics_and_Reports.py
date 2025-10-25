import streamlit as st
import pandas as pd
from db_connection import get_connection

st.set_page_config(page_title="Analytics", page_icon="📊")
st.title("📊 Analytics Dashboard")

conn = get_connection()
if not conn:
    st.error("Database connection failed.")
    st.stop()

cursor = conn.cursor(dictionary=True)

st.subheader("🚁 Drone Status Distribution")
cursor.execute("SELECT Status, COUNT(*) AS Count FROM Drone GROUP BY Status")
df_drone = pd.DataFrame(cursor.fetchall())
st.bar_chart(df_drone.set_index("Status"))

st.subheader("📦 Delivery Completion Stats")
cursor.execute("SELECT Status, COUNT(*) AS Count FROM Delivery GROUP BY Status")
df_delivery = pd.DataFrame(cursor.fetchall())
st.bar_chart(df_delivery.set_index("Status"))

st.subheader("👨‍✈️ Pilot License Validity")
cursor.execute("""
    SELECT 
        CASE 
            WHEN LicenseExpiryDate > CURDATE() THEN 'Active'
            ELSE 'Expired'
        END AS LicenseStatus,
        COUNT(*) AS Count
    FROM Pilot
    GROUP BY LicenseStatus
""")
df_pilot = pd.DataFrame(cursor.fetchall())
st.bar_chart(df_pilot.set_index("LicenseStatus"))

cursor.close()
conn.close()
