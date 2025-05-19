import pandas as pd

csv_files = [
   '/Users/mariolaczajkowska/Desktop/data_hapiness/2018.csv',
    '/Users/mariolaczajkowska/Desktop/data_hapiness/2019.csv'
]

df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=False)

print(df.head())

for file in csv_files:
    df = pd.read_csv(file, nrows=0)  # informion about columns's titles
    print(f"\n{file} → {list(df.columns)}")

    common_cols = set(pd.read_csv(csv_files[0], nrows=0).columns)
for file in csv_files[1:]:
    common_cols &= set(pd.read_csv(file, nrows=0).columns)

df = df.rename(columns={'Country or region': 'Country'})
df = df.round(2)
print(df.isnull().sum())