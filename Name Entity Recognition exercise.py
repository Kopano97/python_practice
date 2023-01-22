import spacy
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")

#Exercice 1
#extract all loiocations
text = """Kiran want to know the famous foods in each state of India. So, he opened Google and search for this question. Google showed that
in Delhi it is Chaat, in Gujarat it is Dal Dhokli, in Tamilnadu it is Pongal, in Andhrapradesh it is Biryani, in Assam it is Papaya Khar,
in Bihar it is Litti Chowkha and so on for all other states"""

doc = nlp(text)



s1 = Span(doc, 54, 55, label="GPE")

doc.set_ents([s1], default="unmodified")

filtered_locations = []
for ent in doc.ents:
    if ent.label_ in "GPE":
        filtered_locations.append(ent.text)
        
print(filtered_locations)


#Exercise 2
#extract all dates
text = """Sachin Tendulkar was born on 24 April 1973, Virat Kholi was born on 5 November 1988, Dhoni was born on 7 July 1981
and finally Ricky ponting was born on 19 December 1974."""

doc = nlp(text)
all_birth_dates = []
for ent in doc.ents:
    if ent.label_ in "DATE":
        all_birth_dates.append(ent.text)

print(all_birth_dates)