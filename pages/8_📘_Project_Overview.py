import streamlit as st

st.set_page_config(page_title="Project Overview", page_icon="📘")
st.title("📘 AeroSwift Drone Logistics Management System")
st.subheader("Miniworld Description & Project Overview")

st.markdown("""
### 🌍 Miniworld Scenario

AeroSwift Logistics is a **drone-based delivery management system** that manages end-to-end operations for lightweight package deliveries across various zones of a city.

The miniworld models how a company uses **autonomous drones** and **certified pilots** to transport goods safely, efficiently, and within airspace regulations.  
It incorporates **customers, drones, pilots, delivery routes, regulatory authorities**, and more into one cohesive database system.
""")

st.info("💡 The system workflow starts automatically once an order is placed — triggering drone assignment, pilot verification, and delivery tracking in real-time through MySQL stored procedures and triggers.")

st.markdown("""
---

### 🎯 Project Objectives

The objective of this project is to **design, implement, and demonstrate a database-backed logistics system** capable of:
- Automating drone delivery workflows
- Managing operational data with high integrity
- Enforcing compliance and safety through database logic
- Providing a user-friendly web interface using Streamlit

This system bridges **Database Management Systems (DBMS)** principles with **real-world drone logistics automation**.
""")

st.markdown("""
---

### 🧠 Key Entities in the Miniworld

| Entity | Description |
|---------|-------------|
| **Customer** | Individuals placing delivery orders |
| **Order & OrderItem** | Stores information about orders and product details |
| **Drone & DroneType** | Represents drone units and their specifications (payload, range, energy use) |
| **Pilot & PilotLicense** | Licensed personnel authorized to operate specific drone types |
| **Permit** | Legal authorization for drone operation in certain zones |
| **Route & RouteZone** | Defines flight paths and intersecting airspace zones |
| **RegulatoryAuthority** | Governing bodies ensuring flight safety and rule compliance |
| **Delivery** | Central operational entity connecting drones, pilots, and orders |
| **FlightLog** | Telemetry and operational logs of each flight |
| **MaintenanceRecord** | Logs servicing and health checks for each drone |
| **ComplianceReport** | Documents legal and safety verifications for each delivery |

---

### ⚙️ Workflow Logic (Automated Backend)

Once an order is placed:
1. **Order Entry** — Details are stored in `OrderTable` and `OrderItem`.  
2. **Drone Validation** — The stored procedure `assign_drone_to_delivery` checks for payload and battery sufficiency.  
3. **Pilot Verification** — The system executes `assign_pilot_to_delivery` ensuring pilot’s license validity.  
4. **Route Approval** — `approve_route` checks for no-fly zones or missing waivers.  
5. **Delivery Execution** — Trigger `trg_before_delivery_update` ensures safety before launch.  
6. **Compliance Reports** — Generated pre-flight and post-flight automatically.  
7. **Maintenance Updates** — Logged after each completed delivery.

All these backend processes occur **automatically** — the user only places an order; the database handles everything else.
""")


# =========================
# 🧭 DATABASE WORKFLOW DIAGRAM
# =========================
#st.header("🧭 How the Database Works")

st.markdown("The following diagram represents how AeroSwift’s database components interact to manage automated logistics operations:")

graph_code = """
digraph AeroSwift {
    rankdir=LR;
    node [shape=box, style=filled, color="#00B4D8", fontname="Helvetica", fontsize=12, fillcolor="#e6f7ff"];

    Customer -> OrderTable [label="places"];
    OrderTable -> Delivery [label="initiates"];
    Delivery -> Drone [label="assigned via procedure"];
    Delivery -> Pilot [label="verified via procedure"];
    Delivery -> Route [label="follows"];
    Route -> RegulatoryAuthority [label="approved by"];
    Delivery -> ComplianceReport [label="logs checks"];
    Delivery -> FlightLog [label="records flight"];
    Drone -> MaintenanceRecord [label="requires"];
    Delivery -> Invoice [label="generates billing"];
}
"""

st.graphviz_chart(graph_code)

st.caption("📊 This represents the logical flow inside the MySQL database once an order is placed.")



st.markdown("""
---

### 🧾 Features Implemented

✅ Fully normalized relational schema (3NF)  
✅ 20+ interconnected tables  
✅ Stored Procedures & Triggers for automation  
✅ Interactive Streamlit interface  
✅ Integrated MySQL connectivity  
✅ Real-time delivery simulation  
✅ Visual analytics and maintenance logs

---

### 🧮 Technologies Used

| Layer | Technology |
|--------|-------------|
| **Frontend** | Streamlit (Python) |
| **Database** | MySQL (InnoDB) |
| **Logic** | Stored Procedures & Triggers |
| **Libraries** | Pandas, mysql.connector |
| **Deployment** | Streamlit Cloud / Render |

---

### 🧾 Project Summary

**AeroSwift Drone Logistics Management System** demonstrates how a relational database can drive automation in drone-based logistics — maintaining safety, compliance, and operational efficiency.

It bridges **theory (DBMS concepts)** with **practical application (smart logistics)**, reflecting how real-world companies like Zipline or Amazon Prime Air operate.

---

### 👩‍💻 Developed By
**Shreya Gupta**  
Birla Institute of Technology and Science (BITS) Pilani, Hyderabad Campus  

💬 *“From data to delivery — automating logistics the smart way.”*
""")
