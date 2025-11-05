import pandas as pd

marks = [80, 90, 85]
series = pd.Series(marks, index = ['phy', 'Maths', 'chem'])


print(series)
print("Mean of marks is: ", series.mean())
print("Maximum marks: ", series.max())
print("Minimum Marks: ", series.min())


data ={
    'name':['Snehal', 'Sanika', 'Om', 'Vishal', 'Athrv'],
    'age' :[20, 22, 19, 21, 20],
    'marks':[86, 90, 89, 75, 95]
}

df = pd.DataFrame(data)
print(df)

print(df['name'])
print(df['name'], ['marks'])
print(df.iloc[0])
print(df.loc[2])

df['grade'] =['B', 'A', 'A', 'B', 'A+']
print(df)

print("Average marks: ", df['marks'].mean())
print("Sorted by Marks: ", df.sort_values('marks', ascending=False))