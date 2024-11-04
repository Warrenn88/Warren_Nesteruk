import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "C:\\Users\\Warren\\Desktop\\hotaling_cocktails - Cocktails.csv"
df = pd.read_csv(file_path)
def data_types():
    print(df.dtypes)

def null_check():
    print("\nMissing values per column:")
    print(df.isnull().sum())

def duplicate_boolean_check(df, column_name):
    duplicates_in_column = df[column_name].duplicated().any()
    print(f"Duplicates in the {column_name} column: ", duplicates_in_column)

def duplicate_identify(df, column_name):
    duplicate_entries = df[df[column_name].duplicated(keep=False)]
    print(f"Duplicate entries in the {column_name}: \n", duplicate_entries)

def remove_duplicate_rows_by_column(df, column_name):
    result = df.drop_duplicates(subset=[column_name])
    return result

def total_duplicate_check ():
    result = df.duplicated().any()
    print(f"Any duplicate data in the set? {result}")

def column_length_check(df, column_name):
    result = df[column_name].count()
    print(f"The length of column {column_name} is {result}")

def reset_dataframe_index(df):
    return df.reset_index(drop=True)

def dataframe_to_numpy_array(df):
    return df.to_numpy()

data_types()
null_check()
duplicate_boolean_check(df,'Cocktail Name' )
duplicate_boolean_check(df,'Ingredients')
duplicate_identify(df, 'Cocktail Name')
duplicate_identify(df, 'Ingredients')
df = remove_duplicate_rows_by_column(df, 'Cocktail Name')
df = remove_duplicate_rows_by_column(df, 'Ingredients')
df = df[['Cocktail Name','Ingredients']]
null_check()
total_duplicate_check()
column_length_check(df, 'Cocktail Name')
column_length_check(df, 'Ingredients')
df = reset_dataframe_index(df)
print(df)
df = dataframe_to_numpy_array(df)
print(df)
