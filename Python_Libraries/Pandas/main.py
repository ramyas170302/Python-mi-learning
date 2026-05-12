import pandas as pd

#Load
df=pd.read_csv("s.csv")


'''print("Top 5")
print(df.head(5))
print("\n")

print("Bottom 5")
print(df.tail(5))
print("\n")

print("number of rows and columns")
print(df.shape) # (rows,columns)

print("\ninfo")
df.info() # information

print("\n Describe")
print(df.describe())# mean,max,min,std(stastical summary)

print("\n colums:")
print(df.columns)

#filter using loop
print("\n Filter")
rows=[]
for i in range(len(df)):
    if df.loc[i,"Marks"] > 80:
        rows.append(df.loc[i,["Name","Marks"]])

print(pd.DataFrame(rows)) 
print("\n") 

# using condition

print("filter using condtion")
print(df.loc[df["Marks"]>80,["Name","Marks"]])

# update using loop
print("\nUsing loop")
for i in range(len(df)):
    if df.loc[i,"Marks"]<80:
        df.loc[i,"Marks"]=80
print(df)

#using loc new column
print("\n New column with update")
df["st"]=df.loc[df["Marks"]<80,"Marks"]=80
print(df)

#sort
print("\nsorting")
sort=df.sort_values(by=["Department","Marks"],ascending=[True,False])
print(sort.loc[:,["Name","Marks","Department"]])

print(df[df["Name"].str.contains("ram",case=False)])


# query Function 
df.query("Marks>80 and Department=='CSE'")

# delete particular field
dele=df.drop("Department",axis=1)
print(dele)

#copying
df3=df.copy()
df2=df
df2["Marks"]=80
print(df2) #change
print("\n")
print(df) # change in df2 reflects df
print("\n")
print(df3) # make change in df2 or df do not effect (copied)

# copy,modify
df3=df.copy()
print(df3["Name"].str.split(''))'''


#merging  and concatenation
df3=df[["Name","Marks"]]  # two brackets because that is 2d
df2=df[["Department","Name"]]
fin=pd.merge(df3,df2,on="Name",how="Inner") # merging pd.merge(df1,df2,on="common field",how="X")  x="Inner,Outer,Left,right"
print(fin)
res=pd.concat([df3,df2],ignore_index=True) # concatenate pd.cancat([df1,df2],ignore_index=true)
print(res)



