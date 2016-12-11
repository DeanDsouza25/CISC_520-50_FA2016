'''
@author: Dean D'souza
'''
# Importing Required Libraries
import csv
import nltk
import random
from ProjectTokenizer import pToken
from ProjectTagger import pTagger
from nltk.corpus import stopwords
from nltk.text import Text
from nltk.classify.util import apply_features

# Declaring empty holder for trainign set
allTweets=[]

# Reading in the data from the file
csvfile = open('C:/Users/demon/OneDrive/Documents/GitHub/CISC_520-50_FA2016/Project/data/FinalData.csv')
reader = csv.DictReader(csvfile, dialect='excel', fieldnames=['sentiment', 'ID', 'date', 'query', 'author', 'content'])
for row in reader:
    allTweets.append((row['content'], row['sentiment']))
csvfile.close()

# Separating the training and testing data
sep = int(0.8*len(allTweets))
random.shuffle(allTweets)
trainTweets = allTweets[:sep]
testTweets = allTweets[sep:]
print(testTweets)

# Creating a list of tokenized words and sentiment
tweets = []
for (words,sentiment) in trainTweets:
    filter1Words=([w.lower() for w in pToken(words) if len(w) >= 2 and w not in stopwords.words('english')])
    filteredWords = Text([e for (e,t) in pTagger(filter1Words) if  t not in ['email','punct','link']])
    tweets.append((filteredWords,sentiment))

# Function to create list of all words
def getWordsInTweets(tweets):
    wordsInTweets=[]
    for (word, sentiment) in tweets:
        wordsInTweets.append(word)
    return wordsInTweets

# Function to get frequency distribution to be used as feature
def getWordFeatures(tWordList):
    tWordList = nltk.FreqDist(tWordList)
    wordFeats = tWordList.keys()
    return wordFeats

tweetsFeats = getWordFeatures(getWordsInTweets(tweets))

# Function to extract features from new tweets
def FeatExt(ttweet):
    tagdWords = pTagger(pToken(ttweet))
    tWords = (e for (e,t) in tagdWords if t not in ['email','DT','punct', 'link'] and len(e)>=2)
    feat = {}
    for e in tweetsFeats:
        feat['contains(%s)' % e] = (e in tWords)
    if [e for (e,t) in tagdWords if t in ['punct']] != []:
        feat['punct'] = max([len(e) for (e,t) in tagdWords if t in ['punct']])
    feat['htag'] = sum([1 for (e,t) in tagdWords if t in ['htag']])
    return feat

# Building the Naive Bayes classifier
trainTweetsApplied = nltk.classify.apply_features(FeatExt, trainTweets)
classifier1 = nltk.NaiveBayesClassifier.train(trainTweetsApplied)
print(classifier1.show_most_informative_features(30))

# Building Decision Tree Classifier
#classifier2 = nltk.DecisionTreeClassifier.train(trainTweetsApplied)
#print(classifier2.pseudocode(depth=5))

# Evaluating the classifiers
print("For Naive Bayes Classifier:")
print(nltk.classify.accuracy(classifier1,apply_features(FeatExt,testTweets)))

#print("For Decision Tree Classifier:")
#print(nltk.classify.accuracy(classifier2,testTweets))