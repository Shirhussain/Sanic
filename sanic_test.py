from sanic import Sanic
from sanic.response import json, html,text
import os 
import requests

app = Sanic()

#serves file from the static forler
app.static('/static','./static')

@app.route("/")
async def test(request):
    #return json({"hello":"world"})
    template = open(os.getcwd()+"/templates/index.html")
    return html(template.read())

@app.route('/saveIP', methods=["POST"])
async def saveIP(request):
    ip = request.form.get('ip')
    response = requests.get('https://ipapi.co/'+ip+'/json')
    return json(response.text)



if __name__=="__main__":
    app.run(host ="127.0.0.1",port=8000, debug=True)



