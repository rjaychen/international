from flask import Flask, request, jsonify 
from flask_cors import CORS
from CSESearch import CSESearch
from MaxURL import TopFiveCommon

app = Flask(__name__)

cors = CORS(app)

#Create the receiver API POST endpoint:
@app.route("/receiver", methods=["POST"])
def postME():
   data = request.get_json()
   
   print(data)
   
   keywords = ["Cálculo", "Ecuación diferencial"]
   Allurls = CSESearch(keywords, data[1])
   urls = TopFiveCommon(Allurls)
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
