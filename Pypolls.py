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

#Open the election results and read the file.
with open(file_to_load) as election_data:


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
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
