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
#file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file.
#with open(file_to_load) as election_data:
    #Print the file object.
    #print(election_data)

#here we are going to try out writing to a file using more verbose code
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#outfile = open(file_to_save, "w")--less concise code

#write some data to the file
#outfile.write("Hello World")--less concise code

#close the file
#outfile.close()--less concise

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the with statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
    #write three counties to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")

    #write three counties to the file in one line
    txt_file.write("Counties in the Election\n_______________________________\nArapahoe\nDenver\nJefferson")

