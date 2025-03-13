from textblob import Textblob
# from nltk.corpus import stopwords
text = "today is a good day. Tommorow is likely to be a bad day. "
blob = Textblob(text)
print(blob.sentences)