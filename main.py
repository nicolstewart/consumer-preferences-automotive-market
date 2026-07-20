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
# Initial Dataset Insepction
#============================================================================================================================================================
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())