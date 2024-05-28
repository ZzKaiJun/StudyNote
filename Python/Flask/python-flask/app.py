from flask import Flask  #載入Flask

app = Flask(__name__)   #建立Application物件


#建立網站首頁的回應方式

@app.route("/")  #網站首頁

def index():                #用來回應網站首頁連現的函式
    return "Hello flask!"    #回傳網頁首頁的內容

#啟動網站伺服器
app.run()

