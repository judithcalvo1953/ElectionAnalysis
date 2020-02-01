import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0
#declare  a new list.
candidate_options = []
#declare the empty dictionary.
candidate_votes = {}
#Winning Candidate and Winning County tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#open the election results and read the file.

with open(file_to_load) as election_data:
# read the file object (election_data is the file object) with the reader function. 
# call it another object name-file_reader.
    file_reader = csv.reader(election_data)
#direction to skip headers
    
    headers = next(file_reader)
    
    #print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
           candidate_options.append(candidate_name)
           candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

#determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list Note: candidate_votes is your dictionary.
for candidate in candidate_votes:
    #2. retrieve vote count of a candidate
    votes = candidate_votes[candidate]
    #3. Calculate the percentages of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # to do: print out each candidate's name, vote count, and percentage of
    #votes to the terminal to be used to feed the if conditional statements
    print(f"{candidate}: {vote_percentage:.1f}%  ({votes:,})\n")
    #determine winning vote count and candidate
    #1.determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #2 if true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage =vote_percentage
        #3 Set the winning_candidate equal to the candidate's name
        winning_candidate = candidate
    #4. Print the candidate name and percentage of votes.
    #print(f"{candidate}: received {vote_percentage:.2f}% of the vote.")
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