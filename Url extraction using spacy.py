import spacy


text='''
Look for data to help you address the question. Governments are good
sources because data from public research is often freely available. Good
places to start include http://www.data.gov/, and http://www.science.
gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
and the European Social Survey at http://www.europeansocialsurvey.org/.
'''

nlp = spacy.blank("en")

doc = nlp(text)
urls = []
for token in doc:
    if token.like_url:
        urls.append(token.text)

print(urls)