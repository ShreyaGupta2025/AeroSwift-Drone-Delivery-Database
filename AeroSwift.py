import streamlit as st
from streamlit_extras.let_it_rain import rain

# 🎯 PAGE CONFIG
st.set_page_config(
    page_title="AeroSwift | Drone Logistics Management",
    page_icon="🚀",
    layout="wide",
)

# 🌈 PAGE HEADER
st.markdown("<h1 style='text-align:center; color:#00b4d8;'>🚀 AeroSwift</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:gray;'>Smart Drone Logistics for Modern Deliveries</h3>", unsafe_allow_html=True)
st.write("")
st.markdown("<p style='text-align:center;'>Automate, track, and manage every phase of your drone-based delivery operations — from customer orders to final confirmation.</p>", unsafe_allow_html=True)




st.markdown(
    """
    
    **AeroSwift** is a modern **drone logistics management system** that automates and supervises every phase of drone-based deliveries — from order placement to route approval and final delivery confirmation.

    This platform bridges **logistics, aviation safety, and database automation** to create a realistic model of a drone delivery company operating across Indian cities.
    """
)
st.divider()
# =========================
# 📊 SYSTEM METRICS (Demo)
# =========================
st.header("📊 System Performance Snapshot")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Drones", "18", "↑ 2")
col2.metric("Registered Pilots", "15", "↑ 1")
col3.metric("Deliveries Completed", "132", "↑ 12%")
col4.metric("Compliance Score", "98%", "✅")

st.caption("*(Demo values — can be linked to live MySQL database for real-time updates.)*")

st.divider()


# 🌟 FEATURE OVERVIEW
st.subheader("✨ Key Modules")
features = {
    "📦 Customer & Orders": "Manage customer details, order creation, and billing efficiently.",
    "✈️ Drones & Pilots": "Ensure drones are flight-ready and pilots are licensed.",
    "🔄 Automated Deliveries": "Assign routes and confirm deliveries automatically.",
    "🧾 Compliance & Logs": "Monitor drone health and ensure safety compliance.",
    "📊 Analytics & Reports": "Track performance and airspace efficiency metrics."
}

cols = st.columns(3)
for i, (title, desc) in enumerate(features.items()):
    with cols[i % 3]:
        st.markdown(f"### {title}")
        st.write(desc)

st.divider()

# =========================
# 💡 MISSION STATEMENT
# =========================
st.header("💡 Our Mission")

st.markdown(
    """
    To redefine **urban logistics** through drone automation — combining **efficiency**, **safety**, and **data-driven compliance**.  

    AeroSwift demonstrates how modern logistics systems can integrate **database intelligence**, **aeronautical safety**, and **AI-ready automation** to deliver smarter, faster, and safer.
    """
)

st.divider()

# 🧭 CUSTOMER GUIDANCE BOX

st.markdown("### 🧭 Getting Started")

with st.container():
    st.markdown("""
    <div style="
        background-color: #0E1117;
        border: 2px solid #00b4d8;
        border-radius: 12px;
        padding: 25px;
        margin-top: 10px;
    ">
        <h3 style='color:#00b4d8;'>💡 Ready to Place an Order?</h3>
        <p style='color:#cccccc;'>
        If you're a new customer, start by creating your first order. 
        AeroSwift will automatically handle drone assignment, route scheduling, and delivery confirmation for you.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
        if st.button("🛒 Proceed to Order Placement"):
            st.switch_page("pages/2_🛒_Place_Order.py")
        st.markdown("</div>", unsafe_allow_html=True)


st.caption("✅ The workflow runs automatically, simulating a realistic drone delivery lifecycle.")


