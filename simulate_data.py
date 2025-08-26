import random
import time

def generate_data():
    while True:
        voltage = round(random.uniform(15.0, 20.0), 2)     # Simulated voltage
        current = round(random.uniform(1.0, 5.0), 2)       # Simulated current
        efficiency = round((voltage * current / 100.0) * 100, 2)  # Efficiency %
        
        print(f"Voltage: {voltage} V | Current: {current} A | Efficiency: {efficiency} %")
        time.sleep(2)  # Wait 2 seconds before next reading

generate_data()