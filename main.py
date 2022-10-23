from flask import Flask, request, jsonify 
from flask_cors import CORS
from CSESearch import CSESearch
from MaxURL import TopFiveCommon
from frequency_filter import frequency_filter_stopwords
from google_translate import sourceTranslate
app = Flask(__name__)

cors = CORS(app)

#Create the receiver API POST endpoint:
@app.route("/receiver", methods=["POST"])
def postME():
   data = request.get_json()
   keywords = frequency_filter_stopwords(data[0]) #Filter out for keywords first

   #keywords 
   print(data[2])
   #Translation function
   Translatedwords = keywords
   for i, keywords in enumerate(keywords):
      Translatedwords[i] = sourceTranslate(keywords, data[1], data[2])

   keywords = Translatedwords
   #print(keywords)
   
   Allurls = CSESearch(keywords, data[2])   #Search on Custom Search Engine using the keywords
   urls = TopFiveCommon(Allurls) #Find top 5 urls given keyworcs 
   
   data = urls
   print(data)
   data = jsonify(data)
   return data
if __name__ == "__main__": 
   app.run(debug=True)