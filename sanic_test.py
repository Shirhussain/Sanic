from sanic import Sanic 
from sanic.response import json, html,text
import os 

app = Sanic()

#serves file from the static forler
app.static('/static','./static')

@app.route("/")
async def test(request):
    #return json({"hello":"world"})
    template = open(os.getcwd()+"/templates/index.html")
    return html(template.read())




if __name__=="__main__":
    app.run(host ="0.0.0.0",port=8000, debug=True)



