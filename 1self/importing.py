import pandas as pd   
import numpy as np   

df = pd.read_csv("pokyData.csv" , index_col="Name")

def getNme():
    pokymon = input("Enter your Pokymon Name : ")

    try :
       print (df.loc[pokymon])

    except KeyError :
       print (f"{pokymon} not found")



# it will display the trancit version of data --> firts 5 and end 5
#print (df)

# to display the whole data --> 
#print (df.to_string())

# accessing through column 
#print (df[["Name"]])

# # accessing through row/s   --> we can also use slicing 
# print (df.loc["Bulbasaur" :"Wartortle" , ["Height" , "Weight"]])

# # can perform slicing  start : end : gap , start col : end col
# print (df.iloc[0 : 5 : 2 , 0:3])

"""
----> FILTRING 
"""

tallPoky = df[df["Legendry"] == True] 
print (tallPoky)