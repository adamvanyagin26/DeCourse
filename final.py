import csv
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt

# Функция для чтения данных о продажах
def read_sales_data(file_path):
    sales_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            product_name, quantity, price, date = row
            sales_data.append({
                'product_name': product_name.strip(),
                'quantity': int(quantity.strip()),
                'price': float(price.strip()),
                'date': datetime.strptime(date.strip(), '%Y-%m-%d').date()
            })
    return sales_data

# Функция для расчета общей суммы продаж по продуктам
def total_sales_per_product(sales_data):
    total_sales = defaultdict(float)
    for sale in sales_data:
        total_sales[sale['product_name']] += sale['quantity'] * sale['price']
    return total_sales

# Функция для расчета общей суммы продаж по дням
def sales_over_time(sales_data):
    total_sales = defaultdict(float)
    for sale in sales_data:
        total_sales[sale['date']] += sale['quantity'] * sale['price']
    return total_sales

# Чтение данных из файла
file_path = 'sales_data.txt'
sales_data = read_sales_data(file_path)

# Расчет общей суммы продаж по продуктам
product_sales = total_sales_per_product(sales_data)

# Определение продукта с наибольшей выручкой
max_revenue_product = max(product_sales, key=product_sales.get)
print(f"Продукт с наибольшей выручкой: {max_revenue_product} - {product_sales[max_revenue_product]}")

# Расчет общей суммы продаж по дням
daily_sales = sales_over_time(sales_data)

# Определение дня с наибольшей суммой продаж
max_sales_day = max(daily_sales, key=daily_sales.get)
print(f"День с наибольшей суммой продаж: {max_sales_day} - {daily_sales[max_sales_day]}")

# Построение графиков
def plot_sales(data, title, xlabel, ylabel):
    plt.figure(figsize=(10, 5))
    plt.bar(data.keys(), data.values())
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.show()

# График общей суммы продаж по продуктам
plot_sales(product_sales, 'Общая сумма продаж по продуктам', 'Продукт', 'Сумма продаж')

# График общей суммы продаж по дням
plot_sales(daily_sales, 'Общая сумма продаж по дням', 'Дата', 'Сумма продаж')



