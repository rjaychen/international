import keybert
from keybert import KeyBERT


kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc)
print(kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 1), stop_words=None))