import os
import csv
import pandas as pd

# Path to collect data from the Resources folder
electionData = "election_data_1.csv"
election_df = pd.read_csv(electionData)
#print(election_pd.head())

# Number of votes
num_votes = election_df["County"].count()

# Grouping by Candidate
candidate_group = election_df.groupby("Candidate")

#Count votes per candidate
#candidate_vote = election_df(candidate_group["Voter ID"].count())
#candidate_votes = election_df.groupby(["Candidate"]).size()
candidate_votes = election_df.groupby(["Candidate"])

# Candidate percentage
candidate_percent = (candidate_votes["Voter ID"].count())/num_votes
# print(candidate_percent)

#candidate votes part 2
calc_votes = (candidate_percent*num_votes)
# print(calc_votes)

# combine 2 dataframes
result = pd.concat([candidate_percent, calc_votes], axis=1)

# change column names of combined dataframe and format
result.columns = ['Percent of Vote', 'Total Votes']
# result['Percent of Vote'] = result['Percent of Vote'].map("{:,.2f}%".format)
result['Total Votes'] = result['Total Votes'].map("{:,.0f}".format)



print("Election Results")
print("---------------")
print("Total Votes: " + str(num_votes))
print("---------------")
print(str(result))
print("---------------")
#print winner
# winner = result.idxmax(axis=0,skipna=True)
# result.loc[result['Total Votes'].argmax()]
# print(winner)
print("---------------")
