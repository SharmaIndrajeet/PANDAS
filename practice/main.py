import pandas as pd    

"""
----> DATA CLEANNING % 
"""
df =pd.read_csv("pokyData.csv")

def remove_column(df):
    # removing irrevelent colunms from data 
    df = df.drop(columns =["Legendry"])

def removee():
    # handeling missing data and rop them 
    df = df.dropna(subset=["Type2"])
    print (df)

def addValue(df):
    #filling all unavailable vlaues 
    df = df.fillna({"Type2" : "Laundiyabazz"})
    print (df)

def changeInstance(df):
    # changing the instance value of a element in place
    df["Type1"] = df["Type1"].replace("Grass", "GRASS")
    print (df)

def changeCase(df):
    # standarized a text of element by changing a case of any text
    df["Name"] = df["Name"].str.upper()
    print (df)

def fixDataType(df) : 
    # change a data type of a column 
    df["Legendry"] = df["Legendry"].astype(int)
    print (df)


def remove_dublicate(df):
    # remove dublicate vlaues from the data or drop them 
    df = df.drop_duplicates()
    print (df)


"""
AGGRIGATE FUNCTION OF PANDAS --- > 
"""

def get_numerical(df):
    # get the sum of all numerical values  column wise
    print ("sum : " , df.sum(numeric_only=True))

    # get mean 
    print (df.mean(numeric_only= True))

    #get minimum 
    print (df.min(numeric_only=True))

    # get maximum
    print (df.max(numeric_only=True))

    # we can count the  number of element of different column 
    print (df.count())


# this fuction do exactily what upper function do but for a single column 
def  get_single_vlaue(df):

    # sum 
    print (df["Height"].sum())
    
    # mean
    print (df["Height"].mean())

    # minimm
    print (df["Height"].min())

    #maximum
    print (df["Height"].max())

    #count 
    print (df["Type2"].count())

get_single_vlaue(df)