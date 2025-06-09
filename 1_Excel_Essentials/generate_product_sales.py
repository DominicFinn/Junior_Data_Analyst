# Data Analysis with Python
# Generate Product Sales Data for Excel Essentials

# This script generates a CSV file with product sales data for each month, region, and country.
# It uses the regions and products defined in the code, and generates data for each combination.
# The data is saved to a CSV file in the same directory as the script.

import pandas as pd
import numpy as np
from datetime import datetime
import calendar

# Define regions and countries
regions = {
    'EMEA': ['United Kingdom', 'Germany', 'France'],
    'APAC': ['Japan', 'Australia', 'Singapore'],
    'AMAR': ['United States', 'Canada', 'Mexico']
}

# Define products and their introduction dates
products = {
    'LocoTrack HGD4': {'intro_date': '2020-01', 'type': 'cash_cow'},
    'LocoTrack HGR4': {'intro_date': '2020-01', 'type': 'cash_cow'},
    'LocoTrack HGP4': {'intro_date': '2020-01', 'type': 'cash_cow'},
    'LocoTrack HFR4': {'intro_date': '2020-01', 'type': 'cash_cow'},
    'LocoTag P4P': {'intro_date': '2020-01', 'type': 'dog'},
    'LocoTag E4BL': {'intro_date': '2021-01', 'type': 'star'},
    'LocoTag C2PL': {'intro_date': '2022-01', 'type': 'problem_child'},
    'LocoPoint': {'intro_date': '2024-01', 'type': 'star'},
    'LocoCard E1BL': {'intro_date': '2025-01', 'type': 'star'}
}

# Generate date range
start_date = '2020-01'
end_date = '2025-12'
date_range = pd.date_range(start=start_date, end=end_date, freq='M')

# Initialize empty lists for data
data = []

# Generate data for each combination
for date in date_range:
    year = date.year
    month = date.strftime('%b')
    
    for region, countries in regions.items():
        for country in countries:
            for product, details in products.items():
                # Skip if product hasn't been introduced yet
                intro_date = datetime.strptime(details['intro_date'], '%Y-%m')
                if date < intro_date:
                    continue
                
                # Calculate base units based on product type and region
                base_units = {
                    'cash_cow': 1000,
                    'star': 800,
                    'problem_child': 200,
                    'dog': 100
                }[details['type']]
                
                # Apply regional multipliers
                region_multiplier = {
                    'EMEA': 1.0,
                    'APAC': 0.8,
                    'AMAR': 0.9
                }[region]
                
                # Calculate growth factor based on months since introduction
                months_since_intro = (date.year - intro_date.year) * 12 + date.month - intro_date.month
                growth_factor = 1 + (months_since_intro * 0.02)  # 2% monthly growth
                
                # Apply product-specific adjustments
                if product == 'LocoTrack HGD4':
                    growth_factor *= 1.2  # 20% higher growth
                elif product == 'LocoTag C2PL':
                    growth_factor *= 0.8  # 20% lower growth
                
                # Calculate final units and revenue
                units = int(base_units * region_multiplier * growth_factor)
                revenue = units * 100  # Assuming $100 per unit
                
                # Add to data list
                data.append({
                    'Month': month,
                    'Year': year,
                    'Region': region,
                    'Country': country,
                    'Product': product,
                    'Units_Sold': units,
                    'Revenue': revenue
                })

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('1_Excel_Essentials/product_sales_month_region_complete.csv', index=False) 