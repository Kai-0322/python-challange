import os
import csv

file = "../Resources/budget_data.csv"

months = []

with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimeter = ',')

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        months.append(row[0])

print(len(months))


