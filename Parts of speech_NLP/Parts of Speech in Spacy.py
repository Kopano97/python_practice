import spacy

nlp = spacy.load("en_core_web_sm")

# doc = nlp("Wow! Elon flew to mars yesterday. He carried briyani masala with him")

# for token in doc:
#     print(token,"|",token.pos_, "|",  spacy.explain(token.pos_),"|", token.tag_, "|",  spacy.explain(token.tag_))



#nlp on microsoft earning report

earnings_text = """ Microsoft Corp. today announced the following results for the quarter ended September 30, 2022, as compared to the corresponding period of last fiscal year:

·        Revenue was $50.1 billion and increased 11% (up 16% in constant currency)

·        Operating income was $21.5 billion and increased 6% (up 15% in constant currency)

·        Net income was $17.6 billion and decreased 14% (down 8% in constant currency)

·        Diluted earnings per share was $2.35 and decreased 13% (down 7% in constant currency)

“In a world facing increasing headwinds, digital technology is the ultimate tailwind,” said Satya Nadella, chairman and chief executive officer of Microsoft. “In this environment, we’re focused on helping our customers do more with less, while investing in secular growth areas and managing our cost structure in a disciplined way."""""

doc = nlp(earnings_text)

# filterted_tokens = []
# for token in doc:
#     if token.pos_ not in ["SPACE", "X", "PUNCT"]:
#         filterted_tokens.append(token)

# print(filterted_tokens[:20])


count = doc.count_by(spacy.attrs.POS)
print(count)

for k, v in count.items():
    print(doc.vocab[k].text," | ",v)