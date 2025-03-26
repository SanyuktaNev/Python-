#NumPy
#1. Weather Forcasting
#2.Use case : handling and analysing large data sets from weather sensor and satellites

import numpy as np 


'''temp = np.array([1,2,3,4,5,6,7])
output=np.mean(temp)

df=pd.read_csv('project.csv') 
print(output)'''

import pandas as pd 
#sorted_df=df.sort_values(by='STATUS',ascending=False)
#deleted_df=df = df.drop(columns=['Period'])
#df['Series_reference']=df['Series_reference'].str.lower()
#print(df)

#print(sorted_df)
import matplotlib.pyplot as plt
#line plot
'''x=[1,2,3,4,5,6]
y=[2,4,6,8,10,12]
'''
'''plt.plot(x,y)

plt.title('simpal line points')
plt.xlabel('X-axis')
plt.ylabel('y-axis')

plt.show()
'''

#bar graph
'''plt.figure(figsize=(8, 5))  # Set the figure size (optional)
plt.bar(x, y, color='g', alpha=0.7, label='Data Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Plot Example')
plt.legend()
plt.grid(True)
plt.show()'''

#pie graph
'''label=['a','b','c','d']
size=[30,43,75,23]
color=['red','blue','yellow','green']
explode=[0.1,0,0,0]

plt.pie(size,explode=explode,labels=label,colors=color,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title('fruit distribution')
plt.show()'''

import seaborn as sns

'''
# Define data
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 6, 8, 10, 12]

# Create line plot
sns.lineplot(x=x, y=y)
plt.title("Line Plot Example")
plt.show()'''
