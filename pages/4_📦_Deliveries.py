import streamlit as st
import pandas as pd
from db_connection import get_connection

st.set_page_config(page_title="Deliveries", page_icon="📦")
st.title("📦 Deliveries Overview")

conn = get_connection()
if not conn:
    st.error("Database connection failed.")
    st.stop()

cursor = conn.cursor(dictionary=True)

cursor.execute("""
    SELECT d.DeliveryID, d.Status, d.ScheduledStartTime, d.ScheduledEndTime,
           dr.RegistrationNo AS Drone, p.Name AS Pilot, o.CustomerID
    FROM Delivery d
    LEFT JOIN Drone dr ON d.AssignedDroneID = dr.DroneID
    LEFT JOIN Pilot p ON d.AssignedPilotID = p.PilotID
    LEFT JOIN OrderTable o ON d.OrderID = o.OrderID
    ORDER BY d.DeliveryID DESC
""")
deliveries = cursor.fetchall()

st.dataframe(pd.DataFrame(deliveries))

cursor.close()
conn.close()
