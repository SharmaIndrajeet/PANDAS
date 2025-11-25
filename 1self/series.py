import numpy as np  
import pandas as pd  

data = [1,2,3]
# we can create a index value also by using index command
ser = pd.Series(data , index = ['a' , 'b' , 'c'])
print (ser)

# access a single element through idx
print (ser.loc['a']) 

# access a single vlaue through a idx vlaue 
print (ser.iloc[1])

#couple of operation which we can perform in array using pandas 
print (ser[ser > 2])