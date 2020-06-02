#Add our dependencies
import csv
import os

#Assign a variable for the file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

#Challenge County Option County Votes
county_names = []
county_votes = {}

#Track the winning candidate vote count and percentages
winning_candidate = ""
winning_county = 0
winning_percentage = 0

#Challenge: Track the largest county voter turnout and its percentages
largest_county_turnout = ""
largest_county_vote = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    print(reader)

    #Read the header
    header = next(reader)
  
    #loop each row in the csv file
    for row in reader:
        
        #Add to the total vote count
        total_votes = total_votes + 1

        #Get the candidate name from each row
        candidate_name = row[2]

        #Get the county name from each row
        county_name = row[1]

        #If the candidate does not match any existing candidate
        #add it to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #and begin tracking that candidate voter count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate count
        candidate_votes[candidate_name] += 1

        if county_name not in county_names:
            county_names.append(county_name)

            #begin tracking the county vote
            county_votes[county_name] = 0

        county_votes[county_name] +=1

#save the results to our text file
with open(file_to_save, "w") as txt_file:
    #Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes {total_votes:,}\n"
        f"--------------------\n"
        f"County Votes:\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)

    #Challenge save final county vote count to the text file
    for county in county_votes:
        #retrieve vote count and percentage
        county_vote = county_votes[county]
        county_percent = int(county_vote) / int(total_votes) * 100

        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n"
        )
        print(county_results, end="")
        txt_file.write(county_results)

        #Determine winnign vote count
        if (county_vote > largest_county_vote):
            largest_county_vote = county_vote
            largest_county_turnout = county

    #Print the county with the largest turnout
    largest_county_turnout = (
        f"\n--------------------\n"
        f"Largest County Turnout {largest_county_turnout}\n"
        f"----------------------\n"
        )

    print(largest_county_turnout)    
    txt_file.write(largest_county_turnout)
 
    #Save the final candidate vote count to the text file
    for candidate in candidate_votes:
        #Retrieve the vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) *100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        )

        #Print each candidate voter count and percentage to the terminal
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_county) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage =vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate:}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n" 
    )

    print(winning_candidate_summary)

    #save to text file
    txt_file.write(winning_candidate_summary)
