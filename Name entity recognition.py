import spacy

nlp = spacy.load("en_core_web_sm")


doc = nlp("Tesla Inc is going to acquire Twitter for $45 billion")


from spacy.tokens import Span

s1 = Span(doc, 0, 1, label="ORG")
s2 = Span(doc, 6, 7, label="ORG")
doc.set_ents([s1, s2], default="unmodified")

for ent in doc.ents:
    print(ent.text, "| ",ent.label_, "| ", spacy.explain(ent.label_))


# from spacy import displacy
# displacy.render(doc, style="ent")  


doc2 = nlp("Michael Bloomberg founded Bloomberg Inc in 1982")


for ent in doc2.ents:
    print(ent.text, "| ",ent.label_, "| ", spacy.explain(ent.label_))

