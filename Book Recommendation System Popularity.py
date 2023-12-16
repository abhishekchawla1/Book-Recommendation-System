#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


books=pd.read_csv(r"C:\Users\ASUS\Downloads\Books.csv")
ratings=pd.read_csv(r"C:\Users\ASUS\Downloads\Ratings.csv")
users=pd.read_csv(r"C:\Users\ASUS\Downloads\Users.csv")


# In[3]:


books


# In[4]:


ratings


# In[5]:


users


# In[6]:


books.shape


# In[7]:


users.shape


# In[8]:


ratings.shape


# In[9]:


books.isnull().sum()


# In[10]:


users.isnull().sum()


# In[11]:


ratings.isnull().sum()


# In[12]:


ratings.duplicated().any()


# In[13]:


users.duplicated().any()


# In[14]:


books.duplicated().any()


# Exploratory Data Analysis

# In[15]:


books.head()


# In[16]:


books.dtypes


# In[17]:


books.dropna(inplace=True)


# In[18]:


books.shape


# In[19]:


books.describe()


# In[20]:


ratings.head()


# In[21]:


users.shape


# Popularity based Recommendation system (Highest average rating considering only those books which have got minimum 250 ratings)

# In[22]:


temp=pd.merge(books,ratings,on='ISBN',how='outer')


# In[23]:


temp.shape


# In[24]:


tempdf=temp.groupby('Book-Title').count()['Book-Rating'].reset_index().rename(columns={'Book-Rating':'number of ratings'})


# In[25]:


tempdf


# In[26]:


average_rating=temp.groupby('Book-Title').mean()['Book-Rating'].reset_index().rename(columns={'Book-Ratings':'Mean of ratings'})


# In[27]:


average_rating


# In[28]:


popularity_df=pd.merge(tempdf,average_rating,on='Book-Title')


# In[29]:


popularity_df


# In[30]:


popularity_df.sort_values(ascending=False,by='number of ratings')


# In[31]:


popularity_df=popularity_df[popularity_df['number of ratings']>250].sort_values(by='Book-Rating',ascending=False)


# In[32]:


popularity_df.shape


# In[33]:


popularity_df


# In[34]:


final_df=pd.merge(popularity_df,books,on='Book-Title')


# In[35]:


final_df


# In[36]:


final_df.drop_duplicates('Book-Title',inplace=True)


# In[37]:


final_df=final_df.drop(columns=['Image-URL-S','Image-URL-M','Image-URL-L','number of ratings']).rename(columns={'Book-Rating':'Average Rating'}).head(50)


# In[38]:


final_df


# In[39]:


final_df.shape


# Top 50 books for recommenation

# In[ ]:




