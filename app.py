from flask import Flask,request

import requests

from main import mainfunc


app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "HOME"

@app.route('/sms',methods=['GET',"POST"])
def sms():
    """You are to send in a POST request packed in an arg named location """

    message_body = request.args.get('location')

    string_ = message_body.strip()
    arr = (string_.split('to'))
    from_val = (arr[0])
    print(from_val)
    to_val = arr[1]
    print(to_val)
    
    #taking mode of transport as default
    
    text_string = str(mainfunc(from_val  , to_val ))
    return jsonify({"details": text_string}), 200




@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Invalid"}), 400



if __name__ == "__main__":
    app.run(debug= True)
