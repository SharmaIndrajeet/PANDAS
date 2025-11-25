import numpy as np   
import pandas as pd   

data = {
    "Name" : ["Indrajeet" , "Kalwa" , "Chutiya"],
    "Age"  :[23 , 54 , 65]
}

df = pd.DataFrame(data , index = ["Player 1" , "Player 2" , "Player 3"])

# add a new column 
df["Job"] = ["Cook" , "Nan" , "Security"]

# add a new row  
new_row = pd.DataFrame([{"Name":"Priyanshu" , "Age" :"24" , "Job" : "Engineer"}] , index = ["Player 4"])
df = pd.concat([df , new_row])

print (df)