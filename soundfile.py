from flask import Flask,send_file,send_from_directory,request, redirect, url_for, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import speech_recognition as sr
import wave
import requests, io

#Speech to text "Service"
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
    if(is_downloadable(data)):
        r = requests.get(data, allow_redirects=True)
        with open('soundfile.wav', 'wb') as f:
            f.write(r.content)
    return process_file('soundfile.wav')


def process_file(filename):
    #code for returning text from speech
    r = sr.Recognizer()
    lecture = sr.AudioFile(filename)
    with lecture as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    return jsonify(r.recognize_google(audio))

if __name__ == '__main__':
    app.run(port = 8000, debug = True)
