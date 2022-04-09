import pandas as pd

path="age.csv"

data=pd.read_csv(path)
df=pd.DataFrame(data)

x=df.str.split(',')
print(x)