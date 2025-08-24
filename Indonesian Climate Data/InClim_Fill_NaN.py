import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split

# This script imputes missing climate station data using IterativeImputer and saves completed station datasets

# Load the original climate dataset
df = pd.read_csv("climate_data.csv")

# Get a list of station IDs based on frequency of occurrence
station_id_list = df["station_id"].unique()

# Loop through each station dataset
for sid in station_id_list:
    try:
        # Load the pre-cleaned CSV file for the current station
        df = pd.read_csv(f'station_datasets/station_{sid}.csv')

        # Select only the columns with data I want to fill in
        imputedf = df[["min_temp", "max_temp", "avg_temp", "avg_humidity",
                       "sunshine", "max_wind", "wind_dir_at_max", "avg_wind"]]

        # Split the data into training and testing sets (80% / 20%)
        traindf, testdf = train_test_split(imputedf, test_size=0.2)

        # Initialize IterativeImputer (multi-variate imputation method)
        imp = IterativeImputer(max_iter=50, random_state=0)

        # Fit imputer on the full dataset (learn imputation model)
        imp.fit(imputedf)

        # Impute missing values for the training set and round to 1 decimal
        traindf_imp = pd.DataFrame(np.round(imp.transform(traindf), 1),
                                   columns=traindf.columns)

        # Impute missing values for the test set and round to 1 decimal
        testdf_imp = pd.DataFrame(np.round(imp.transform(testdf), 1),
                                  columns=testdf.columns)

        # Impute missing values for the complete dataset
        compdf = pd.DataFrame(np.round(imp.transform(imputedf), 1),
                              columns=imputedf.columns,
                              index=imputedf.index)

        # Replace the original columns in df with the imputed values
        df.loc[compdf.index, compdf.columns] = compdf

        # Save the completed dataset to a new folder
        df.to_csv(f'station_ds_complete/station_{sid}.csv', index=False)

    except Exception as e:
        # If any error occurs (e.g., missing file or corrupted data), print message
        print(f"Error in DS {sid}: {e}")




