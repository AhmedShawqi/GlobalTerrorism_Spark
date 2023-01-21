#Importing Modules

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

###

#Specifying my Data

use_cols = ["eventid","iyear","imonth","iday","country_txt","region_txt","region_txt","city",
            "location","attacktype1_txt","targtype1_txt","corp1","natlty1_txt","gname",
            "motive","weaptype1_txt","nkill"]
###

#Reading Data

df = pd.read_csv(r"C:\Users\Ahmed\Downloads\Global Terrorism - START data\globalterrorismdb_0718dist.csv",encoding='latin1'
                 ,usecols=use_cols,low_memory=False
                 )
print(df.head(30))

###

#Renaming Columns

df.rename(columns={"eventid":"id","iyear":"year","imonth":"month","iday":"day","country_txt":"country",
                   "region_txt":"region","attacktype1_txt":"attack_type","targtype1_txt":"target_type","corp1":"corp",
                   "natlty1_txt":"nationality","gname":"gang_name","weaptype1_txt":"weapon_type","nkill":"num_kills"},
          inplace =True)

###

#Removing Duplicates and Null Values

df.drop_duplicates()
df = df.dropna()
print(df.shape)

###

#Checking Unique Values

print(df.nunique())

####

#plotting the data through the years

fig, ax = plt.subplots(figsize = (17, 5))
sns.countplot(x='year', data=df)
plt.xticks(rotation = 90)
plt.show()

###

#Highest countries in Terrorism

fig, ax = plt.subplots(figsize= (17,5))
sns.countplot(x='country',data=df)
plt.xticks(rotation = 90)
plt.show()

###

#Most Dangerous gangs around the World
n=df.groupby('gang_name').agg(num_kills=('num_kills','sum')).sort_values('num_kills',ascending = False).head(20)
print(n.head(5))
g=n.plot(kind='bar',title='Most Dangerous gangs',color='royalblue',edgecolor='black')
g.set_xticks(np.arange(len(n)))
plt.show()

###

#Countries Highest Kills
n=df.groupby('country').agg(num_kills=('num_kills','sum')).sort_values('num_kills',ascending = False).head(20)
print(n.head(5))
g=n.plot(kind='bar',title='Countries Hightes Kills',color='maroon',edgecolor='black')
g.set_xticks(np.arange(len(n)))
plt.show()

###


#Most Dangerous Attack Types around the World

n=df.groupby('attack_type').agg(num_kills=('num_kills','sum')).sort_values('num_kills',ascending = False).head(20)
print(n.head(5))
g=n.plot(kind='bar',title='Most Attack Types',color='navy',edgecolor='black')
g.set_xticks(np.arange(len(n)))
plt.show()

###

#Most used Weapons

n=df.groupby('weapon_type').agg(num_kills=('num_kills','sum')).sort_values('num_kills',ascending = False).head(20)
print(n.head(5))
g=n.plot(kind='bar',title='Most Used Weapons',color='royalblue',edgecolor='black')
g.set_xticks(np.arange(len(n)))
plt.show()

###

#Number Of Kills per Year

n=df.groupby('year').agg(num_kills=('num_kills','sum')).sort_values('num_kills',ascending = False).head(20)
print(n.head(5))
g=n.plot(kind='bar',title='Number of Kills per Year',color='lightgreen',edgecolor='black')
g.set_xticks(np.arange(len(n)))
plt.show()

#Each region

n=df.groupby('region').agg(num_kills=('num_kills','sum')).sort_values('num_kills',ascending = False).head(20)
print(n.head(5))
g=n.plot(kind='bar',title='Number of Kills by each Region',color='lightgrey',edgecolor='black')
g.set_xticks(np.arange(len(n)))
plt.show()

