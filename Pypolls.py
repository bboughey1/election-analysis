#The data we need to retrieve
#1.Total votes cast
#2. A complete list of candidates
#3. The total number of votes each candidate received
#4. The percentage of total votes each candidate received
#5. Who got the most votes

#Assign a variable for the file to load and the path.

#file_to_load = "Resources/election_results.csv"

#Open the election results and read the file.

#with open(file_to_load) as election_data:

    #To do: peform analysis
   # print(election_data)

#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

    #print the file object
    #print(election_data)

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0

# Print the candidate name from each row
candidate_options = []

#Declare an empty dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file

# Using the with statement open the file as a text file.
    #with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")#outfile.close()

     # Write three counties to the file.
     #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")#outfile.close)

        #To Do: read and analyze the data here.
    
    #Open the election results and read the file.
   

    # Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #2 add to the total vote count
        total_votes += 1

        #Print the candidate name from each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            #Begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


#Determine the percentage of votes for each candidate by looping through the counts.
#1. Iterate through the candidate list.
for candidate in candidate_votes:
    #2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    #3. Calcualte the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #4. Print the candidate's name, vote count, and percentage of votes to the terminal
    #print(f"{candidate}: received {vote_percentage:.1f}% of the vote.") 

    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
    # If true then set winning_count = votes and winning_percent =
    # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        #Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate  

        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# 3. Print the total votes.
#print(total_votes)

#Print the candidate list.
#print(candidate_options)

#Print the candidate vote dictionary.
#print(candidate_votes)
