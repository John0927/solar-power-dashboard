import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import time

# Setup Google Sheets connection
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("E:/Solar Project/credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("SolarData").sheet1

# Simulate and log data
def log_data():
    while True:
        voltage = round(random.uniform(15.0, 20.0), 2)
        current = round(random.uniform(1.0, 5.0), 2)
        efficiency = round((voltage * current / 100.0) * 100, 2)

        sheet.append_row([voltage, current, efficiency])
        print(f"Logged: {voltage} V | {current} A | {efficiency} %")
        time.sleep(2)

log_data()