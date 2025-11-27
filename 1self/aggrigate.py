import pandas as pd   
df = pd.read_csv("pokyData.csv" , index_col="Name")

def getAgg ():
    # we can identify the mean of all numerical values 
    print (df.mean(numeric_only=True))

    # we can identify all the sum of numerical values 
    print (df.sum(numeric_only=True))

    # we can identify the minimum value of numerial values 
    print (df.min(numeric_only=True))

    #we can identify the maximum value of numerial values 
    print (df.max(numeric_only=True))

    # we can count the number of element 
    print(df.count()) 

"""
---> Single column aggrigate function 
"""
def getSingle():
    #calculte a single column 
    print (df["Height"].mean())
   
    # sum of all legendary data 
    print (df["Legendry"].sum())

    #we can also do this for minum and maimum of a singlr column 

getSingle()
