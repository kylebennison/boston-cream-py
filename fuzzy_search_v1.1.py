#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Sample list of results options
word_database = ['Philadelphia Eagles', 'Penn State Nittany Lions', 'Baltimore Ravens', 'St. Louis Cardinals']

# Make lowercase
word_database = [x.lower() for x in word_database]

print(word_database)


# In[10]:


sample_search = input('Enter a search term: ')

sample_search = sample_search.lower()

print(sample_search)


# In[11]:


word_dict = dict()

for i in range(len(word_database)):
    print('Word ', i)
    
    word_scores = list()
    
    for n in range(len(sample_search)):
        print('Letter ', n)
        try:
            if sample_search[n] == word_database[i][n]:
                word_scores.append(1)
                
            elif sample_search[n] == word_database[i][n-1] or sample_search[n] == word_database[i][n+1]:
                word_scores.append(.5)
                
            elif sample_search[n] in word_database[i]:
                word_scores.append(.1)
                
            else:
                word_scores.append(0)
        except:
            word_scores.append(None)
            continue
            
    word_dict[i] = word_scores
            
print(word_dict)


# In[12]:


import numpy as np
import pandas as pd


# In[13]:


scores = pd.DataFrame.from_dict(word_dict).mean()

scores


# In[14]:


sorted_scores = scores.sort_values(ascending=False)

sorted_scores = pd.DataFrame(sorted_scores)

sorted_scores


# In[15]:


word_database = pd.Series(word_database, name = "word_database")


# In[16]:


sorted_scores.join(word_database)

