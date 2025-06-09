import pandas as pd
import random
from datetime import datetime, timedelta

# Define the data
devices = [
    "LocoTrack HGD4",
    "LocoCard E1BL",
    "LocoTrack HFR4"
]

customers = [
    "Emerald Logistics",
    "Super QuickSite",
    "Newbridge Overwatch Services",
    "Naas Supply Chain Systems",
    "DAS",
    "Cobra Tech"
]

# Generate random orders
orders = []
start_date = datetime(2025, 3, 1)
end_date = datetime(2025, 3, 31)

# Generate 2-5 orders per day
for day in range(31):
    current_date = start_date + timedelta(days=day)
    num_orders = random.randint(2, 5)
    
    for _ in range(num_orders):
        order = {
            'Order number': f'ORD-{current_date.strftime("%Y%m%d")}-{random.randint(1000, 9999)}',
            'Customer': random.choice(customers),
            'Device Model': random.choice(devices),
            'Date': current_date.strftime('%Y-%m-%d'),
            'Total': round(random.uniform(1000, 5000), 2)
        }
        orders.append(order)

# Create DataFrame and save to CSV
df = pd.DataFrame(orders)
df.to_csv('1_Excel_Essentials/march_2025_orders.csv', index=False)
print("CSV file has been generated successfully!") 