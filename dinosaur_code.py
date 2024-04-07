import requests
from bs4 import BeautifulSoup

#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

import nltk
import nltk.corpus
#from nltk import word_tokenize
#from nltk.corpus import stopwords

#import pandas as pd
#from nltk.tokenize import word_tokenize
#nltk.download('punkt')

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

#from nltk import ne_chunk


#not needed anymore
text = "In Brazil they drive on the right-hand side of the road. Brazil has a large coastli"

#not needed anymore
# token = word_tokenize(text) #method to make list
#print(token)hom

#not needed anymore
# from nltk.probability import FreqDist
# fdist = FreqDist(token) #make dictionary counting the frequency of words in a song
# fdist

#not needed anymore
# fdist1 = fdist.most_common(10) # find top 10 frequency words
# fdist1

#apply when data cleaning
pst = PorterStemmer() # break down the word into a simpler form. For example, waiting & waited --> wait
#print(pst.stem("waiting"))

#apply when data cleaning
lemmatizer = WordNetLemmatizer() #turns plural word to singular
#print("rocks :", lemmatizer.lemmatize("rocks"))
#print("corpora :", lemmatizer.lemmatize("corpora"))

# #apply when data cleaning
# a = set(stopwords.words('english')) # identify stop words and not include them in the data
# text = "Cristiano Ronaldo was born on February 5, 1985, in Funchal, Madeira, Portugal."
# text1 = word_tokenize(text.lower())
# #print(text1)
# stopwords = [x for x in text1 if x not in a]
# #print(stopwords)


#Part of Speech Tagging: make the system understand that what all words are ‘nouns’, ‘pronouns’, etc., for better analysis

# text = "vote to choose a particular man or a group (party) to represent them in parliament"
# #Tokenize the text
# tex = word_tokenize(text)
# for token in tex:
#     print(nltk.pos_tag([token])) # change to return or assign to a variable later


# text = "vote to choose a particular man or a group (party) to represent them in parliament"
# token = word_tokenize(text)
# tags = nltk.pos_tag(token)
# chunk = ne_chunk(tags)
# chunk #try printing on jupyter notebook

# text = "We saw the yellow dog"
# token = word_tokenize(text)
# tags = nltk.pos_tag(token)
# reg = "NP: {<DT>?<JJ>*<NN>}"
# a = nltk.RegexpParser(reg)
# result = a.parse(tags)
# print(result)
# #output == (S We/PRP saw/VBD (NP the/DT yellow/JJ dog/NN))

# #start of VADER sentiment analysis
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# #function to print various sentiments of the sentence

# def sentiment_scores(sentence):
#     #creating object
#     sia_obj = SentimentIntensityAnalyzer()
#     #polarity_scores method of SentimentIntensityAnalyzer
#     # object gives a sentiment dictionary which contains pos, neg, neu, and compound scores.
#     sentiment_dict = sia_obj.polarity_scores(sentence)    
#     print("Overall sentiment dictionary is : ", sentiment_dict)
#     print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
#     print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
#     print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
#     print("Sentence Overall Rated As", end = " ")
#     #conditions to check whether the sentiment's stats about positivity, negativity, and neutrality
#     if sentiment_dict['compound'] >= 0.05 :
#         print("Positive")
#     elif sentiment_dict['compound'] <= - 0.05 :
#         print("Negative")
#     else :
#         print("Neutral")


# #driver code for analysis
# if __name__ == "__main__":
#     print("Text Selected for VADER Sentimental Analysis :")
#     sentence1 = ("I was very sad yesterday because I fell off the stairs but I ate chocolate so this hyped me up.")
#     print(sentence1)

# sentiment_scores(sentence1)

