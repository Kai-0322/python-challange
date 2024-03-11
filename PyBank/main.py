import os
import csv

file = r"C:\Users\KANO\Desktop\Bootcamp files\weekly challenge 3\python-challange\PyBank\Resources\budget_data.csv"

# Create empty arrays to hold values
months = []
net_total = []
monthly_change = []

# Open and read csv
with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # Read the header row first
    csv_header = next(csv_file)

    # Read through each row of data after the header then transfer them to arrays
    for row in csv_reader:
        months.append(row[0])
        net_total.append(int(row[1]))

    # Calculate monthly change then add to array
    for i in range(len(net_total) - 1):
        monthly_change.append(net_total[i + 1] - net_total[i])

    # Calculate total, average, min and max
    total = sum(net_total)
    average = sum(monthly_change) / len(monthly_change)
    greatest_increase = max(monthly_change)
    greatest_decrease = min(monthly_change)

    # Plus 1 because the month associated with change is the next month
    greatest_increase_month = monthly_change.index(max(monthly_change)) + 1
    greatest_decrease_month = monthly_change.index(min(monthly_change)) + 1

print("Total Months: " + str(len(months)))
print("Total: $" + str(total))
print("Average Change: $" + str(average))
print("Greatest Increase in Profits: " + str(months[greatest_increase_month]) + ' $' + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(months[greatest_decrease_month]) + ' $' + str(greatest_decrease))
