import os
import csv

file = r"C:\Users\KANO\Desktop\Bootcamp files\weekly challenge 3\python-challange\PyPoll\Resources\election_data.csv"

# Create empty arrays to hold values
id = []
candidates = []
unique_names = []
each_votes = []
percentages = []

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

    # Iterate through candidates to get each votes and associated percentages           
    for j in range(len(unique_names)):
        each_votes.append(candidates.count(unique_names[j]))
        percentages.append(round((each_votes[j] / len(id)) * 100, 3))
    
    # Find winner's name
    winner_name = each_votes.index(max(each_votes))

print("Election Results")
print("------------------")
print("Total Votes: " + str(len(id)))
print("------------------")
for k in range(len(unique_names)):
    print(f"{unique_names[k]}: {percentages[k]}% ({each_votes[k]})")
print("------------------")
print(f"Winner: {unique_names[winner_name]}")
print("------------------")

# Set variable for output file
output_file = os.path.join("python-challange","PyPoll", "analysis", "election_analysis.txt")

#  Open the output file
with open(output_file, "w", newline='') as datafile:

    datafile.write("Election Results" + "\n")
    datafile.write("------------------""\n")
    datafile.write("Total Votes: " + str(len(id)) + "\n")
    datafile.write("------------------"+ "\n")
    for x in range(len(unique_names)):
        datafile.write(f"{unique_names[x]}: {percentages[x]}% ({each_votes[x]})\n")
    datafile.write("------------------" + "\n")
    datafile.write(f"Winner: {unique_names[winner_name]}\n")
    datafile.write("------------------")
