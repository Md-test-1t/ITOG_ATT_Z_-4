import pandas as pd
data = pd.read_csv('data.csv')
average_salary = data['salary'].mean()
employees_over_30 = data[data['age'] > 30]
print(f"Средняя зарплата всех сотрудников: {average_salary:.2f}")
print("Сотрудники старше 30 лет:")
print(employees_over_30[['name', 'age', 'salary']])