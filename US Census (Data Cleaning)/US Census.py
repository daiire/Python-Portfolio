import pandas as pd
import glob
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# The data I am working with comes in 9 seperate CSV files named 'states' with a sequencial number following it.
# Each file contains 6 rows of data with an idenical column structure. As such, I will need to use glob to
# import the files and concatinate them into a single database
files = glob.glob('Raw Data CSVs/states*.csv')

df_list = []
for file in files:
    data = pd.read_csv(file)
    df_list.append(data)
df = pd.concat(df_list)

# Altering the columns to get a uniform case convention.
df.columns = df.columns.str.lower()

# Upon viewing the dataframe, notice there are a few duplicate rows.
#print(df)
df = df.drop_duplicates().reset_index(drop=True)

# I sum the null values to identify any possible issues. 'pacific' produces 4 total null values. This is attributed
# to there being fewer than 0.01% Pacific peoples living in the state. As such, I have decided to replace the null
# values with 0
#print(df.isnull().sum())
df['pacific'] = df.pacific.fillna(float(0))

# There is a column named 'genderpop' which contains values like '415644M_456415F'. This signifies there are
# 415644 males and 456415 females. I wish to split this data into their own columns, 'male_pop' and 'female_pop' respecively.
df['male_pop'] = (df.genderpop.str.split(r'(\d+)', expand = True)[1]).astype("int64")

# Upon further inspection, some rows do not have any data for female population, e.g: '415644M_F'. To remedy this, I have
# subtracted the 'male_pop' column from the 'total_pop' column.
df['female_pop'] = df['totalpop'] - df['male_pop']

# The 'income' and ethnicity columns contain commas and signs that make it awkward to work with. In order to get the
# data into a workable configuration, I removed unwanted characters using a lambda function along with the translate()
# and strip() methods.
df["income"] = df["income"].apply(lambda x: x.translate(str.maketrans('', '', '$,'))).astype("float")

cols_to_strip = ["white", "hispanic", "black", "native", "asian", "pacific"]
df[cols_to_strip] = df[cols_to_strip].apply(lambda x: x.str.strip("%")).astype("float")

# As 'genderpop' is now obsolete, and 'unnamed: 0' served no purpose, these columns can be removed.
df = df.drop(["unnamed: 0", "genderpop"], axis = 1)

# Renamed totalpop and income to fit the naming convention and better explain the values in the column.
df = df.rename(columns = {"totalpop": "total_pop", "income": "avg_income", "white": "white_%", "hispanic": "hispanic_%",
                          "black": "black_%", "native": "native_%", "asian": "asian_%", "pacific": "pacific_%"})

# Re-ordered the columns.
cols = ["state", "total_pop", "male_pop", "female_pop", "white_%", "hispanic_%", "black_%", "native_%", "asian_%",
        "pacific_%", "avg_income"]
df = df[cols]

print(df.head())
print(df.dtypes)



based = (df["male_pop"] < df["female_pop"]).sum()

print(based)