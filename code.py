# --------------
import pandas as pd 
import numpy as np

# Read the data using pandas module.
df_ipl = pd.read_csv(path)
#print(df_ipl)
# Find the list of unique cities where matches were played
unique_cities = df_ipl['city'].unique()
#print("The list of unique cities are ",unique_cities)
# Find the columns which contains null values if any ?
null_columns_mask= df_ipl.isnull().any()
null_columns =df_ipl.columns[null_columns_mask]
print("the null coulmns are",null_columns)
# List down top 5 most played venues
top_venues = df_ipl.groupby(['venue'])['match_code'].nunique().nlargest(5)
#top_venues = df_ipl].groupby(['venue'])['match_code'].nunique().sort_values(ascending =false)[:5]
print(top_venues)


# Make a runs count frequency table
runs_count_frequency = df_ipl['runs'].value_counts()
print(runs_count_frequency)

# How many seasons were played and in which year they were played 
df_ipl['year']=df_ipl['date'].str[:4]
df_ipl['year']=df_ipl['date'].apply(lambda x :x[:4])
print(df_ipl['year'].nunique())
# No. of matches played per season
matches_season =df_ipl.groupby(['year'])['match_code'].sum()
print("no of matches playes",matches_season)
# Total runs across the seasons
runs_season = df_ipl.groupby(['year'])['runs'].sum()
print(runs_season)
# Teams who have scored more than 200+ runs. Show the top 10 results
innings_total =df_ipl.groupby(['match_code','batting_team','inning'],as_index=False)['runs'].sum()
high_innings_totals_mask = innings_total['runs']>=200
high_innings_totals =innings_total[high_innings_totals_mask]
#print(high_innings_totals)
high_innings_scoring_teams =high_innings_totals.groupby(['batting_team'])['runs'].sum().nlargest(10)
print(high_innings_scoring_teams)
# What are the chances of chasing 200+ target
innings_total =df_ipl.groupby(['match_code','batting_team','inning'],as_index=False)['runs'].sum()
high_innings_one_total =high_innings_totals[high_innings_totals['inning']==1]
high_innings_two_total =high_innings_totals[high_innings_totals['inning']==2]
joined_data =pd.merge(left =high_innings_one_total,right =high_innings_two_total,on='match_code',suffixes =('_first','second'))
print(joined_data)

chased_matched_won =joined_data['runs_first']<joined_data['runssecond']
total_matches =len(joined_data)
winning_percentage = chased_matched_won.sum()/total_matches*100
print(winning_percentage)

# Which team has the highest win count in their respective seasons ?
highest_win = df_ipl.groupby(['match_code'])['winner'].value_counts().nlargest(1)
print(highest_win)





