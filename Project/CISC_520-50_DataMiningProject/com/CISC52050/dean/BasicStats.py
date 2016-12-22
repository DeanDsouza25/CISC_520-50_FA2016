'''
@author: Dean D'souza
'''
# Loading necessary Libraries
from __future__ import division
import nltk
from nltk.text import Text
from ProjectTokenizer import pToken
from ProjectTagger import pTagger
from nltk.corpus import stopwords

# Loading all text data
txtFile=open('C:/Users/demon/OneDrive/Documents/GitHub/CISC_520-50_FA2016/Project/data/AllText.txt','r')
tempTxt = txtFile.read()
txtFile.close()

# Tokenizing the text
pTok1 = pToken(tempTxt)

# Basic Statistics of the text without removing stopwords
#print("Number of Words : "+str(len(pTok1)))
#print("Number of Unique Words : "+str(len(set(pTok1))))
#print("Lexical Diversity : "+str(len(pTok1)/len(set(pTok1))))

# Basic Statistics after removing stopwords
#pTok2 = [w.lower() for w in pTok1 if w not in stopwords.words('english')]
#print("Number of Words : "+str(len(pTok2)))
#print("Number of Unique Words : "+str(len(set(pTok2))))
#print("Lexical Diversity : "+str(len(pTok2)/len(set(pTok2))))

# Converting to nltk.text.Text form to easily create Frequency Distribution 
nText = Text(pTok1)
fdistv = nltk.FreqDist(nText)
vocab = fdistv.keys()

# List of top most tokens
#print(vocab[:50])

# Cummulative Frequency Plot of the top most tokens
#fdistv.plot(50)
#fdistv.plot(50,cumulative=True)

# Collocations (a.k.a. Words occurring together with a frequency considered greater than chance)
#print(nText.collocations())

# Tagging the tokens with Part-of-Speech tag
taggedTok = pTagger(vocab)
tags = []
for tag in taggedTok:
    for t2 in tag:
        if isinstance(t2, tuple):
            tags.append(t2[1])
        elif t2 in ['link','punct','UserID','htag','email','emoji','num']:
            tags.append(t2)

# Frequency Distribution of tags
fdisttag=nltk.FreqDist(tags)
#fdisttag.tabulate()

# Frequency Distribution Plot of tags
fdisttag.plot(50)
