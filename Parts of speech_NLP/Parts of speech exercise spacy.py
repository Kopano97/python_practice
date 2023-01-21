import spacy

nlp = spacy.load("en_core_web_sm")


# Open the file
with open('inflation.txt', 'r') as file:
    # Read the contents of the file
    contents = file.read()
    # Print the contents
   


doc = nlp(contents)

#extract NOUNs in a python list
filterted_nouns = []
for token in doc:
    if token.pos_ in ["NOUN"]:
        filterted_nouns.append(token)
       
print(filterted_nouns)


#Extract all numbers (NUM POS type) in a python list
filterted_numbers = []
for token in doc:
    if token.pos_ in ["NUM"]:
        filterted_numbers.append(token)
       
print(filterted_numbers)


#Print a count of all POS tags in this story
count = doc.count_by(spacy.attrs.POS)

for k, v in count.items():
    print(doc.vocab[k].text," | ",v)