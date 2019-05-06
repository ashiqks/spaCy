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


# In[3]:


#define the getter function to retrieve the length of each input string
def return_length(doc):
    length_list = []
    for d in doc:
        l = len(d.text)
        length_list.append(l)
    return length_list

#set the extension attribute on the document level with name as 'len_of_str' and the getter function as 'return_length'
Doc.set_extension("len_of_str", getter=return_length, force=True)
#print the output value returned by the extension attribute
print(doc._.len_of_str)


# In[4]:


words_list = ['French', 'France']
#create a getter function to search if any of the words given in the list are found on the input strings
if_in = lambda doc:  any(word in doc.text for word in words_list)
#set the extension attribute with the namem 'if_in' and the getter function 'if_in'
Doc.set_extension('if_in', getter=if_in, force=True)
#print the result of checking 
print(doc._.if_in)


# In[ ]:




