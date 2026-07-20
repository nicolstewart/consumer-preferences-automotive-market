# Data Quality Report 

## Project
Consumer Preferences in the Automative Market

## Dataset Overview
| Metric | Value |
|---------|------:|
| Number of Rows | 1000 |
| Number of Columns | 12 |
| Missing Values | 0 |
| Duplicate Records | 0| 

The dataset contains information on 1000 used vehicles from 10 automotive brands. 

## Variables
### Numerical Variables 
| Variable | Description |
|-----------|-------------|
| Car_ID | Unique vehicle identifier |
| Model_Year | Manufacturing year |
| Kilometers_Driven | Total distance travelled |
| Engine_CC | Engine capacity (cc) |
| Max_Power_bhp | Maximum engine power |
| Mileage_kmpl | Fuel efficiency (km/L) |
| Seats | Number of seats |
| Price_USD | Vehicle selling price |

### Categorical Variables

| Variable | Description |
|-----------|-------------|
| Brand | Vehicle manufacturer |
| Fuel_Type | Petrol, Diesel, Hybrid or Electric |
| Transmission | Manual or Automatic |
| Owner_Type | First, Second or Third owner |

---
## Initial Observations

Several characteristics make this dataset well suited for analysing consumer preferences within the used automotive market:

- The dataset contains information from **10 different vehicle manufacturers**, allowing comparisons between brands.
- Four fuel types are represented (Petrol, Diesel, Hybrid and Electric), enabling analysis of fuel preferences.
- Both Manual and Automatic transmissions are included, allowing investigation into transmission preferences.
- Owner history (First, Second and Third owner) provides an opportunity to examine how ownership history may relate to resale price.
- Multiple numerical variables (engine size, horsepower, mileage, vehicle age and price) enable correlation and pricing analyses.

## Data Quality Assessment

Overall data quality is **excellent**.

Strengths include:

- Complete dataset
- No duplicate observations
- Appropriate data types
- Balanced representation across several categorical variables
- Sufficient numerical variables for statistical analysis

No immediate data cleaning is required prior to exploratory data analysis.

Future feature engineering may include:

- Vehicle Age
- Price per Horsepower
- Price per Engine Capacity
- Mileage Category
- Premium vs Economy Brand Classification