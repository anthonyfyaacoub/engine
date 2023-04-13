# Import libraries
import pandas as pd
import numpy as np

import pickle 

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

from collections import Counter

#Import Warnings
import warnings
warnings.filterwarnings("ignore")

# Load games data
gamesdata = pd.read_csv('gamesdata.csv', index_col = 0)
gamesdata.head()

# Load merged data
mergeddata = pd.read_csv('mergeddata.csv', index_col = 0)
mergeddata.head()

# Load numgames data
numgames = pd.read_csv('numgames.csv', index_col = 0)
numgames.head()

# Count unique game ids
unique_game_ids = len(mergeddata['id'].unique())

# Count unique user ids
unique_user_ids = len(mergeddata['uid'].unique())

# Select entries where release date is not null
data = gamesdata[gamesdata['release_date'].notnull()]

# Describe release date feature
release_date_desc = data['release_date'].describe()

# Replace strings which are not of the format xxxx-xx-xx with None
def format_release_date(date_str):
    if date_str[-3] != '-':
        return None
    return date_str
data['release_date'] = data['release_date'].apply(format_release_date)

# Select entries where release date is not null
data = data[data['release_date'].notnull()]

# Convert release date to DateTime 
data['release_date'] = pd.to_datetime(data['release_date'])

# Plot histogram of release date feat for all games
plt.hist(data['release_date'], bins=30)
plt.title('Game Releases')
plt.ylabel('Number of Games')
plt.xlabel('Year')
plt.show()

# Filter for games released after 2010
recentgames = data[data['release_date'].dt.year > 2010]

# Plot histogram of release date feat for recent games
plt.hist(recentgames['release_date'], bins=30)
plt.title('Game Releases post 2010')
plt.ylabel('Number of Games')
plt.xlabel('Year')
plt.show()



# Create month feature
data['release_month'] = pd.DatetimeIndex(data['release_date']).month

# Plot countplot using Seaborn
sns.countplot(x=data['release_month'])
plt.title('Frequency of game releases per month')
plt.xlabel('Month')
plt.ylabel('Count')
plt.show()

# Countplot of sale month

# define palette to highlight best months to buy
custompalette = {release_month: "skyblue" if (release_month == 10 or release_month == 11 or release_month == 12 ) else "lightgrey" \
                 for release_month in data['release_month'].unique()}

sns.set_style("whitegrid")
sns.countplot(x=data['release_month'], palette=custompalette)
plt.title('Number of game releases per month')
plt.xlabel('Month')
plt.ylabel('Count')
plt.savefig('Images/month.pdf', bbox_inches="tight")

# Define function to determine quarter
def quarter(month):
    ''' Returns quarter in which month falls'''
    if 1 <= month <= 3:
        quarter = 'Q1'
    elif 4 <= month <= 6:
        quarter = 'Q2'
    elif 7 <= month <= 9:
        quarter = 'Q3'
    else:
        quarter = 'Q4'
    return quarter

# Create quarter feature
data['release_quarter'] = data['release_month'].apply(quarter)

# Plot countplot using Seaborn
sns.countplot(x=data['release_quarter'], order=data['release_quarter'].value_counts().index)
plt.title('Frequency of game releases per quarter')
plt.xlabel('Quarter')
plt.ylabel('Count')
plt.show()

# Create copy to work with
releasedatedata = mergeddata.copy()

# Select entries where release date is not null
releasedatedata = releasedatedata[releasedatedata['release_date'].notna()]

# Replace strings which are not of the format xxxx-xx-xx with None
releasedatedata['release_date'] = [date if date[-3] == '-' else None for date in releasedatedata['release_date']]

# Select entries where release date is not null
releasedatedata = releasedatedata[releasedatedata['release_date'].notna()]

# Convert to DateTime 
releasedatedata['release_date'] = pd.to_datetime(releasedatedata['release_date'])

# Check 
releasedatedata['release_date'].describe()

# Display the first few rows of data
numgames.head()

# Generate descriptive statistics for the number of items owned
numgames['items_count'].describe()

# Visualize the distribution of the number of games owned
numgames['items_count'].hist()
plt.title('Number of games owned')
plt.xlabel('Number of games')
plt.ylabel('Number of users')
plt.show()

# Visualize the distribution of the number of games owned within the 90th percentile
numgames[numgames['items_count'] < numgames['items_count'].quantile(0.90)].hist()
plt.title('Number of games owned (within 90th percentile)')
plt.xlabel('Number of games')
plt.ylabel('Number of users')
plt.show()

# Save the visualization of the number of games owned within the 90th percentile to a PDF file
numgames[numgames['items_count'] < numgames['items_count'].quantile(0.90)].hist()
plt.title('Number of games owned (within 90th percentile)')
plt.xlabel('Number of games')
plt.ylabel('Number of users')
plt.savefig('Images/numgames.pdf', bbox_inches = "tight")
plt.show()

# Create a copy of the original data to work with
gamesprice = gamesdata.copy()

# Generate descriptive statistics for the price of games
gamesprice['price'].describe()

# Define the values to be replaced with 0
replace_values = ['Free To Play', 'Free', 'Free Demo', 'Play for Free!', 'Install Now', 'Play WARMACHINE: Tactics Demo',
                  'Free Mod', 'Install Theme', 'Third-party', 'Play Now', 'Free HITMAN™ Holiday Pack', 'Play the Demo',
                  'Starting at $499.00', 'Starting at $449.00', 'Free to Try', 'Free Movie', 'Free to Use']

# Replace each value in the list with 0 using a for loop
for value in replace_values:
    gamesprice = gamesprice.replace(to_replace=value, value=0)


import pandas as pd
import matplotlib.pyplot as plt

# Convert 'price' column to float
gamesprice['price'] = pd.to_numeric(gamesprice['price'], errors='coerce')

# Get summary statistics
gamesprice_stats = gamesprice['price'].describe()

# Get data below 99th percentile
below_99 = gamesprice[gamesprice['price'] < gamesprice['price'].quantile(0.99)]

# Get summary statistics for data below 99th percentile
below_99_stats = below_99['price'].describe()

# Plot distribution of data below 99th percentile
plt.hist(below_99['price'])
plt.xlabel('Price in USD')
plt.title('Game Price Distribution')
plt.savefig('Images/price.pdf', bbox_inches = "tight")
plt.show()

# Create a copy of 'gamesdata'
gamegenres = gamesdata.copy()

# Drop rows with missing 'genres' values
gamegenres.dropna(subset=['genres'], inplace=True)

# Get unique genres as a list
genres = gamegenres['genres'].unique().tolist()

# Print first 5 genres
print(genres[:5])

# Join all genre strings
allgenres = ','.join(genres)

# Preview first 100 characters
print(allgenres[:100])

# Remove unwanted characters
allgenres = allgenres.translate(str.maketrans("", "", "[]' "))

# Preview first 100 characters
print(allgenres[:100])

# Split genres into a list
splitgenres = allgenres.split(',')

# Get unique genres using a set
uniquegenres = set(splitgenres)

# Print unique genres
print(uniquegenres)

# Create columns with genres
gamegenres = pd.concat([gamegenres, pd.DataFrame(columns=uniquegenres)])

# Split genres in genres column
gamegenres['genres'] = gamegenres['genres'].str.replace("[\]\[\']", "").str.split(',').apply(pd.Series)

# Map to columns - set to 1 if genre applies
gamegenres = gamegenres.set_index('genres').stack().str.get_dummies().sum(level=0)

# Visualize the new columns
gamegenres.head(2)

# Get genre columns
genrecols = gamegenres.loc[:, 'Casual':'Adventure'].columns

# Go through each column and sum it
sortedgenresdict = {col: gamegenres[col].sum() for col in genrecols}

# sort dictionary based on counts, ascending order so reverse = True    
sortedgenresdict = {keys: values for keys, values in \
                        sorted(sortedgenresdict.items(), key = lambda item: item[1], reverse = True)}

# View dictionary
sortedgenresdict

# Create copy
gametags = gamesdata.copy()

# Drop NaN
gametags = gametags[gametags['tags'].notnull()]

# Get unique lists
tags = gametags['tags'].unique()

# View first 5
tags[:5]

# Combine all strings
alltags = ','.join(tags)

# Preview first 100 characters
alltags[:100]

# Replace chars
alltags = alltags.replace("[\]\[\']", "")

# Check
alltags[:100]

# Split
splittags = alltags.split(',')

# Use set to obtain unique values
uniquetags = set(splittags)
len(uniquetags)

# Select entries where publisher is non-null
data = gamesdata[gamesdata['publisher'].notnull()]

# Create dictionary
game_publishers = {}
for publisher in list(data['publisher']):
    game_publishers[publisher] = game_publishers.get(publisher, 0) + 1

# Get top 10 publishers
top10_publishers = dict(sorted(game_publishers.items(), key=lambda x:x[1], reverse=True)[:10])

# Prepare for bar chart plot
publishers = list(top10_publishers.keys())
counts = list(top10_publishers.values())

# Plots most popular publishers
fig, ax = plt.subplots(figsize=(8,4))
ax.barh(publishers, counts, align='center')
ax.set_yticks(publishers)
ax.set_yticklabels(publishers, fontsize=12)
ax.set_title("Most Popular Publishers", fontsize=12, fontweight='bold')
plt.show()
