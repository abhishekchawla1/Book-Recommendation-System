#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


books=pd.read_csv(r"C:\Users\ASUS\Downloads\Books.csv")
users=pd.read_csv(r"C:\Users\ASUS\Downloads\Users.csv")
ratings=pd.read_csv(r"C:\Users\ASUS\Downloads\Ratings.csv")


# In[3]:


books.head()


# In[4]:


ratings.head()


# In[5]:


users.head()


# In[6]:


tempdf=pd.merge(books,ratings,on='ISBN')


# In[7]:


tempdf


# In[8]:


x=tempdf.groupby('User-ID').count()['Book-Rating']>200


# In[9]:


useful_users=x[x].index


# In[10]:


useful_users.shape


# In[11]:


df=tempdf[tempdf['User-ID'].isin(useful_users)]


# In[12]:


y=df.groupby('Book-Title').count()['Book-Rating']>50


# In[13]:


useful_books=y[y].index


# In[14]:


useful_books.shape


# In[15]:


df=df[df['Book-Title'].isin(useful_books)]


# In[16]:


df


# In[17]:


pivot=df.pivot_table(index='Book-Title',columns='User-ID',values=['Book-Rating'])


# In[18]:


pivot


# In[20]:


pivot.fillna(0,inplace=True)


# In[21]:


pivot


# In[22]:


from sklearn.metrics.pairwise import cosine_similarity


# In[23]:


similarity_scores=cosine_similarity(pivot)


# In[25]:


similarity_scores.shape


# In[39]:


def book_rec(x):
    index=np.where(pivot.index==x)[0][0]
    similar_books=sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]
    for s in similar_books:
        print(pivot.index[s[0]])
        


# In[40]:


book_rec('Animal Farm')


# In[43]:


book_rec('1984')


# In[44]:


book_rec('Harry Potter and the Goblet of Fire (Book 4)')


# In[53]:


book_rec('Naked')


# In[56]:


pivot.index.values


# In[58]:


book_rec('The Alchemist: A Fable About Following Your Dream')


# In[ ]:




