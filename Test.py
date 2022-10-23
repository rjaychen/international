from Search import SearchURL
from CSESearch import CSESearch
from MaxURL import TopFiveCommon
from google_translate import sourceTranslate




# KeyWords = ["hello", "Goodbye", "Sorry"]
# words = KeyWords
# for i, KeyWords in enumerate(KeyWords):
#     words[i] = sourceTranslate(KeyWords, "en", "zh-tw")

# print(words)
# # urls = CSESearch(KeyWords, "en")

urls = ["h", "k", "d", "d", ""]
URLOutput = TopFiveCommon(urls)
print(URLOutput)

