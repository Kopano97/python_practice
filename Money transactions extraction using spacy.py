import spacy 

text = "Tony gave two $ to Peter, Bruce gave 500 € to Steve"


nlp = spacy.blank("en")

doc = nlp(text)
for i in range(len(doc)):
    if doc[i].like_num and doc[i+1].is_currency:
        print(doc[i].text + ' ' + doc[i+1].text+'\n')
        


