import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Cyber Threat Detection", layout="centered")
st.title("🔐 Insider Threat Detection Dashboard")

with st.form("input_form"):
    st.subheader("Enter Activity Log:")
    login_hour = st.slider("Login Hour", 0, 23, 9)
    files_accessed = st.number_input("Files Accessed", min_value=0, step=1, value=10)
    device_connected = st.selectbox("USB Device Connected", [0, 1])
    submitted = st.form_submit_button("Check Threat")

    if submitted:
        input_data = {
            "login_hour": login_hour,
            "files_accessed": files_accessed,
            "device_connected": device_connected
        }

        try:
            response = requests.post("http://127.0.0.1:5000/predict", json=input_data)
            result = response.json()["threat"]
            st.success(f"🛡️ Threat Status: {result}")
        except Exception as e:
            st.error("❌ Could not connect to backend.")
