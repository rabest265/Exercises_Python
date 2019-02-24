import os
import csv

# Call in the CSV file election_data.csv and store the output path
csvpath = os.path.join("..", "Resources", "election_data.csv")
output_path = os.path.join("poll_results.txt")

#Set counting variables to 0 to start
totalvotes = 0
candidatelist = []
candidatecount =[]
largest = 0

#Open the file and read the header in csv reader
with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # Go through each row of data
    for row in csvreader:
        candidate =  row[2]
        # Calculate the total number of votes
        totalvotes = totalvotes + 1
        # add value to count if candidate is already there otherwise add them to the list
        if candidate in candidatelist:
            candidatecount[candidatelist.index (candidate)] += 1
        else:
            candidatelist.append (candidate)
            candidatecount.append (1)

    
    

#Write an output file with requested information
    file = open(output_path,"w")
    file.write("Election Results\n")
    file.write("----------------------------------------\n")
    file.write("Total Votes: " + str(totalvotes) + "\n")
    file.write("----------------------------------------\n")
    #  list each cabdidate, the percentage and total number of votes
    for name in candidatelist:
        count = candidatecount[candidatelist.index (name)]
        pct = round(count /totalvotes * 100,2)
        file.write(name + ":  " + str(pct) + "% (" + str(count) + ")\n")
    # Calculate the winner of the election based on popular vote.
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
