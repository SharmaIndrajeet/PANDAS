import pandas as pd   
df = pd.read_csv("data.csv")

#converting the date time from object to int64
# here error is for handeling alter values 
df["date"] = pd.to_datetime(df["date"] , errors="coerce")
df = df.set_index("date")

# to excess what you want day \ month \ year
#print (df["date"].dt.day)

# we can change the formate of a date = "%d-%m-%y"

# filter using  date
print (df[df["date"] > "25-01-2023"])

#resampelling ("monthely" - "weekly"  "daily")

monthely_avg= df.resample("M")["temperature"].mean()
print (monthely_avg)