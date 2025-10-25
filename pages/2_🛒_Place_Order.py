import streamlit as st
import mysql.connector
from datetime import datetime
from db_connection import get_connection

# ==============================
# 🛒 Place Order Page
# ==============================
st.set_page_config(page_title="Place an Order", page_icon="🛒")

st.title("🛒 Place a New Order")
st.markdown("Select your delivery location and fill in your details below.")
st.divider()

# Connect to DB
conn = get_connection()
if not conn:
    st.error("❌ Failed to connect to database.")
    st.stop()

cursor = conn.cursor(dictionary=True)

# ==============================
# 📍 Step 1: Delivery Zone / City
# ==============================
st.subheader("📦 Choose Your Delivery Location")

cursor.execute("SELECT DeliveryZoneID, ZoneName, PriorityTag FROM DeliveryZone ORDER BY ZoneName;")
zones = cursor.fetchall()

available_cities = {
    "Delhi": "Zone A",
    "Bangalore": "Zone B",
    "Chennai": "Zone C",
    "Mumbai": "Zone D",
    "Hyderabad": "Zone F",
    "Kolkata": "Zone G",
    "Pune": "Zone H",
    "Ahmedabad": "Zone I",
    "Lucknow": "Zone J"
}

city_choice = st.selectbox("Select your city", ["Select City"] + list(available_cities.keys()))

if city_choice == "Select City":
    st.warning("Please select a valid city to proceed.")
    st.stop()

zone_name = available_cities.get(city_choice)

# Check if delivery zone exists in database
cursor.execute("SELECT DeliveryZoneID FROM DeliveryZone WHERE ZoneName = %s", (zone_name,))
zone = cursor.fetchone()

if not zone:
    st.error(f"🚧 Sorry! We're not delivering to **{city_choice}** yet. We'll be there soon! 🛫")
    cursor.close()
    conn.close()
    st.stop()

zone_id = zone["DeliveryZoneID"]

# ==============================
# 👤 Step 2: Customer Information
# ==============================
st.subheader("👤 Customer Information")

col1, col2 = st.columns(2)
with col1:
    first_name = st.text_input("First Name")
    email = st.text_input("Email")
with col2:
    last_name = st.text_input("Last Name")
    phone = st.text_input("Phone Number")

street = st.text_input("Street Address")
pincode = st.text_input("Pincode")

# ==============================
# 📦 Step 3: Select Item
# ==============================
st.subheader("🧾 Select Item to Order")

ITEM_CATALOG = [
    {"SKU": "DRN-BAT-001", "Name": "Drone Battery Pack 3000mAh", "Weight": 1.25, "Price": 4999},
    {"SKU": "DRN-CAM-003", "Name": "HD Aerial Camera", "Weight": 0.45, "Price": 2999},
    {"SKU": "DRN-PROP-007", "Name": "Propeller Set", "Weight": 0.30, "Price": 899},
    {"SKU": "DRN-GIM-006", "Name": "3-Axis Gimbal", "Weight": 0.75, "Price": 4999},
]

item_names = [f"{item['Name']} (₹{item['Price']})" for item in ITEM_CATALOG]
selected_item = st.selectbox("Choose Item", item_names)
quantity = st.number_input("Quantity", min_value=1, step=1)

# ==============================
# ✅ Step 4: Place Order
# ==============================
if st.button("🚀 Place Order"):
    item = ITEM_CATALOG[item_names.index(selected_item)]
    total_cost = item["Price"] * quantity
    total_weight = item["Weight"] * quantity

    # Insert or get customer
    cursor.execute("SELECT CustomerID FROM Customer WHERE Email = %s", (email,))
    result = cursor.fetchone()

    if result:
        customer_id = result["CustomerID"]
    else:
        cursor.execute("""
            INSERT INTO Customer (FirstName, LastName, Email, AddressStreet, AddressCity, AddressState, AddressPincode)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, email, street, city_choice, "StateX", pincode))
        conn.commit()
        customer_id = cursor.lastrowid

    # Insert order
    cursor.execute("""
        INSERT INTO OrderTable (CustomerID, Priority, Status, BillingAmount, BillingAddressStreet, BillingAddressCity, BillingAddressPincode, DeliveryZoneID)
        VALUES (%s, 'Standard', 'Created', %s, %s, %s, %s, %s)
    """, (customer_id, total_cost, street, city_choice, pincode, zone_id))
    conn.commit()
    order_id = cursor.lastrowid

    # Insert item
    cursor.execute("""
        INSERT INTO OrderItem (OrderID, ItemNo, SKU, Description, WeightKg, Quantity)
        VALUES (%s, 1, %s, %s, %s, %s)
    """, (order_id, item["SKU"], item["Name"], item["Weight"], quantity))
    conn.commit()

    # Insert delivery
    cursor.execute("""
        INSERT INTO Delivery (OrderID, DeliveryZoneID, SourceHubID, ScheduledStartTime, ScheduledEndTime, Status)
        VALUES (%s, %s, 1, NOW(), DATE_ADD(NOW(), INTERVAL 2 HOUR), 'Scheduled')
    """, (order_id, zone_id))
    conn.commit()

    st.success(f"✅ Order placed successfully for **{city_choice}**! Order ID: {order_id}")
    st.info("Drone assignment and pilot allocation will be processed automatically.")
    st.balloons()

cursor.close()
conn.close()
