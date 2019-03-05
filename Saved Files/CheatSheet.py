# This file is a cheat sheet of codes for Python

## Import random at top if need a random generater
import random

## Declare/assigning variables
name = "Testing"
age = 5
type1 = ["Testing","Data"]
type2 = ["Mary","Rachel"]
type3 = ["Sony","Dell"]

# Zip all three lists together into tuples
namelists = zip(type1, type2, type3)


## inputting values as string, integer, or booleon
name2 = input ("Input Name: ")
age2 = int(input("Input Age: "))

##Output with and without f-string
print("Test Name: " + name + ", Test Age: " + str(age))
print(f"Your Name: {name2}, Your Age: {age2}")

##Conditionals use if, elif, else and have colons and indents
if name2 in type2:
    print("You are in type 2")
elif name2 in type3:
    print("You are in type 3")
else:
    print("You are not in a group")

##Use random to select a random item from a list (make sure to import random)
name3 = random.choice(type3)
print ("Computer's name is: " + name3)


## Set up a list
AgeList = [0,1,2,3]
## remove first (or given) variable
AgeList.pop(0)
## Add to end of list
AgeList.append (4)
AgeList.append (9)
## Remove from the list
AgeList.remove (9)

## len returns the length of the list
print ("The length of the list is: " + str(len(AgeList)))

## use brackets to call an item from the list by it's index number (remember starts with 0)
print ("The first name is " + type3[0] + " and the second name is " + type3[1])
## index to return the nth value of the list (remember starts with 0)
print ("You got name number: " + str(type3.index(name3) + 1))

age3 = random.choice(AgeList)
print ("Computer age is: " + str(age3))
for x in range(10):
    print(random.randint(1, 10))


## Use range to set up a list of values strting from 0 or the first variable denoted
run = "y"
lastval = 0
while run == "y":
    Chain = int(input("How many numbers? "))
    for x in range(lastval, lastval + Chain):
        print (x)
    run = input ("Do you want to continue? (y/n) ")
    lastval = Chain +lastval

#Store the file path associated with the file (note the backslash may be OS specific)
file = '../Resources/input.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text" only within with statement
with open(file, 'r') as text:
    print(text)
    # Store all of the text inside a variable called "lines"
    lines = text.read()
    # Print the contents of the text file
    print(lines)


# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

#HOW TO CALL IN A FILE PATH
csvpath = os.path.join('..', 'Resources', 'accounting.csv')
output_path = os.path.join("..", "output", "new.csv")

# HOW TO READ IN A CSV FILE
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # skipp = next(csv_reader, None)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header (if you have the row before)
    for row in csvreader:
        print(row)


#HOW TO WRITE A CSV FILE
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])
    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])


# open the output file, create a header row, and then write the zipped object to the csv
output_file = os.path.join("output.csv")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Option 1", "Option 2"])
    #Write a list of zipped arrays
    writer.writerows(namelists)

# List[index] += 1 will add 1 to the indexed value in a list

#Write an output text file
output_path = os.path.join("output.txt")
file = open(output_path,"w")
file.write("AGES\n") #\n gets you to another line
file.write("The age is: " + str(age2) + "\n")
file.close()
    
#Print the file in terminal
file = open(output_path,"r")
print (file.read())
file.close

# Define the function and tell it to print "Hello!" when called
def printHello():
    print(f"Hello!")


# Call the function within the application to ensure the code is run
printHello()
# -------------#


# Functions that take in and use parameters can also be defined
def printName(name):
    print("Hello " + name + "!")


# When calling a function with a parameter, a parameter must be passed into the function
printName("Bob Smith")
# -------------#

# The prime use case for functions is in being able to run the same code for different values
listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [11, 12, 13, 14, 15]


def listInformation(simpleList):
    print(f"The values within the list are...")
    for value in simpleList:
        print(value)
    print("The length of this list is... " + str(len(simpleList)))


listInformation(listOne)
listInformation(listTwo)

# A dictionary of the names
actor = {"name": "Tom Cruise"}
print(f'{actor["name"]}')
another_actor = {
    "name": "Sylvester Stallone",
    "age": 62,
    "married": True,
    "best movies": [
        "Rocky",
        "Rocky 2",
        "Rocky 3"]}
# A dictionary can even contain another dictionary
film = {"title": "Interstellar",
        "revenues": {"United States": 360, "China": 250, "United Kingdom": 73}}
print(f'{film["title"]} made {film["revenues"]["United States"]}'" in the US.")

# We can manipulate each element as we go
fish = "halibut"
capital_letters = []
for letter in fish:
    capital_letters.append(letter.upper())
# List Comprehension for the above
capital_letters = [letter.upper() for letter in fish]

july_temperatures = [87, 85, 92, 79, 106]
# List Comprehension with conditional
hot_days = [temperature for temperature in july_temperatures if temperature > 90]

# upper is uppercase, lower is lowercase, title is titlecase
# % is mod
# += to add to itself

# We can also specify default values for parameters
def make_quesadilla(protein, topping="sour cream",cheese="chedder"):
    quesadilla = f"Here is a {protein} quesadilla with {topping}"
    print(quesadilla)
# Make a quesadilla using the default topping
make_quesadilla("chicken")
# Make a quesadilla with a new topping
make_quesadilla("beef", cheese="feta")

# Functions can return a value
def square(number):
    return number * number
# You can save the value that is returned
squared = square(2)
print(squared)
print(square(2))
