import pandas as pd


data=pd.read_csv("students.csv")
print(data)  # dataFrame

print(data.isnull().sum())  # checking number of null values in each column
filter=data.copy()
filter["Marks"]=filter["Marks"].fillna(filter["Marks"].mean())  #replace Nan marks
filter["Department"]=filter["Department"].fillna("Unknow")  #replace Null department values
filter["Attendance"]=filter["Attendance"].fillna(filter["Attendance"].mean())   # replace Nan value of Attendance
print(filter.isnull().sum())  #to check is all the null values clear in the all the field

print(filter)  #final null cleared dataframe
print("\n")
change=filter.query("Marks>80 and Attendance>85")
print(change)
print("\n")
sort=filter.sort_values(by=["Department","Marks"],ascending=[True,False])
print(sort[["Name","Department","Marks"]])

print("\n")
print("Number of students:",len(filter))
print("\naverage marks:",round(filter["Marks"].mean(),2))
ma_sort=filter.sort_values(by="Marks",ascending=False)
topper=ma_sort.iloc[0]
print("\n🏆 College Topper:",topper["Name"],"(",topper["Marks"],")")

print("\nAverage of each marks of department")
print(round(filter.groupby("Department")["Marks"].mean(),2))





 
