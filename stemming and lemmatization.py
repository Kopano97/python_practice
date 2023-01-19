import spacy
import nltk

print("\n================Stemming in NLTK============\n")
#Stemming in nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["eating", "eats", "eat", "ate", "adjustable", "rafting", "ability", "meeting"]

for word in words:
    print(word, "|",stemmer.stem(word),) 


#--------------------------------------------------------------------------
print("\n================Lemmatization in Spacy============\n")
#lemmatization in spacy    
nlp = spacy.load("en_core_web_sm")

doc = nlp("Mando talked for three hours although talking isn't his thing")

for token in doc:
    print(token, "|", token.lemma_)


#--------------------------------------------------------------------------------------
print("\n================Adding Custom Rule============\n")
#adding custom rule
ar = nlp.get_pipe("attribute_ruler")

ar.add([[{"TEXT":"Bro"}],[{"TEXT":"Brah"}]], {"LEMMA": "Brother"})

doc = nlp("Bro, you waqnna go? Brah, don't say no! I am exhausted")

for token in doc:
    print(token.text, "|", token.lemma_)

# --------------------------------------------------------------------------------------
print("\n================Stemming Exercise 1============\n")  

stemmer = PorterStemmer()

lst_words = ['running', 'painting', 'walking', 'dressing', 'likely', 'children', 'whom', 'good', 'ate', 'fishing']

for word in lst_words:
    print(word, "|",stemmer.stem(word),) 


#--------------------------------------------------------------------------------------
print("\n================Lemmatization Exercise 1============\n")  


nlp = spacy.load("en_core_web_sm")

doc = nlp("running painting walking dressing likely children who good ate fishing")

for token in doc:
    print(token, "|", token.lemma_)

#--------------------------------------------------------------------------------------
print("\n================Stemming and Lemmatization Exercise 2============\n")  

text = """Latha is very multi talented girl.She is good at many skills like dancing, running, singing, playing.She also likes eating Pav Bhagi. she has a 
habit of fishing and swimming too.Besides all this, she is a wonderful at cooking too.
"""


doc = nlp(text)

#Stemming using nltk stemmer
new_words = []
for token in doc:
    new_words.append(stemmer.stem(token.text))


print(' '.join(new_words)) 


#Lemmatization with spacy
new_words = []
for token in doc:
    new_words.append(token.lemma_)


print(' '.join(new_words)) 
