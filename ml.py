import pandas as pd
df = pd.read_csv('employee.csv')
print("Employee salary Data:")
print(df)

average_salary = df['Salary'].mean()
print("\nAverage Salary:", average_salary)

print(df[(df['Age']>30) & (df['Department']=='Engineering')])