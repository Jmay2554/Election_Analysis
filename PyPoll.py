#Add dependencies
import os
import csv

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources" ,"election_results.csv")
#Asdsign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# Initialize a new list for candidate options
candidate_options = []
# Initialize a new dict for candidate votes
candidate_votes = {}
# Initialize a winning canididate and count tracker
winning_candidate =""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #2 Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]

       
        #If the candidates does not match any existing candidate......
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            votes = candidate_votes[candidate_name] = 0
         
           #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each canididate by looping through the counts.
# Iterate through the canididate list.
for candidate_name in candidate_votes:
    #grab the votes for a candidate
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes
    vote_percentage = float(votes)/float(total_votes)* 100
 
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
## Determine the winning vote count
# Print the candidate name and percentage of votes.

#if statement to check if the first vote count is greater than 0


if (votes > winning_count) and (vote_percentage > winning_percentage):
    # if true then so is this
    winning_count = votes
    # set the percentage to the winning percentage
    winning_percentage = vote_percentage
    # set the winning candidate
    winning_candidate = candidate_name
    
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
    


        


#3 print the candidate votes
