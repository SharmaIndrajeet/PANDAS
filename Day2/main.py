import pandas as pd  
import numpy as np  

# print ("helo")
# s = pd.Series(5 , index=[0,1,2,3])
# print (s)

# s = pd.Series([1,2,3,4,5] , index = ['a' , 'b' , 'c' , 'd' , 'e'])
# print (s['b'])


"""
--> Data Frames 
"""

# df = pd.DataFrame()
# print (df)

# data = [1,2,3,4,5]
# df = pd.DataFrame(data)
# print (df)

# data = {'Name':['Tom' , 'Jerry' , 'Rishav'], 'age':[28 , 34 , 67]}
# df  = pd.DataFrame(data)
# print (df)


# data = [{'A' : 1,  'B':2 , 'C' : 23} , {'A' :5, 'B' : 10 , 'C':20} , {'A' :5, 'B' : 10 , 'C':20}]

# pd = pd.DataFrame(data)
# print (pd)

# d= {'one' : pd.Series([1,2,3] , index=['a' , 'b' , 'c'])
#     'two' }


#data = {'Name' :['Rishav' ,'Kalwa' , 'Rishu' , 'KalwaPro' , 'Indrajeet'] , 'Physics' :[90 , 60 , 78 , 89 , 100] , 'Chemistry':[45 , 67, 89, 65, 100] , 'Computer':[56 ,78 , 65, 76, 100] , 'Maths' : [54 , 65, 76, 87, 90] , 'Hindi' :[34, 56, 87, 98, 90]}
data = np.random.randint(60 , 100,(5 , 5))
df = pd.DataFrame(data , index = ['Indrajeet' , 'Rishav' , 'Kalwa' , 'KalwaPro' , 'Rishu'] , columns = ['Math' , 'Chemistry' , 'Physics' , 'Computer' , 'English'])
print(df)


