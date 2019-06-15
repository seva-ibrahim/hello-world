from flask import Flask,render_template,jsonify,request
import urllib.request
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode() == 200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData


@app.route('/test', methods=["GET", "POST"])
def test():
    urlData = "https://jsonplaceholder.typicode.com/posts"
    jsonData = getResponse(urlData)
    
    for i in jsonData:
        print(
            f'Body:  {i["body"]}, Title : {i["title"]}')

    return render_template('test.html')


if __name__ == "__main__":
    app.run(debug=True)
 
