import streamlit as st
import pandas as pd
import numpy as np

# Set dark theme and page config
st.set_page_config(page_title="DrainWatch Dashboard", layout="wide")

st.title("🌊 DrainWatch: Municipal GIS Command Center")
st.markdown("### Live Flood Risk & Vector Breeding Tracking")

# Layout with 3 columns for quick stats
col1, col2, col3 = st.columns(3)
col1.metric("Active Sensor Nodes (API)", "50", "+5 this week")
col2.metric("High Flood Risk Zones", "2", "-1 from yesterday")
col3.metric("Critical Vector Breeding Alerts", "1", "Requires Fogging")

st.divider()

# Create fake map data for the prototype (Centered vaguely around Chennai)
st.subheader("🗺️ Live Subterranean Node Map")
map_data = pd.DataFrame(
    np.random.randn(50, 2) / [50, 50] + [13.0827, 80.2707],
    columns=['lat', 'lon']
)
st.map(map_data, zoom=11)

st.divider()

st.subheader("🚨 Automated Dispatch Logs")
alerts = pd.DataFrame({
    'Ward': ['Velachery', 'T. Nagar', 'Adyar'],
    'Status': ['🔴 CRITICAL FLOOD', '🟡 VECTOR RISK', '🟢 NORMAL'],
    'AI Prediction': ['Overflow in 2 hrs', 'Stagnant > 48 hrs', 'Clear flow'],
    'Action': ['Dispatch Pumping Truck', 'Dispatch Fogging Team', 'None']
})
st.table(alerts)

st.sidebar.success("✅ System Status: ALL SYSTEMS OPERATIONAL")
st.sidebar.info("Model: PyTorch GCN-LSTM (V1.0)")

st.divider()
st.subheader("🌦️ Live IMD Weather Ingestion Feed")
weather_col1, weather_col2, weather_col3 = st.columns(3)
weather_col1.metric("Precipitation Rate", "18.4 mm/hr", "Heavy Rain Alert")
weather_col2.metric("Drain Water Level", "78%", "Rising (+12%/hr)")
weather_col3.metric("Predicted Overflow Time", "2 hrs 15 mins", "Evacuation Window")