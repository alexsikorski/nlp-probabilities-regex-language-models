import nltk
from nltk import FreqDist
from nltk import LaplaceProbDist
from nltk import MLEProbDist

# QUESTION 5
sampleData = "./sampledata.txt"
sampleVocab = "./sampledata.vocab.txt"
sentenceData = "./sampletest.txt"


# sampleData = "./train.txt"
# sampleVocab = "./train.vocab.txt"


def openFile(filePath):
    with open(filePath, "r") as file:  # opens file
        return file.read().split()  # reads and splits


# opened files
textData = openFile(sampleData)
textVocab = openFile(sampleVocab)
sentenceData = openFile(sentenceData)

# reading words
initialOutput = []
sentencesOutput = []
unseen = []  # list for unseen words
for words in textData:
    if words == "<s>":  # start of sentence
        sentence = []
    if words == "</s>":  # end of sentence
        sentencesOutput.append(sentence)  # appends the contents into the list as its own list
    for vocab in textVocab:
        if vocab == words:  # if vocab matches word, append sentence with the word
            sentence.append(words)  # we append to list as a sentence
            initialOutput.append(words)
    if words != vocab:
        unseen.append(words)

# UNK
unseen = list(set(unseen))  # removes duplications
unseen.remove("<s>")  # removes sentence marks
unseen.remove("</s>")
finalUnseen = list(set(unseen) - set(sampleVocab))  # isolates unseen word
# now we know list of unique UNK words, need to find them in given text and check for matches
# when matches are found, replace them with literal text "UNK"
# output new list with addition UNK items, if any are found

finalOutput = []

for words in textData:
    for vocab in textVocab:
        if vocab == words:
            finalOutput.append(words)
    for UNK in finalUnseen:  # for unique unseen values
        if words == UNK:  # if word in input is equivalent to one of these
            finalOutput.append("UNK")  # append UNK as value


def printOutContent(input):
    for a, b in input:  # prints out tuple contents
        print(a + ":" + str(b), end=" ")  # on the same line


theData = finalOutput

# UNIGRAM
fdist1 = FreqDist(theData) + FreqDist({"UNK": 0})
# initialises frequency distribution and adds a frequency of 0  for UNK
# however unseen events get a value of zero and don't get smoothed...
# Unsmoothed
unSmoothed = MLEProbDist(fdist1)  # initialises probability distribution
unSmoothProb = [(x, unSmoothed.prob(x)) for x in unSmoothed.samples()]

# Smoothed
Smoothed = LaplaceProbDist(fdist1)
SmoothedProb = [(x, Smoothed.prob(x)) for x in Smoothed.samples()]

# QUESTION 5
# BIGRAM
bigram = list(nltk.ngrams(theData, 2))
fdist2 = FreqDist(bigram)

# Unsmoothed
unSmoothedBigram = MLEProbDist(fdist2)
unSmoothedBigramProb = [(x, unSmoothedBigram.prob(x)) for x in unSmoothedBigram.samples()]

# Smoothed
smoothedBigram = LaplaceProbDist(fdist2)
smoothedBigramProb = [(x, smoothedBigram.prob(x)) for x in smoothedBigram.samples()]

# PRINTING
print()
print("---------------- Toy dataset ----------------")
print("=== UNIGRAM MODEL ===")
print("- Unsmoothed  -")
printOutContent(unSmoothProb)
print("\n- Smoothed  -")
printOutContent(SmoothedProb)
print()
print("=== BIGRAM MODEL ===")
print("- Unsmoothed  -")
print(unSmoothedBigramProb)
print("- Smoothed  -")
print(smoothedBigramProb)
