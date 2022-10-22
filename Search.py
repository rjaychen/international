try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
 
 
 
websites = ["Wikipedia", "Khan Academy", "Encylopedia Britanica"]

# to search
for i in websites:
    query = "magnetic fields" + i

    for j in search(query, tld="co.in", num=2, stop=5, pause=1):
        print(j)