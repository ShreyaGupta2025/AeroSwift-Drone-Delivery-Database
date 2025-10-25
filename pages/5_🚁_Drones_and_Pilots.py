import streamlit as st
import pandas as pd
from db_connection import get_connection

st.set_page_config(page_title="Drones and Pilots", page_icon="🚁")
st.title("🚁 Drones and Pilots Overview")

conn = get_connection()
if not conn:
    st.error("Database connection failed.")
    st.stop()

cursor = conn.cursor(dictionary=True)

st.subheader("🛸 Available Drones")
cursor.execute("""
    SELECT d.DroneID, d.RegistrationNo, dt.ModelName, d.Status, d.BatteryLevelPercent, dh.HubName
    FROM Drone d
    JOIN DroneType dt ON d.DroneTypeID = dt.DroneTypeID
    JOIN DroneHub dh ON d.CurrentHubID = dh.HubID
""")
drones = cursor.fetchall()
st.dataframe(pd.DataFrame(drones))

st.subheader("👨‍✈️ Pilots")
cursor.execute("""
    SELECT PilotID, Name, LicenseNo, LicenseIssueDate, LicenseExpiryDate, ActiveStatus
    FROM Pilot
""")
pilots = cursor.fetchall()
st.dataframe(pd.DataFrame(pilots))

cursor.close()
conn.close()
