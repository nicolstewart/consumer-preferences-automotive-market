"""
Consumer Preferences in the Automative Market

Author: Nicol Stewart

Project:
An exploratory data analysis investigating the relationship between vehicle characteristics, market pricing, and consumer preferences in the used automotive market.

Purpose:
To identify the vehicle characteristics associated with premium pricing and interpret the findings from a consumer behavior and marketing perspective.
"""

#============================================================================================================================================================
# Imports
#============================================================================================================================================================
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Plot Styling
sns.set_style("whitegrid")

# Load dataset
df = pd.read_csv("data/car_price_dataset_medium.csv")


#============================================================================================================================================================
# Initial Dataset Inspection
#============================================================================================================================================================
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.dtypes)

#============================================================================================================================================================
# Summary Statistics
#============================================================================================================================================================
# Summary statistics for categorical columns
print(df.describe(include="str"))

# Unique values and frequency counts
for column in df.select_dtypes(include="str").columns:
    print(f"\n{'-' * 50}")
    print(f"{column}")
    print(f"{'-' * 50}")
    print(df[column].value_counts())

# Looking for missing values
print(df.isnull().sum())

# Looking for duplicate Records
print(df.duplicated().sum())

# Create working dataset
df_clean = df.copy()

#============================================================================================================================================================
# Check numerical ranges
print("-" * 60)
print(df_clean.describe())

#============================================================================================================================================================
# Feature Engineering
#============================================================================================================================================================
# Vehicle age

CURRENT_YEAR = 2026
df_clean["Vehicle_Age"] = CURRENT_YEAR - df_clean["Model_Year"]
print("-" * 60)
print("Vehicle Age:")
print(df_clean[["Model_Year", "Vehicle_Age"]].head())

# Price per horsepower
df_clean["Price_per_bhp"] = (
    df_clean["Price_USD"] /
    df_clean["Max_Power_bhp"]
)
print("Price per Horsepower:")
print(df_clean[["Price_USD", "Max_Power_bhp"]].head())

# Classifying into two segments (premium and mass market)
premium_brands = [
    "Audi",
    "BMW",
    "Mercedes"
]

df_clean["Brand_Segment"] = df_clean["Brand"].apply(
    lambda brand: "Premium"
    if brand in premium_brands
    else "Mass Market"
)

# Grouping Vehicles based on their mileage
df_clean["Mileage_Category"] = pd.cut(
    df_clean["Kilometers_Driven"],
    bins=[0, 50000, 100000, 150000, 200000],
    labels=[
        "Low",
        "Moderate",
        "High",
        "Very High"
    ]
)

# Inspecting new dataset
print(df_clean.head())
print(df_clean.info())


# Saving clean dataset
df_clean.to_csv(
    "data/used_car_dataset_clean.csv",
    index=False
)