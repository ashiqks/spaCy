#!/usr/bin/env python
# coding: utf-8

# In[362]:


#import necessary modules and tools 
import spacy
from spacy.matcher import Matcher #import the Matcher class from spacy
from spacy.tokens import Span #import the Span class to extract the words from the document object

#Language class with the English model 'en_core_web_sm' is loaded
nlp = spacy.load("en_core_web_sm")
#instantiate a new Matcher class object 
matcher = Matcher(nlp.vocab)

#define the pattern
pattern = [{'LOWER': 'computer', 'POS': 'NOUN'},
             {'POS':{'NOT_IN': ['VERB']}}]

#add the pattern to the previously created matcher object
matcher.add("Matching", None, pattern)

#The input text string is converted to a Document object
doc = nlp("Computer programming is the process of writing instructions that get executed by computers. The instructions, also known as code, are written in a programming language which the computer can understand and use to perform a task or solve a problem. Basic computer programming involves the analysis of a problem and development of a logical sequence of instructions to solve it. There can be numerous paths to a solution and the computer programmer seeks to design and code that which is most efficient. Among the programmer’s tasks are understanding requirements, determining the right programming language to use, designing or architecting the solution, coding, testing, debugging and writing documentation so that the solution can be easily understood by other programmers.Computer programming is at the heart of computer science. It is the implementation portion of software development, application development and software engineering efforts, transforming ideas and theories into actual, working solutions.")

#call the matcher object the document object and it will return match_id, start and stop indexes of the matched words
matches = matcher(doc)

#print the matched results and extract out the results
for match_id, start, end in matches:
    # Get the string representation 
    string_id = nlp.vocab.strings[match_id]  
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)

