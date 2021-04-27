import csv
with open('sales (1).csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    sales = []

    for row in spreadsheet:
        sales_monthly = int(row['sales'])
        sales.append(sales_monthly)

sales_monthly = (sales)
print(sales_monthly)

total = sum(sales_monthly)
print(total)
