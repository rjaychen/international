from flask import Flask, request, jsonify 
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)

#Create the receiver API POST endpoint:
@app.route("/receiver", methods=["POST"])
def postME():
   data = request.get_json()
   
   print(data)
   
   data[0] = data[0] + "Goodbye"
   
   print(data)
   data = jsonify(data)
   return data
if __name__ == "__main__": 
   app.run(debug=True)
