# Import the libraries and modules we need
import pandas as pd

df = pd.read_csv('/workspaces/nola/Code_Enforcement_Active_Pipeline_20260311.csv')
print(df.columns)

# filter to one zipcode
df1 = df[df['Zipcode'] == 70117]
print(df1.head())

cols_delete = ['GeoPIN', 'XPos', 'YPos','PointLocation']
df1=df1.drop(columns=cols_delete)
print(df1.head())

