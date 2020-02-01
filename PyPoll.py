import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0
#Candidate options and candidates as lists and dictionary
candidate_options = []
#declare the empty dictionary.
candidate_votes = {}
#Track the Winning Candidate, Vote County and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file.

with open(file_to_load) as election_data:
# read the file object (election_data is the file object) with the reader function. 
# call it another object name-file_reader.
    file_reader = csv.reader(election_data)
#Read the header row
    
    headers = next(file_reader)
    
    #print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
        #get the candidate name from each row.
        candidate_name = row[2]
        #If the candidate does not match any existing candidate add it to the candidate list.
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #and begin tracking that candidates voter count and use increment +=1 in the next line after the if statement
            #to add a vote
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
#save the results to our text file
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"____________________________\n"
        f"Total Votes: {total_votes:,}\n"
        f"____________________________\n")
    print(election_results, end="")
    #Save the final vot count to the text file
    txt_file.write(election_results)
    
#determine the percentage of votes for each candidate by looping through the counts This will be output to txt file.
# 1. Iterate through the candidate list Note: candidate_votes is your dictionary.
for candidate in candidate_votes:
    #retrieve vote count and percentage of a candidate
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(total_votes) * 100
    # print out each candidate's name, vote count, and percentage of votes to the terminal to be used to feed the if conditional statements
    print(f"{candidate}: {vote_percentage:.1f}%  ({votes:,})\n")
   
    
    #save the candidate results to our text file
    #determine winning vote count, winning percentate, and candidate
    
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #2 if true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage =vote_percentage
        #3 Set the winning_candidate equal to the candidate's name
        winning_candidate = candidate
    #4. Print the candidate name and percentage of votes.
    #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"__________________________________\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"___________________________________\n"
)
print(winning_candidate_summary)
#Print the total votes.
#print(total_votes)    
#print the candidate list.
#print(candidate_votes)