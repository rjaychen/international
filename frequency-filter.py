import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import keybert
from keybert import KeyBERT
kw_model = KeyBERT()



def filter_stopwords(text_pathname: str) -> str:
    with open(text_pathname) as f:
        transcript = f.read()
    stop_words = set(stopwords.words('english'))
    stop_words.add(",")
    stop_words.add(".")
    stop_words.add("ok")
    stop_words.add(".")
    transcript = transcript.lower()
    word_tokens = word_tokenize(transcript)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return kw_model.extract_keywords(transcript, keyphrase_ngram_range=(3, 3), stop_words=stop_words,
                              use_maxsum=True, nr_candidates=20, top_n=5)



