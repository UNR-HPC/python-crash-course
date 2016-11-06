# Print the total FY 2014/2015 City of Reno Checkbook expenditure

# The csv module implements classes for reading and writing tabular data
import csv

# Create a function called 'print_total_spent'
def print_total_spent():
	# Open the FY 2014/2015 City of Reno checkbook file for binary reading
	checkbook = open('FY_14_15_City_of_Reno_Checkbook.csv', 'rb')

	# Create a reader object for reading rows from the checkbook file.
	# Each field is delimited with a ',' character.
	checkbook_reader = csv.reader(checkbook, delimiter=',')

	# Read the header row from the checkbook
	header = checkbook_reader.next()

	# Declare and initialize a variable for the total spent
	total_spent = 0.0
	# Read each row and of the checkbook and add accumulate the value of the
	# last column into the total spent
	for row in checkbook_reader:
		total_spent += float(row[-1])

	# Print the total spent to the console.
	print 'Total Spent =', total_spent

	# Close the checkbook file
	checkbook.close()

# Check to see if we are executing this script
if __name__ == '__main__':
	print_total_spent()