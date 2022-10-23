import requests

def CSESearch(Queries, Language):
    SEARCH_ENGINE_ID = "53fb634b0dd564827"
    if(Language == "en"):
        SEARCH_ENGINE_ID = "746fa251ea3354591"
    if(Language == "es"):
        SEARCH_ENGINE_ID = "f317c1554c49a487c"
    if(Language == "zh-TW"):
        SEARCH_ENGINE_ID = "53fb634b0dd564827"
    
    
    urls = []
    for k in Queries:
        API_KEY = "AIzaSyBPbbZVAapo_FQh_SnlUBFJhPLKQ_ya-AU"

        query = k

        page = 1
        # constructing the URL
        # doc: https://developers.google.com/custom-search/v1/using_rest
        # calculating start, (page=2) => (start=11), (page=3) => (start=21)
        start = (page - 1) * 10 + 1
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

        data = requests.get(url).json()
        # get the result items
        search_items = data.get("items")
        # iterate over 5 results found
        for i, search_item in enumerate(search_items, start=1):
            try:
                long_description = search_item["pagemap"]["metatags"][0]["og:description"]
            except KeyError:
                long_description = "N/A"
            # get the page title
            #title = search_item.get("title")
            # alternatively, you can get the HTML snippet (bolded keywords)
            #html_snippet = search_item.get("htmlSnippet")
            # extract the page url
            link = search_item.get("link")
            # print the results
            urls.append(link)
            if i>=8: #only have 5 results
                break
    return urls