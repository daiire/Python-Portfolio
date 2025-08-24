import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

main_df = pd.read_csv("climate_data.csv")
station_id_list = main_df["station_id"].unique()

for sid in station_id_list:
    try:
        df = pd.read_csv(f"station_datasets/station_{sid}.csv")
        print(f"\n\n station_{sid}\n",df.isnull().sum()/len(df)*100)
    except: print("Error in DS {}\n\n\n".format(sid))
