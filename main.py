"""
Consumer Preferences in the Automotive Market

Author: Nicol Stewart

Project:
An exploratory data analysis investigating the relationship between vehicle characteristics, market pricing, and consumer preferences in the used automotive market.

Purpose:
To identify the vehicle characteristics associated with premium pricing and interpret the findings from a consumer behaviour and marketing perspective.
"""

#============================================================================================================================================================
# Imports
#============================================================================================================================================================
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Apply a consistent visual style across all figures
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
# Feature Engineering:
#============================================================================================================================================================
# Get vehicle age to analyse depreciation

CURRENT_YEAR = pd.Timestamp.today().year
df_clean["Vehicle_Age"] = CURRENT_YEAR - df_clean["Model_Year"]
print("-" * 60)
print("Vehicle Age:")
print(df_clean[["Model_Year", "Vehicle_Age"]].head())

# Calculate a value-for-money metric
df_clean["Price_per_bhp"] = (
    df_clean["Price_USD"] /
    df_clean["Max_Power_bhp"]
)
print("Price per Horsepower:")
print(df_clean[[
    "Price_USD",
    "Max_Power_bhp"
    "Price_per_bhp"
]].head())

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

# Categorizing based on age
df_clean["Age_Category"] = pd.cut(
    df_clean["Vehicle_Age"],
    bins=[0, 3, 7, 12, 20],
    labels=[
        "New",
        "Recent",
        "Older",
        "Very Old"
    ]
)

# Inspecting new dataset
print(df_clean.head())
print(df_clean.info())


# Save clean dataset
df_clean.to_csv(
    "data/used_car_dataset_clean.csv",
    index=False
)

#============================================================================================================================================================
# Exploratory Data Analysis:
#============================================================================================================================================================
# Brand Distribution
# Which manufacturers have the strongest representation in this market?
plt.figure(figsize=(10, 6))

sns.countplot(
    data=df_clean,
    x="Brand",
    order=df_clean["Brand"].value_counts().index
)

plt.title(
    "Distribution of Vehicles by Brand",
    fontsize=14
)
plt.xlabel("Brand")
plt.ylabel("Number of Vehicles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    "images/brand_distribution.png",
    dpi=300
)
plt.show()

# Fuel Type Distribution
# What fuel types dominate consumer choices?
plt.figure(figsize=(10, 6))

sns.countplot(
    data=df_clean,
    x="Fuel_Type"
)

plt.title(
    "Distribution of Vehicles by Fuel Type",
    fontsize=14
)
plt.xlabel("Fuel Type")
plt.ylabel("Number of Vehicles")
plt.tight_layout()
plt.savefig(
    "images/fuel_type_distribution.png",
    dpi=300
)
plt.show()

# Transmission Preference
# Is the market shifting toward convenience-oriented vehicles?
plt.figure(figsize=(10, 6))

sns.countplot(
    data=df_clean,
    x="Transmission"
)
plt.title(
    "Manual vs Automatic Transmission Distribution",
    fontsize=14
)
plt.xlabel("Transmission Type")
plt.ylabel("Number of Vehicles")
plt.tight_layout()
plt.savefig(
    "images/transmission_distribution.png",
    dpi=300
)
plt.show()

#============================================================================================================================================================
# Pricing Analysis
# Price Distribution
# What does the automative pricing landscape look like?
plt.figure(figsize=(10, 6))

sns.histplot(
    data=df_clean,
    x="Price_USD",
    bins=30,
    kde=True,
)

plt.title(
    "Distribution of Vehicle Prices",
    fontsize=14
)
plt.xlabel("Price (USD)")
plt.ylabel("Number of Vehicles")
plt.tight_layout()
plt.savefig(
    "images/price_distribution.png",
    dpi=300)
plt.show()

# Average Price by Brand
# Which brands command the highest price premiums?
brand_prices = (df_clean
                .groupby("Brand")["Price_USD"]
                .mean()
                .sort_values()
                )
plt.figure(figsize=(10, 6))

brand_prices.plot(
    kind="barh"
)

plt.title(
    "Average Vehicle Price by Brand",
    fontsize=14
)
plt.xlabel("Average Price (USD)")
plt.ylabel("Brand")
plt.tight_layout()
plt.savefig(
    "images/average_price_brand.png",
    dpi=300
)
plt.show()

# Price vs Vehicle Age
# How strongly does vehicle age influence market value?
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df_clean,
    x="Vehicle_Age",
    y="Price_USD",
)

plt.title(
    "Relationship Between Vehicle Age and Price",
    fontsize=14
)
plt.xlabel("Vehicle Age")
plt.ylabel("Price USD")
plt.tight_layout()
plt.savefig(
    "images/age_vs_price.png",
    dpi=300
)
plt.show()












