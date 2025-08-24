import pandas as pd
import numpy as np


pd.set_option('display.max_columns', None)
pd.options.display.max_rows = 999

# This script takes care of general data cleaning (renaming columns, removing outliers, etc.) and splits the dataframe
# in order to more effectively fill in missing values with IterativeImputer.

# Load the dataset from a CSV file
df = pd.read_csv("climate_data.csv")

# Rename columns for better readability
df.rename(columns={
    "Tn": "min_temp",
    "Tx": "max_temp",
    "Tavg": "avg_temp",
    "RH_avg": "avg_humidity",
    "RR": "rainfall",
    "ss": "sunshine",
    "ff_x": "max_wind",
    "ddd_x": "wind_dir_at_max",
    "ff_avg": "avg_wind",
    "ddd_car": "most_wind_dir"
}, inplace=True)

# Count how many records exist for each station
sub500_stations = df["station_id"].value_counts()

# Select station IDs that have fewer than 500 records
sub500_stations = sub500_stations[sub500_stations < 500].index

# Remove rows belonging to those stations with fewer than 500 records
df = df[~df["station_id"].isin(sub500_stations)]

# Clean whitespace in the 'most_wind_dir' column (important for categorical values)
df["most_wind_dir"] = df["most_wind_dir"].str.strip()

# Define acceptable ranges (filters) for each variable to remove outliers
outliers = {
    'min_temp': lambda x: x <= 30,  # Minimum temperature capped at 30
    'max_temp': lambda x: x <= 50,  # Maximum temperature capped at 50
    'avg_temp': lambda x: x <= 40,  # Average temperature capped at 40
    'avg_humidity': lambda x: (x >= 60) & (x <= 100),  # Humidity must be between 60–100%
    'sunshine': lambda x: (x > 0) & (x <= 10),  # Sunshine duration between 0–10
    'max_wind': lambda x: (x > 0) & (x < 26),  # Max wind speed between 0–25
    'wind_dir_at_max': lambda x: x <= 360,  # Wind direction (degrees) within compass range
    'avg_wind': lambda x: (x > 0) & (x <= 15),  # Average wind speed between 0–15
    'most_wind_dir': lambda x: x.isin(['E', 'SW', 'NE', 'W', 'N', 'NW', 'S', 'SE'])  # Valid compass directions
}

# Apply outlier filtering: replace invalid values with NaN
for col, outlier in outliers.items():
    df[col] = df[col].where(outlier(df[col]))

# I will handle the missing data using IterativeImputer in a future step.
# For more accurate estimates, the dataframe will be divided by station ID, ensuring imputation is performed within
# each station's data.

# Get list of station IDs and create a for loop to iterate though them
station_id_list = df['station_id'].unique()
for sid in station_id_list:
    station_df = df[df['station_id'] == sid]  # Extract data for a single station

    # Calculate percentage of missing values per column
    missing_percent = station_df.isnull().sum() / len(station_df) * 100

    # If any column has ≥ 85% missing values, flag the station
    if (missing_percent >= 85).any():
        print(f"Issue with station {sid}:\n {missing_percent}%")
    else:
        # Otherwise, save station data as a separate CSV file
        station_df.to_csv(f'station_datasets/station_{sid}.csv', index=False)


