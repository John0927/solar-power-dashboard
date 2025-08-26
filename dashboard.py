import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("🔆 Solar Power Monitoring Dashboard")

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("E:/Solar Project/credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("SolarDashboard").sheet1

# Fetch data
data = sheet.get_all_records()
df = pd.DataFrame(data)
st.write("Columns in DataFrame:", df.columns.tolist())  
# Layout
col1, col2 = st.columns(2)
with col1:
    st.subheader("📈 Voltage & Current Over Time")
    st.line_chart(df[['Voltage', 'Current']])
with col2:
    st.subheader("⚡ Efficiency Trend")
    st.bar_chart(df['Efficiency'])

st.subheader("📋 Raw Data Table")
st.dataframe(df)