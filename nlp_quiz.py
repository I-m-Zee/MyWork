# -*- coding: utf-8 -*-
"""NLP_Quiz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Flj7yp-qXIMvy7sbqx07-6aLDlB1fHi

#Part-1

#Import Required Modules
"""

import pandas as pd
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import re

"""#File Loading"""

df=pd.read_csv('tweets.csv',encoding='latin1', header=None)

"""#Selecting First 2 Columns"""

df=df[[1,2]]
df.head()

"""#Renaming Columns"""

df.columns=['ser','tweets']
df.head()

"""#Count Words"""

df['wordCount']=df.tweets.apply(lambda x: len(str(x).split()))

df.head()

"""#Count Characters"""

df['charCount']=df.tweets.apply(lambda x:len(x))

df.head()

"""#Function to Count Avg Word Lenght"""

def avg_word_len(x):
  words = x.split()
  char_len = 0
  for word in words:
    char_len = char_len+len(word)
  return char_len / len(words)

"""#Count Avg Word Length"""

df['avg_word_len1'] = df.tweets.apply(lambda x: avg_word_len(x))

df['avg_word_len']=df.tweets.apply(lambda x: len(x) / len(str(x).split()))

df.head()

"""#Count StopWords"""

df['stop_words_len'] = df.tweets.apply(lambda x: len([t for t in x.split() if t in STOP_WORDS]))

df.head()

"""#Count Words strat with '#' & '@'"""

df['hashCount']=df.tweets.apply(lambda x: len([t for t in x.split() if t.startswith('#')]))
df['mentionCounts']=df.tweets.apply(lambda x: len([t for t in x.split() if t.startswith('@')]))

df.head(20)

"""#If String has Numeric Character"""

df['hasNumeric'] = df.tweets.apply(lambda x: bool(re.search(r'\d', x)))

"""#Numberic Characters Are"""

df['numericsFound'] = df.tweets.apply(lambda x: ''.join([t for t in re.findall(r'\d', x)]))

df.head(20)

"""#Count Upper Case Words"""

df['upperCaseWords'] = df.tweets.apply(lambda x: len([t for t in x.split() if re.search(r'([A-Z])', t)]))

df.head(20)

"""#Save file"""

df.to_csv('myWord.csv', index=None, header=True)

"""#Part-2

#Convert tweets column to Lower case
"""

df.tweets = df.tweets.str.lower()

df.head()

"""#Find Emails"""

df["foundEmail"] = df.tweets.apply(lambda x: bool(re.search(r'([\w.]+)/s([/@]+)/s([\w.]+)',x)))

df["countEmail"] = df.tweets.apply(lambda x: len([t for t in x.split() if re.search(r'([\w.]+)/s([/@]+)/s([\w.]+)', x)]))

df.head(20)

df.countEmail.describe()

df["foundURL"] = df.tweets.apply(lambda x: bool(re.search(r'\b(https)\b\/*([a-z]*)\/*([a-zA-Z0-9]*)',x)))

df["countURL"] = df.tweets.apply(lambda x: len([t for t in x.split() if re.search(r'\b(https)\b\/*([a-z]*)\/*([a-zA-Z0-9]*)', x)]))

df.head(20)

"""#Clean Text Function"""

def clean_text(text):
    #Remove RT
    text = re.sub(r'rt', '', text)
    
    #Remove HTML tags
    text = re.sub(r'[<]+[a-z0-9+]+[>]','', text)

    #Remove Links
    text = re.sub(r'\b(https)\b\/*([a-z]*)\/*([a-z0-9]*)','',text)

    #Remove Emails
    text = re.sub(r'([\w.]+)/s([/@]+)/s([\w.]+)','',text)
    
    #Remove All Special Characters
    text = re.sub(r'[?!.;:,#@-]', '', text)

    #Remove Extra Spaces
    text = re.sub(' +',' ',text)

    return text

df.tweets = df.tweets.apply(lambda x: clean_text(x))

df.head(20)

"""#Count Word Frequencies to Remove Stops Words"""

df['wordFreq'] = df.tweets.apply(lambda x: pd.Series(x.split()).value_counts())