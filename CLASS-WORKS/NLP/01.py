from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
text = "today is a good day.Tomorrow is likely to be a bad day."
text2 = "ghaswarya"
text3 = "Thalla"
blob1 = TextBlob(text)
blob2 = TextBlob(text2,analyzer = NaiveBayesAnalyzer())
blob3 = TextBlob(text3,analyzer = NaiveBayesAnalyzer())

print(blob2.sentiment)
print(blob3.sentiment)

# print(blob1.sentences)
# print(blob1.words)
