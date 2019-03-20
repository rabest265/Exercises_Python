import os
import csv

# Call in the CSV file budget_data.csv and store the output path
csvpath = os.path.join("..", "Resources", "budget_data.csv")
output_path = os.path.join("budget_output.txt")

#Set counting variables to 0 to start
totalpandl = 0
totalmonths = 0
totalchange = 0
lastpandl = 0
largest = 0
smallest = 0

#Open the file and read the header in csv reader
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # Go through each row of data
    for row in csvreader:
        date =  row[0]
        pandl = float(row[1])
        # Calculate the total number of months included in the dataset
        totalmonths += 1
        # Calculate the net total amount of "Profit/Losses" over the entire period        
        totalpandl += pandl
        # Calculate the changes in "Profit/Losses" after the first instance
        if totalmonths != 1:
            change = pandl - lastpandl
            totalchange += change
            # Calculate the greatest increase in profits (date and amount) over the entire period
            if change > largest:
                largest = change
                largestmonth = date
            # Calculate the greatest decrease in losses (date and amount) over the entire period
            if change < smallest:
                smallest = change
                smallestmonth = date
        #set up the last profit/loss value
        lastpandl = pandl    

    #Write an output file with requested information
    file = open(output_path,"w")
    file.write("Financial Analysis\n")
    file.write("----------------------------------------\n")
    file.write("Total number of months are: " + str(totalmonths) + "\n")
    file.write("Total Profit/Losses over the period are: $" + str(totalpandl) + "\n")
    file.write("Total average change in Profit/Loss is: $" + str(round(totalchange / (totalmonths - 1),2)) + "\n")
    file.write("The greatest increase in profits happened in " + largestmonth + " for $" + str(largest) + "\n")
    file.write("The greatest decrease in losses happened in " + smallestmonth + " for $" + str(smallest) + "\n")
    file.write("----------------------------------------")
    file.close()
    
    #Print the file in terminal
    file = open(output_path,"r")
    print (file.read())
    file.close