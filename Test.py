from Search import SearchURL
from CSESearch import CSESearch
from MaxURL import TopFiveCommon

KeyWords = ["Ordering Number Elimination", "Computing Order Unknowns"]
urls = CSESearch(KeyWords, "en")
URLOutput = TopFiveCommon(urls)
print(URLOutput)
