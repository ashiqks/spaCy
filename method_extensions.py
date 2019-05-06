#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import necessary tools and packages
import spacy
from spacy.tokens import Doc #import Doc class from spacy


# In[2]:


#Language class with the English model 'en_core_web_sm' is loaded
nlp = spacy.load('en_core_web_sm')
#The input text string is converted to a Document object
doc = nlp("The French Revolution was a period of time in France when the people overthrew the monarchy and took control of the government. The French Revolution lasted 10 years from 1789 to 1799. It began on July 14, 1789 when revolutionaries stormed a prison called the Bastille. The revolution came to an end 1799 when a general named Napoleon overthrew the revolutionary government and established the French Consulate (with Napoleon as leader).")


# In[6]:


#create a function  filter based on the size of each element to be used as an object method
def size_filter(doc, size):
    filtered_list = []
    for d in doc:
        if len(d.text) > size:
            filtered_list.append(d.text)
    return filtered_list

#Define the extension attribute 
Doc.set_extension("wordsize_filter", method=size_filter, force=True)


# In[10]:


#print the result with the user input '6'
print(doc._.wordsize_filter(6))


# In[8]:


#define another function to filter based on user input entity types
def entity_filter(doc, entity_list):
    filtered_list = []
    for d in doc:
        if d.ent_type_ in entity_list and not d.is_punct:
            filtered_list.append((d.text, d.ent_type_))
    return filtered_list

#set the extension attribute
Doc.set_extension("entity_filters", method=entity_filter, force=True)


# In[11]:


entity_list = ['EVENT', 'DATE']

#print the filtered result with the user given list of entity types
print(doc._.entity_filters(entity_list))


# In[ ]:




