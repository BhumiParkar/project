import pandas as pd
data = pd.read_csv('C:/Users/admin/Downloads/data.csv')
df = pd.DataFrame(data)
avg = df['Pulse'].mean()
print(df['Pulse'].fillna(avg))
