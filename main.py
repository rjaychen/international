from http.client import ImproperConnectionState
from flask import Flask, request, jsonify 
from flask_cors import CORS
from CSESearch import CSESearch
from MaxURL import TopFiveCommon
from frequency_filter import frequency_filter_stopwords
import speech_recognition as sr
import wave #probably not needed
import requests, io
from google_translate import sourceTranslate
app = Flask(__name__)

cors = CORS(app)

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

# Get WAV File Routing
@app.route('/soundfiles',methods = ['GET','POST'])
#get file
def wavtoText():
    data = request.get_json()
    print(data)
    if(is_downloadable(data[0])):
         r = requests.get(data[0], allow_redirects=True)
         with open('soundfile.wav', 'wb') as f:
            f.write(r.content)
         keywords = frequency_filter_stopwords(process_file('soundfile.wav'))
         
         #translation
         translatedWords = keywords
         for i, keywords in enumerate(keywords):
            translatedWords[i] = sourceTranslate(keywords, data[1], data[2])

         keywords = translatedWords

         print(keywords)
         Allurls = CSESearch(keywords, data[2])
         urls = TopFiveCommon(Allurls)
         data = urls
         print(data)
         data = jsonify(data)
         return data


def process_file(filename):
    #code for returning text from speech
    r = sr.Recognizer()
    lecture = sr.AudioFile(filename)
    with lecture as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    return r.recognize_google(audio)


#Create the receiver API POST endpoint:
@app.route("/receiver", methods=["POST"])
def postME():
   data = request.get_json()
   print()
   keywords = frequency_filter_stopwords(data[0])

   #translation
   translatedWords = keywords
   for i, keywords in enumerate(keywords):
      translatedWords[i] = sourceTranslate(keywords, data[1], data[2])

   keywords = translatedWords
   
   Allurls = CSESearch(keywords, data[2])
   urls = TopFiveCommon(Allurls)
   
   data = urls
   print(data)
   data = jsonify(data)
   return data
if __name__ == "__main__": 
   app.run(debug=True)
