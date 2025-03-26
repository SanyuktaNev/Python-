import pandas as pd

data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age'  : [25, 30, 22, 35, 28],
    'City' : ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Seattle']
}
df = pd.DataFrame(data)
print(df, end='\n\n')

print(df[['Name', 'Age']], end='\n\n')
print(df[df['Age'] > 25], end='\n\n')

df['Gender'] = ['F', 'M', 'M', 'M', 'F']
print(df, end='\n\n')
grouped_data = df.groupby('Gender')['Age'].mean()
print(grouped_data, end='\n')