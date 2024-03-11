import os
import csv

file = r"C:\Users\KANO\Desktop\Bootcamp files\weekly challenge 3\python-challange\PyPoll\Resources\election_data.csv"

# Create empty arrays to hold values
id = []
candidates = []
unique_names = []

# Open and read csv
with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # Read the header row first
    csv_header = next(csv_file)

    # Read through each row of data after the header 
    for row in csv_reader:
        id.append(row[0])
        candidates.append(row[2])

    # Load first candidate for comparison 
    unique_names.append(candidates[0])

    # Iterate through candidates to get unique names
    for i in range(len(candidates) - 1):
        if candidates[i + 1] != candidates[i] and candidates[i + 1] not in unique_names:
            unique_names.append(candidates[i + 1])
    
    print(unique_names)

    print(len(id))
