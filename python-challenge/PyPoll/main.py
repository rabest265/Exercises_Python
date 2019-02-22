#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

import os
import csv

# Call in the CSV file budget_data.csv and store the output path
csvpath = os.path.join("..", "Instructions", "election_data.csv")
output_path = os.path.join("poll_results.txt")

#Set counting variables to 0 to start
totalvotes = 0
candidatelist = []
candidatecount =[]
largest = 0

#Open the file and read the header in csv reader
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # Go through each row of data
    for row in csvreader:
        candidate =  row[2]
        # Calculate the total number of votes
        totalvotes = totalvotes + 1
        # add value to count if candidate is already there otherwise add them
        if candidate in candidatelist:
            candidatecount[candidatelist.index (candidate)] += 1
        else:
            candidatelist.append (candidate)
            candidatecount.append (1)

    
# Calculate the total number of votes
#  * A complete list of candidates who received votes
#  * The percentage of votes each candidate won
#  * The total number of votes each candidate won
#  * The winner of the election based on popular vote.


#Write an output file with requested information
    file = open(output_path,"w")
    file.write("Election Results\n")
    file.write("----------------------------------------\n")
    file.write("Total Votes: " + str(totalvotes) + "\n")
    file.write("----------------------------------------\n")
    for name in candidatelist:
        count = candidatecount[candidatelist.index (name)]
        pct = round(count /totalvotes * 100,3)
        file.write(name + ":  " + str(pct) + "% (" + str(count) + ")\n")
        if count > largest:
            largest = count
            Winner = name
    file.write("----------------------------------------\n")
    file.write("Winner:  " + Winner + "\n")
    file.write("----------------------------------------")
    file.close()

#Print the file in terminal
    file = open(output_path,"r")
    print (file.read())
    file.close
