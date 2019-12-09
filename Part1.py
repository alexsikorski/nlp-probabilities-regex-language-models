from urllib import request

import nltk
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# (Q1)
websiteURL = "https://www.theguardian.com/music/2018/oct/19/while-my-guitar-gently-weeps-beatles-george-harrison"  # sets url
rawText = BeautifulSoup((request.urlopen(websiteURL).read().decode("utf8")), "html.parser")  # obtains raw text
textArticle = rawText.find("article").get_text()  # isolates wanted text from article
lmtzr = WordNetLemmatizer()

# Before removing punctuation/lowercasing/lemmatization:
aTokens = word_tokenize(textArticle)  # tokenizes to list
aTypes = set(aTokens)  # types set
print("Question 1")
print()
print("This text contains types BEFORE removing punctuation, lowercasing and lemmatization:", len(aTypes))
print("This text contains tokens BEFORE removing punctuation, lowercasing and lemmatization:", len(aTokens))
print("10 token index values in aTokens at 290:300:", aTokens[290:300])
print()

# PRE PROCESS
# Lowercasing
lowerTextArticle = textArticle.lower()  # sets lowercase text article
aTokens_Lower = word_tokenize(lowerTextArticle)  # creates tokens for lowercased article
aTypes_Lower = set(aTokens_Lower)
# Removed punctuation
aTokens_NoPunc = [word for word in aTokens if word.isalpha()]  # removes all non alphabetic characters
aTypes_NoPunc = set(aTokens_NoPunc)
# Lowercasing and removed punctuation
aTokens_Lower_NoPunc = [word for word in aTokens_Lower if
                        word.isalpha()]  # removes all punctuation in lowercased tokens
aTypes_Lower_NoPunc = set(aTokens_Lower_NoPunc)

# LEMMATIZATION
# After lemmatization
aTokens_Lem = [lmtzr.lemmatize(word) for word in aTokens]
aTypes_Lem = set(aTokens_Lem)

print("This text contains types AFTER lemmatization: ", len(aTypes_Lem))
print("This text contains tokens AFTER lemmatization: ", len(aTokens_Lem))
print("10 token values in aTokens_Lem at 290:300:", aTokens_Lem[290:300])
print()

# After lemmatization and lowercasing
aTokens_Lem_Lower = [lmtzr.lemmatize(word) for word in aTokens_Lower]
aTypes_Lem_Lower = set(aTokens_Lem_Lower)

print("This text contains types AFTER lemmatization and lowercasing: ", len(aTypes_Lem_Lower))
print("This text contains tokens AFTER lemmatization and lowercasing: ", len(aTokens_Lem_Lower))
print("10 token values in aTokens_Lem_Lower at 290:300:", aTokens_Lem_Lower[290:300])
print()

# After lemmatization lowercasing and removing punctuation
aTokens_Lem_Lower_NoPunc = [lmtzr.lemmatize(word) for word in aTokens_Lower_NoPunc]
aTypes_Lem_Lower_NoPunc = set(aTokens_Lem_Lower_NoPunc)

print("This text contains types AFTER lemmatization, removing punctuation and lowercasing: ",
      len(aTypes_Lem_Lower_NoPunc))
print("This text contains tokens AFTER lemmatization, removing punctuation and lowercasing: ",
      len(aTokens_Lem_Lower_NoPunc))
print("10 token values in aTokens_Lem_Lower_NoPunc at 290:300:", aTokens_Lem_Lower_NoPunc[290:300])
print("""



Question 2
""")

# (Q2)
# POS tagging
aTokens_Tagged = nltk.pos_tag(aTokens)
print("Displaying from aTokens [269:270]:", aTokens_Tagged[269:270])
print(""" - This error displays a quotation mark as a NNP (proper noun) which it is not.
It should instead display a . in the second tuple field as it is not a word.
This is the reason why punctuation is ignored.

""")
aTokens_Lem_Lower_NoPunc_Tagged = nltk.pos_tag(aTokens_Lem_Lower_NoPunc)
print("Displaying from aTokens_Lem_Lower_NoPunc_Tagged [269:270]:", aTokens_Lem_Lower_NoPunc_Tagged[269:270])
print(""" - This error displays the name eric as a JJ (adjective) which it is not.
As the first letter is lowercased, POS tagging does not determine it as a name (NNP).
This displays the negative effect of preprocessing.

""")
