#!/usr/bin/env python
# coding: utf-8

# In[30]:


#import necessary packages and tools
import spacy
from spacy.tokens import Token #import Token class from spacy

#Language class with the English model 'en_core_web_sm' is loaded
nlp = spacy.load('en_core_web_sm')
#The input text string is converted to Document object 
doc = nlp("The French Revolution was a period of time in France when the people overthrew the monarchy and took control of the government.")

#Define the extension attribute on the token level with name as #'context' and default value as false
Token.set_extension('context', default=False, force=True)

#Try printing the each token on the Document object and the stored #value by the extension attribute. All the values default to 'False'
for d in doc:
    print(d.text, d._.context)
    
#The entity type of previous, next and self tokens are computed and #is set by the 'set' function
for i, d in enumerate(doc):
    if i > 0 and (i < len(doc) - 1):
        meaning = '|' + doc[i-1].ent_type_ + '-' + d.ent_type_ + '-' + doc[i+1].ent_type_ 
        d._.set('context', meaning)
        
#Printing the tokens again to see the modified values
for d in doc:
    print(d.text, d._.context)
    
Token.has_extension('context') #returns True
Token.remove_extension('context') #removes the attribute
Token.has_extension('context') #returns False


# In[ ]:




