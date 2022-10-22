try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

 
def SearchURL(KeyWords):  #outputs list of google searchers 
    websites = ["Wikipedia", "Khan Academy"]
    URLs = []
    for k in KeyWords:
        for i in websites:
            query = k + i
            for j in search(query, tld=".com", num=1, stop=2, pause=.01):
                URLs.append(j)
    return URLs
