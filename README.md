# 🚀 AeroSwift Drone Logistics Management System

### **Efficient • Automated • Compliant**

AeroSwift is a **drone-based logistics management system** designed to automate and monitor the full lifecycle of drone deliveries — from order placement to pilot assignment, compliance validation, and flight logging.  

Developed as part of a **Database Management Systems (DBMS)** project, this system demonstrates how **relational databases**, **stored procedures**, and **Streamlit dashboards** can model real-world logistics automation.

---

## 🧩 **Project Overview**

AeroSwift Logistics simulates a company that uses **autonomous drones** and **certified pilots** to transport lightweight packages across delivery zones in Indian cities.  
The system handles:

- Customer and order management  
- Drone and pilot allocation  
- Flight route validation  
- Airspace compliance checks  
- Real-time delivery tracking and reporting  

All workflows are **automatically triggered** via MySQL **stored procedures** and **triggers**, simulating an intelligent logistics control center.

---

## 🌍 **Miniworld Description**

The project models a **realistic operational ecosystem** involving:

| Entity | Description |
|---------|-------------|
| **Customer** | Places delivery orders |
| **Order & OrderItem** | Details of each purchase and package |
| **Delivery** | Central process connecting drones, pilots, and routes |
| **Drone & DroneType** | Represents fleet capacity and specifications |
| **Pilot & PilotLicense** | Ensures only licensed pilots operate authorized drones |
| **Permit & Waiver** | Legal clearances from aviation authorities |
| **Route & AirspaceZone** | Path and restrictions for each delivery flight |
| **ComplianceReport & FlightLog** | Records pre-flight checks and telemetry |
| **MaintenanceRecord** | Logs drone inspections and servicing |
| **Invoice** | Handles payment tracking and billing |

---

## ⚙️ **System Workflow**

```text
1️⃣ Customer places an order through the Streamlit interface.
2️⃣ Database automatically assigns a suitable drone (procedure: assign_drone_to_delivery).
3️⃣ A pilot is verified and assigned (procedure: assign_pilot_to_delivery).
4️⃣ Route is validated against restricted airspace (procedure: approve_route).
5️⃣ Pre-flight safety checks are enforced by triggers.
6️⃣ Flight details are logged automatically in FlightLog.
7️⃣ Post-flight compliance and maintenance updates are recorded.
8️⃣ Invoice is generated and linked to the delivery.
