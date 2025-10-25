import streamlit as st
import pandas as pd
from db_connection import get_connection

st.set_page_config(page_title="Customers and Orders", page_icon="👤")
st.title("👤 Customers, Orders & Items Overview")

# Connect to DB
conn = get_connection()
if not conn:
    st.error("❌ Database connection failed.")
    st.stop()

cursor = conn.cursor(dictionary=True)

# --- CUSTOMER SECTION ---
st.subheader("🧾 Customer List")

cursor.execute("""
    SELECT 
        CustomerID,
        CONCAT(FirstName, ' ', LastName) AS FullName,
        Email,
        CONCAT(AddressStreet, ', ', AddressCity, ', ', AddressState, ' - ', AddressPincode) AS FullAddress
    FROM Customer
    ORDER BY CustomerID;
""")
customers = cursor.fetchall()

if customers:
    st.dataframe(pd.DataFrame(customers))
else:
    st.info("No customer records found.")

st.divider()

# --- ORDERS SECTION ---
st.subheader("📦 Orders Summary")

cursor.execute("""
    SELECT 
        o.OrderID,
        CONCAT(c.FirstName, ' ', c.LastName) AS Customer,
        o.Priority,
        o.Status,
        o.BillingAmount,
        CONCAT(o.BillingAddressStreet, ', ', o.BillingAddressCity, ' - ', o.BillingAddressPincode) AS BillingAddress,
        dz.ZoneName AS DeliveryZone,
        o.OrderDateTime
    FROM OrderTable o
    JOIN Customer c ON o.CustomerID = c.CustomerID
    LEFT JOIN DeliveryZone dz ON o.DeliveryZoneID = dz.DeliveryZoneID
    ORDER BY o.OrderID DESC;
""")
orders = cursor.fetchall()

if orders:
    df_orders = pd.DataFrame(orders)
    st.dataframe(df_orders)
else:
    st.info("No orders available.")

st.divider()

# --- ORDER ITEMS SECTION ---
st.subheader("📦 Individual Order Items")

cursor.execute("""
    SELECT 
        oi.OrderID,
        o.CustomerID,
        CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
        oi.SKU,
        oi.Description,
        oi.WeightKg,
        oi.LengthCm,
        oi.WidthCm,
        oi.HeightCm,
        oi.Quantity,
        IF(oi.SpecialHandlingFlag=1, 'Yes', 'No') AS SpecialHandling
    FROM OrderItem oi
    JOIN OrderTable o ON oi.OrderID = o.OrderID
    JOIN Customer c ON o.CustomerID = c.CustomerID
    ORDER BY oi.OrderID;
""")
order_items = cursor.fetchall()

if order_items:
    df_items = pd.DataFrame(order_items)
    st.dataframe(df_items)
else:
    st.info("No order items found.")

cursor.close()
conn.close()
