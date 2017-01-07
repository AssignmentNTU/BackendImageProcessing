from flask import  Flask,jsonify,request
from OCRLibrary import PyTeseeract
from BaseTranslator import Base64Translator
import os.path
import thread
script_dir = os.path.dirname(os.path.abspath(__file__))
#this is Main Module to run the RESTFUL API
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route("/api/ureca/getExampleAnswer" , methods=['GET'])
def getSampleAnswer():
    return jsonify({"sample answer":"this is backend service to get data from OCR librray"});



@app.route("/api/ureca/postImageToRead", methods=['POST'])
def transalateImageToText():
    #just for testing
    content_data = request.form["image"]
    Base64Translator.Base64Converter().convertFromBase64ToJPG(data=content_data)
    return jsonify({"answer":checkingTranslationImage()})


def transformJPGtoString():
    location_file = os.path.join(script_dir,"accept.jpg")
    return_string  = PyTeseeract.TextTranslation().translateImageToTextUsingTesseract(location_image=location_file)
    print ("return_string",return_string)
    os.remove(location_file)
    return return_string


def checkingTranslationImage():
    location_file = os.path.join(script_dir,"accept.jpg")
    count = 0
    while True:
        count = count +1
        if(os.path.exists(location_file)):
            return transformJPGtoString()



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
