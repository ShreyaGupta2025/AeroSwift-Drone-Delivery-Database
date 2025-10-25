import streamlit as st
import pandas as pd
from db_connection import get_connection

st.set_page_config(page_title="Compliance & Maintenance", page_icon="⚙️")
st.title("⚙️ Compliance and Maintenance Overview")

conn = get_connection()
if not conn:
    st.error("Database connection failed.")
    st.stop()

cursor = conn.cursor(dictionary=True)

st.subheader("🧾 Compliance Reports")
cursor.execute("""
    SELECT ReportID, DeliveryID, ReportType, CheckDate, Status, Remarks
    FROM ComplianceReport
    ORDER BY CheckDate DESC
""")
compliance = cursor.fetchall()
st.dataframe(pd.DataFrame(compliance))

st.subheader("🛠️ Maintenance Records")
cursor.execute("""
    SELECT m.MaintenanceID, d.RegistrationNo AS Drone, m.StartDate, m.EndDate, 
           m.MaintenanceType, m.PerformedBy, m.NextDueDate
    FROM MaintenanceRecord m
    JOIN Drone d ON m.DroneID = d.DroneID
""")
maintenance = cursor.fetchall()
st.dataframe(pd.DataFrame(maintenance))

cursor.close()
conn.close()
