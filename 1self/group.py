import pandas as pd

df = pd.read_csv("pokyData.csv" , index_col="Name")

group = df.groupby("Type1")

print (group["Height"].sum())

#print (group["Height"].sum())


#we can perform all activity all agrigate for a single gropu