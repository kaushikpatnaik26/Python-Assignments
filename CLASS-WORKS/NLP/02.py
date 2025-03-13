from textblob import Word
w = Word('Similarities')
w2 = Word('seggs')
print(w2.spellcheck()) #corrects spelling errors
print(w2.correct()) #return the correct probable word 
print(w.singularize()) #return the singular form of the words
print(w.stem()) #removes prefix and suffix of the word
print(w.lemmatize()) #takes u back to root word


