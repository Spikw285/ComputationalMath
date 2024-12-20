import pandas as pd

# Предположим, это твой исходный DataFrame
results_table = "utilities/results"

# Вставь сюда улучшенный код форматирования
for column in ["Newton-Raphson", "Bisection", "Secant", "Iteration"]:
    results_table[column] = results_table[column].apply(lambda x: eval(x))  # Конвертация строки в словарь
    results_table[f"{column}_root"] = results_table[column].apply(lambda d: d.get('root'))
    results_table[f"{column}_iterations"] = results_table[column].apply(lambda d: d.get('iterations'))
    results_table[f"{column}_message"] = results_table[column].apply(lambda d: d.get('message'))
    results_table.drop(columns=[column], inplace=True)

# Сохранение очищенной таблицы в Excel
results_table.to_excel("results_cleaned.xlsx", index=False)
print("Результаты сохранены в файл results_cleaned.xlsx")
