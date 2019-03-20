# This version uses dictionaries and functions
import os
import csv

# Call in the CSV file budget_data.csv and store the output path
csvpath = os.path.join("..", "Resources", "budget_data.csv")
output_path = os.path.join("budget_output.txt")


#Set up a dictionary of all the new fields we need
budgetdata = {
    "totalpandl": 0,
    "totalmonths": 0,
    "totalchange": 0,
    "lastpandl": 0,
    "largest": 0,
    "largestmonth":"",
    "smallest":0,
    "smallestmonth":""}

#Define the function
def budgeting (budget_row, lastvalues):
    date =  budget_row[0]
    pandl = float(budget_row[1])
    # Calculate the total number of months included in the dataset
    lastvalues["totalmonths"] += 1
    # Calculate the net total amount of "Profit/Losses" over the entire period        
    lastvalues["totalpandl"] += pandl
    # Calculate the changes in "Profit/Losses" after the first instance
    if lastvalues["totalmonths"] != 1:
        change = pandl - lastvalues["lastpandl"]
        lastvalues["totalchange"] += change
        # Calculate the greatest increase in profits (date and amount) over the entire period
        if change > lastvalues["largest"]:
            lastvalues["largest"] = change
            lastvalues["largestmonth"] = date
        # Calculate the greatest decrease in losses (date and amount) over the entire period
        if change < lastvalues["smallest"]:
            lastvalues["smallest"] = change
            lastvalues["smallestmonth"] = date
        #set up the last profit/loss value
    lastvalues["lastpandl"] = pandl    


#Open the file and read the header in csv reader
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # Go through each row of data
    for row in csvreader:
        budgeting(row, budgetdata)

    #Write an output file with requested information
    file = open(output_path,"w")
    file.write("Financial Analysis\n")
    file.write("----------------------------------------\n")
    file.write("Total number of months are: " + str(budgetdata["totalmonths"]) + "\n")
    file.write("Total Profit/Losses over the period are: $" + str(budgetdata["totalpandl"]) + "\n")
    file.write("Total average change in Profit/Loss is: $" + str(round(budgetdata["totalchange"] / (budgetdata["totalmonths"] - 1),2)) + "\n")
    file.write("The greatest increase in profits happened in " + budgetdata["largestmonth"] + " for $" + str(budgetdata["largest"]) + "\n")
    file.write("The greatest decrease in losses happened in " + budgetdata["smallestmonth"] + " for $" + str(budgetdata["smallest"]) + "\n")
    file.write("----------------------------------------")
    file.close()
    
    #Print the file in terminal
    file = open(output_path,"r")
    print (file.read())
    file.close
