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

# Choose a random day for Emerald Logistics spike
emerald_spike_day = random.randint(5, 25)  # Avoid first and last few days

# Generate 2-5 orders per day
for day in range(31):
    current_date = start_date + timedelta(days=day)
    is_monday = current_date.weekday() == 0  # 0 is Monday
    
    # Base number of orders
    num_orders = random.randint(2, 5)
    
    for _ in range(num_orders):
        # Determine customer based on rules
        if is_monday:
            customer = "Cobra Tech"
        elif day == emerald_spike_day:
            # 80% chance of Emerald Logistics on spike day
            customer = "Emerald Logistics" if random.random() < 0.8 else random.choice([c for c in customers if c != "Cobra Tech"])
        else:
            # Weight the customers
            weights = {
                "Newbridge Overwatch Services": 0.4,  # High weight
                "Naas Supply Chain Systems": 0.05,    # Low weight
                "Emerald Logistics": 0.05,           # Low weight
                "Super QuickSite": 0.2,              # Medium weight
                "DAS": 0.2,                         # Medium weight
                "Cobra Tech": 0.1                    # Medium weight (only applies on Mondays)
            }
            # Remove Cobra Tech from weights if not Monday
            if not is_monday:
                del weights["Cobra Tech"]
                # Normalize remaining weights
                total = sum(weights.values())
                weights = {k: v/total for k, v in weights.items()}
            
            customer = random.choices(list(weights.keys()), weights=list(weights.values()))[0]
        
        order = {
            'Order number': f'ORD-{current_date.strftime("%Y%m%d")}-{random.randint(1000, 9999)}',
            'Customer': customer,
            'Device Model': random.choice(devices),
            'Date': current_date.strftime('%Y-%m-%d'),
            'Total': round(random.uniform(1000, 5000), 2)
        }
        orders.append(order)

# Create DataFrame and save to CSV
df = pd.DataFrame(orders)
df.to_csv('1_Excel_Essentials/march_2025_orders.csv', index=False)
print("CSV file has been generated successfully!") 