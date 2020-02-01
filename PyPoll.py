#Psuedocode
#retrieve data from the .csv file called election results in 
    #1. we need to get the total number of votes case (sum of the candidate column, which should equal the number of rows
        # in the file -1 for the column header)
    #2. Write out a complete list of candidates who received votes--going to need a loop
    #3. We need to calculate the percentage of votes each candidate won 
        # conceptually this is the (count of candidates/totalrows in data*100), then use
        # the precision option to round to no more than 2 decimal places)
    #4. the final challenge will need some formatting to draw out lines and make a facsimile of a table.
#practice statements to open files
#file_to_load = 'Resources/election_results.csv'
#election_data = open(file_to_load, 'r')
#election_data.close()
#with open(file_to_load) as election_data:
    #print(election_data)
import os
import csv
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#open the election results and read the file.
with open(file_to_load) as election_data:
# read the file object (election_data is the file object) with the reader function. 
# call it another object name-file_reader.
    file_reader = csv.reader(election_data)
#print each row in the CSV file.
    #for row in file_reader:
            #print(row)
    headers = next(file_reader)
    print(headers)