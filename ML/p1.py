from sklearn.linear_model import LinearRegression

model=LinearRegression()   # create model
x=[[2],[4],[6],[8]]        #input
y=[10,20,30,40]            #output

model.fit(x,y)              #train model
prediction=model.predict([[3]])   #predict - gives in an array
print(prediction[0])                #give me first index

