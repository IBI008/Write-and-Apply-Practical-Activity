#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Pandas
import pandas as pd
import numpy as np

# Load the Excel data using pd.read_excel
movies = pd.read_excel('movies_merge.xlsx')

# Load the csv data using pd.read_csv
ott = pd.read_csv('ott_merge.csv')

# Data imported correctly
print(movies.columns)
print(movies.shape)
print(ott.columns)
print(ott.shape)


# In[3]:


# Merge the two DataFrame
mov_ott = pd.merge(movies, ott, how='left', on='ID')
 
# View the DataFrame
print(mov_ott.columns)
print(mov_ott.shape)


# In[4]:


# Question one
# What is the average rating per movie.
# View IMDb and Rotten Tomatoes
mov_ott_ratings = mov_ott[['ID','IMDb','Rotten Tomatoes']]

# View the DataFrame
mov_ott_ratings


# In[5]:


print(mov_ott_ratings)


# In[6]:


# Replace missing value with 0
mov_ott_ratings_final = mov_ott_ratings.fillna(0)
# View the DataFrame
mov_ott_ratings_final


# In[7]:


# Add a new column to the DataFrame indicating average rating.
# Average rating is ((IMDb/10) + Rotten Tomaties)/n.
# Write a user defined function.
def av_col2(df1,df2):
    df = (df1/10 + df2)/2
    return df

mov_ott_ratings_final['Rating'] = av_col2(mov_ott_ratings_final['IMDb'],
                                         mov_ott_ratings_final['Rotten Tomatoes'])

# View the DataFrame
mov_ott_ratings_final


# In[8]:


# Question two
# How many movie were release per content rating (Age)
# Categorical count
def cat_cnt(df1):
    print(df1.value_counts())
    
# Number of movies released per age
df = mov_ott['Age'].astype('category')

# View the output
cat_cnt(df)


# In[9]:


# How many movies were released per year
# Categorical count
def cat_cnt(df1):
    print(df1.value_counts())
    
# Number of movies released per year
df = mov_ott['Year'].astype('category')

# View the DataFrame
cat_cnt(df)


# In[ ]:




