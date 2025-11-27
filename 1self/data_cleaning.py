import pandas as pd    


"""
---->  data cleaning is a process of fixing / removing incompleate , incorrect data ~75% of work
of pandas is with data cleaning
"""
df = pd.read_csv("pokyData.csv")

# # how to dtrop irrevelent column ---> 
# df = df.drop(columns=["Legendry"])
# print (df)
# # handel missing data 
# df = df.dropna(subset=["Type2"])

# # filling all not available vlaues 
# df = df.fillna({"Type2" : "Laudiyabazz"})
# print(df.to_string())\

# # can chage a instance of any element
# df["Type1"] = df["Type1"].replace({"Grass" : "GRASS"})
# print (df)

# # standerizd our text 
# df["Name"] = df["Name"].str.lower()
# print (df)

# # fix data types 
# df["Legendry"] = df["Legendry"].astype(bool)
# print (df)

# remove dublicate values 
print (df)

df = df.drop_duplicates()
print (df)