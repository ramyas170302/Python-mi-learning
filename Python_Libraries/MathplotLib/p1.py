import matplotlib.pyplot as plt
import numpy as np
'''x=np.array([1,6,2,3])
y1=np.array([20,30,40,50])
y2=np.array([10,30,10,1])
style=dict(
    marker="*",
    markersize=10,
    markerfacecolor="red",
    markeredgecolor="red",
    linestyle="solid",
    linewidth=2,
    
)
plt.xlabel("Year",
           fontweight="bold",
           fontsize=10,
           color="red")

plt.ylabel("Number of student",
           fontweight="bold",
           fontsize=10,
           color="red")

plt.tick_params(axis="both",
            colors="red")

plt.plot(x,y2,color="blue",**style)
plt.plot(x,y1,color="Green",**style)
plt.title("Students",
          fontsize=10,
          fontfamily="italic",
          fontweight="bold"
          )
#plt.xticks(x)

plt.grid(axis="y",
         linewidth=2,
         color="lightgray",
         linestyle="dotted")'''

# bar chat:

'''categories=["grain","Fruits","protein"]
values=[20,30,10]
plt.bar(categories,values)'''

#pie chart

'''categories=["Freshman","Junior","Senior"]
values=[300,200,100]
color=["Blue","Red","Green"]
plt.pie(values,labels=categories,
                autopct="%1.1f%%",
                colors=color,
                explode=[0,0,0.1],
                shadow=True,
                startangle=180)
plt.show()'''


# scatter chart
'''x = [1,2,3,4,5]
boys = [150,155,160,165,170]
girls = [148,152,158,162,166]
plt.title("Height Analysis",size=20,color="Purple")
plt.scatter(x,boys,label="Boys",color="red",s=25,marker="o")
plt.scatter(x,girls,label="Girls",color="Green",s=25,marker="*")
plt.xlabel("students",size=10)
plt.ylabel("height",size=10)
plt.legend()
plt.show()'''


#Histrogram graph

'''a=[1,1,5,2,4]

plt.hist(a,bins=1,color="Blue")
plt.show()'''

#subplot
'''x=np.array([2,5,3,4])
figure,axes=plt.subplots(2,2)
axes [0,0].plot(x,x**1)
axes[0,0].set_title("x**1")
axes[0,1].plot(x,x**2)
axes[0,1].set_title("X**2")
axes[1,0].plot(x,x**3)
axes[1,0].set_title("X**3")
axes[1,1].plot(x,x**4)
axes[1,1].set_title("X**4")
plt.tight_layout()
plt.show()'''




