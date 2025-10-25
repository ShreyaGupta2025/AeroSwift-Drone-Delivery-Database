### 🌍 Miniworld Scenario

AeroSwift Logistics is a **drone-based delivery management system** designed to handle logistics operations for lightweight packages across different zones of a city.

The miniworld models how an organization uses **autonomous drones** to deliver goods efficiently while ensuring:
- **Airspace compliance** (following aviation rules),
- **Drone and pilot certification validation**, and
- **Operational safety and tracking** through automated database triggers and procedures.

---

### 🧩 Objective

To **design and implement a relational database** and a connected **web-based interface** for managing:
- Customers and their orders,
- Drone fleets and pilot licensing,
- Delivery scheduling and route management,
- Compliance with aviation regulations, and
- Maintenance and reporting.

The goal is to simulate **real-world drone logistics automation**, where placing an order automatically triggers backend processes for drone assignment, pilot verification, route approval, and delivery execution.

---

### 🧠 Key Entities in the Miniworld

| Entity | Description |
|---------|-------------|
| **Customer** | People who place delivery orders through the system |
| **Order & Order Items** | Information about customer orders and specific products |
| **Delivery Zone** | Defined operational zones where drone delivery is supported |
| **Drone & Drone Type** | Represents individual drones and their specifications (payload, range, energy, etc.) |
| **Pilot** | Licensed drone operators with verified certifications |
| **Permit** | Permissions granted by aviation authorities for drone operations |
| **Route & Route Zone** | Defines flight paths and their interaction with restricted airspace |
| **Regulatory Authority** | Entities like DGCA or Air Traffic Control Bureau overseeing airspace compliance |
| **Delivery** | Core operational record connecting customer, order, drone, pilot, and route |
| **Flight Log** | Post-flight telemetry and data summary for each delivery |
| **Maintenance Record** | Ensures drone health and scheduled servicing |
| **Compliance Report** | Logs of regulatory checks before and after flights |

---

### ⚙️ How the Workflow Operates

1. **Order Placement**
   - A customer places an order through the Streamlit interface.
   - Order details and selected items are stored in `OrderTable` and `OrderItem`.

2. **Automatic Drone Assignment**
   - A stored procedure (`assign_drone_to_delivery`) validates payload and battery.
   - If the drone qualifies, it’s automatically assigned to the delivery.

3. **Pilot Verification**
   - Another procedure (`assign_pilot_to_delivery`) ensures the pilot’s license matches the drone type and is valid through the delivery date.

4. **Route Approval**
   - The system runs checks using `approve_route` to ensure no restricted airspace is violated.

5. **Delivery Execution**
   - Delivery begins once all validations are cleared.
   - A trigger (`trg_before_delivery_update`) ensures safety conditions are met before “InTransit” status.

6. **Flight Logging**
   - Real-time telemetry data is logged in `FlightLog`.
   - Compliance reports are generated automatically.

7. **Completion & Billing**
   - Once the delivery ends, costs are calculated and recorded in `Invoice`.

---

### 🧾 Features Implemented

✅ End-to-end database with **20+ interlinked tables**  
✅ **Stored Procedures & Triggers** for automated backend operations  
✅ **Preloaded data** for companies, drones, pilots, zones, and routes  
✅ **Streamlit Interface** for:
- Placing new orders  
- Viewing all customers, drones, and deliveries  
- Visualizing analytics and compliance  
✅ Real-time workflow simulation  
✅ Normalized relational schema ensuring data integrity  

---

### 🎯 Real-World Relevance

The system reflects **how drone logistics companies like Zipline, Skydio, or Amazon Prime Air** operate:
- Assigning drones dynamically based on package load  
- Managing pilot and route authorizations  
- Logging every delivery for compliance and analytics  

It can be easily extended to include:
- Weather integration (for delivery scheduling),
- Live GPS tracking of drones,
- Customer order tracking pages.

---

### 🧮 Technologies Used

| Layer | Technology |
|--------|-------------|
| **Frontend** | Streamlit (Python) |
| **Backend Logic** | MySQL Stored Procedures & Triggers |
| **Database** | MySQL (InnoDB) |
| **Libraries** | Pandas, mysql.connector, Streamlit |
| **Optional Hosting** | Streamlit Cloud / Render / PlanetScale |

---

### 🧾 Project Summary

**AeroSwift Drone Logistics Management System**  
is a complete database application that models the operational and regulatory side of drone-based deliveries.  

It enables **automation, monitoring, and compliance** — from customer orders to flight logging — representing the next generation of urban logistics management.

---

### 👩‍💻 Developed By

**Shreya Gupta**  
B.Tech (EEE), BITS Pilani Hyderabad Campus  
Project: *AeroSwift Drone Logistics Management System* 