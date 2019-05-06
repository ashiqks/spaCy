#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import necessary modules
import spacy
from spacy.matcher import PhraseMatcher #import the PhraseMatcher class

# Language class with the English model 'en_core_web_sm' is loaded
nlp = spacy.load('en_core_web_sm')

# create the PhraseMatcher object
matcher = PhraseMatcher(nlp.vocab, attr='LOWER')

# the list containing the pharses to be matched
terminology_list = ["Machine Learning", "Hidden Structure", "Unlabeled Data"]
# convert the phrases into document object using nlp.make_doc to speed up.
patterns = [nlp.make_doc(text) for text in terminology_list]

# add the patterns to the matcher object without any callbacks
matcher.add("Phrase Matching", None, *patterns)

# the input text string is converted to a Document object
doc = nlp("Supervised machine learning algorithms can apply what has been learned in the past to new data using labeled examples to predict future events. Starting from the analysis of a known training dataset, the learning algorithm produces an inferred function to make predictions about the output values. The system is able to provide targets for any new input after sufficient training. The learning algorithm can also compare its output with the correct, intended output and find errors in order to modify the model accordingly. In contrast, unsupervised machine learning algorithms are used when the information used to train is neither classified nor labeled. Unsupervised learning studies how systems can infer a function to describe a hidden structure from unlabeled data. The system doesn’t figure out the right output, but it explores the data and can draw inferences from datasets to describe hidden structures from unlabeled data. Semi-supervised machine learning algorithms fall somewhere in between supervised and unsupervised learning, since they use both labeled and unlabeled data for training – typically a small amount of labeled data and a large amount of unlabeled data. The systems that use this method are able to considerably improve learning accuracy. Usually, semi-supervised learning is chosen when the acquired labeled data requires skilled and relevant resources in order to train it / learn from it. Otherwise, acquiring unlabeled data generally doesn’t require additional resources.")

# call the matcher objec on the document object to return the results
matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)

