import os
import csv

pollData = os.path.join('PyPoll',"Resources","election_data.csv")


with open(pollData, newline="") as csv_file:
    elections_data = csv.reader(csv_file)

    next(csv.reader)
    data = list(csv.reader)
    row_count = len(data)

    candidatelist = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candidatelist: 
            candidatelist.append(candidate)
            
    candidatecount = len(candidatelist)
    
    votes = list()
    percentage = list()
    for j in range (0,candidatecount):
        name = candidatelist[j]
        votes.append(tally.count(name))
        votesprct = votes[j]/row_count
        percentage.append(votesprct)

    winner = votes.index(max(votes))     

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,candidatecount): 
        print(f"{candidatelist[k]}: {percentage[k]} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candidatelist[winner]}")
    

    output = open("output.txt", "w")


    # line1 = ("Election Results")
    # line2 = ("----------------------------")
    # line3 = (f"Total Votes: {row_count:,}")
    # line4 = ("----------------------------")
    # line5 = for k in range (0,candidatecount): 
    # print(f"{candidatelist[k]}: {percentage[k]} ({votes[k]:,})")
    # line6 = ("----------------------------")
    # line7 = (f"Winner: {candidatelist[winner]}")