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
   #keywords = sourceTranslate(keywords, data[1], data[2]) #Translate the keywords into prefered language
   Allurls = CSESearch(keywords, data[1])   #Search on Custom Search Engine using hte keywords
   urls = TopFiveCommon(Allurls) #Find top 5 urls given keyworcs 
   emptystr = ""
   for i in urls:
       emptystr += i
       emptystr += "\n"
   
   data[0] = emptystr
   print(data)
   data = jsonify(data)
   return data
if __name__ == "__main__": 
   app.run(debug=True)