import pandas as pd   
import numpy as np   

# print ("hello")

# d= {'one': pd.Series([1,2,3] , index= ['a' , 'b' , 'c']),
#     'two': pd.Series([1,2,3,4] , index= ['a' , 'b' , 'c' , 'd']),}


# df = pd.DataFrame(d)
# df['three'] = pd.Series([1,2,3] , index= ['a' , 'b' , 'c'])

# print (df)
# print ("adding new col")
# df['four'] = df['one'] + df['three']
# print (df)

# deleating ----> 
"""
# through del function
del df['one']

#through pop function
df.pop('three')
print (df)
"""

# row selection ---> 

df = pd.DataFrame({'Age' : [30 , 20 , 22],
                   'Colour':[ 'blue' , 'red' , 'black'],
                   'Food': ['mango' , 'poty' , 'BlackBerry'],
                   'height' :[167 , 189 , 10],
                   'Score' :[22 , 44  , 66 ]},
                   
                   index = ['Indrajeet' , 'Rishu' , 'Rishav'])

print (df.loc['Rishav'])



