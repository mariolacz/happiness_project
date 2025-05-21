import pandas as pd
import os

csv_files = [
    '/Users/mariolaczajkowska/Desktop/data_hapiness/2018.csv',
    '/Users/mariolaczajkowska/Desktop/data_hapiness/2019.csv'
]

for file in csv_files:
    cols = pd.read_csv(file, nrows=0).columns.tolist()
    print(f"\n{file} → {cols}")

common_cols = set(pd.read_csv(csv_files[0], nrows=0).columns)
for file in csv_files[1:]:
    common_cols &= set(pd.read_csv(file, nrows=0).columns)

print(f"\nCommon columns: {common_cols}")

#added only common columns and add additional column year
df_list = []
for file in csv_files:
    year = int(os.path.basename(file)[:4])
    temp_df = pd.read_csv(file, usecols=common_cols)
    temp_df['Year'] = year
    df_list.append(temp_df)

# csv's connection
df = pd.concat(df_list, ignore_index=True)

df = df.rename(columns={'Country or region': 'Country'})
df['Year'] = df['Year'].astype(int)

print("\nMissing values:")
print(df.isnull().sum())

#saved to the new file
output_folder = '/Users/mariolaczajkowska/happiness_data/new_data'
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, 'happiness_cleaned.csv')
df.to_csv(output_file, index=True)

print(f"\nCleaned data saved to: {output_file}")