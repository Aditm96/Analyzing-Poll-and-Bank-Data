# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:31:12 2020

@author: aditm
"""

import os
import csv
        
TotalVotes = 0
Canidate = []
Votes = []
Names = []
Khan = 0
Correy = 0
Li = 0
Tooley = 0

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv') 
with open(csvpath, encoding = 'utf-8') as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        TotalVotes += 1
        canidate = row[2]
        Canidate.append(canidate)
        Canidate = list(dict.fromkeys(Canidate))
        if canidate == "Khan":
            Khan += 1
        elif canidate == "Correy":
            Correy += 1
        elif canidate == "Li":
            Li += 1
        else:
            Tooley += 1
    #Calculations
    KhanVote = round((Khan / TotalVotes)*100, 2)
    CorreyVote = round((Correy / TotalVotes)*100, 2)
    LiVote = round((Li / TotalVotes)*100, 2)
    TooleyVote = round((Tooley / TotalVotes)*100, 2)
    Votes = [Khan, Correy, Li, Tooley]
    Names = ['Khan', 'Correy', 'Li', 'Tooley']
    Winner = zip(Names, Votes)
    Max = Votes.index(max(Votes))
    MaxZip = list(Winner)[Max][0]
print("Election Results")
print("------------------------")
print(f'Total Votes: {TotalVotes}')
print("------------------------")
print(f'{Canidate[0]}: {KhanVote}% ({Khan})')
print(f'{Canidate[1]}: {CorreyVote}% ({Correy})')
print(f'{Canidate[2]}: {LiVote}% ({Li})')
print(f'{Canidate[3]}: {TooleyVote}% ({Tooley})')
print(f'----------------------')
print(f'Winner: {MaxZip}')
print(f'----------------------')

