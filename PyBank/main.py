import os
import csv

file = r"C:\Users\KANO\Desktop\Bootcamp files\weekly challenge 3\python-challange\PyBank\Resources\budget_data.csv"

months = []

with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    csv_header = next(csv_file)

    for row in csv_reader:
        months.append(row[0])

print("Total Months: " + str(len(months)))


