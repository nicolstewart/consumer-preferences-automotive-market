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










