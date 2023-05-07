from flask import *
import requests

app = Flask(__name__)

API_KEY = 'y7UGf3ysrES6e3dd'
ratlist = []
md5ratlist = []
notratlist = []
md5notratlist = []
param_cache = {}

@app.route("/")
def index():
    return render_template('index.html', notrathash=notratlist, md5notrat=md5notratlist, ratlist=ratlist, md5rat=md5ratlist)

@app.route('/filehandler', methods=['POST'])
def filehandler():
    if request.method == 'POST':
        clientfiles = {'fileupload': ('APIFILE.jar', request.files['fileupload'].read())}
        # print(clientfiles.filename)
        # print(clientfiles)
        # clientfiles = {'fileupload': clientfiles}
        # print(clientfiles)
        api_data = requests.post(f"https://isthisarat.com/api/frontend_tester?API_KEY={API_KEY}", files=clientfiles)
        print(api_data.status_code)
        if api_data.status_code == 200:
            api_data = api_data.json()
            for param in api_data:
                param_cache.update({param: api_data[param]})
            # isthisarat = api_data["isthisarat"]
            # confidence = api_data["confidence"]
            # hashvalue = api_data["hashvalue"]
            md5hash = api_data["md5hash"]
            # aiconfyes = api_data["aiconfyes"]
            # aiconfno = api_data["aiconfno"]
            # sigstring = api_data["sigstring"]
            # viofiles = api_data["viofiles"]
            # violator = api_data["violator"]
            # violation = api_data["violation"]
            # viodesc = api_data["viodesc"]
            # vcount = api_data["vcount"]
            # str_data = api_data["str_data"]
            print("Rendering template")
            return md5hash
            # return render_template('score.html', isthisarat=isthisarat, confidence=confidence, hashvalue=hashvalue,
            #                        md5hash=md5hash, aiconfyes=aiconfyes, aiconfno=aiconfno, sigstring=sigstring,
            #                        viofiles=viofiles,
            #                        violator=violator, violation=violation, viodesc=viodesc, vcount=vcount,
            #                        str_data=str_data)

@app.route('/score/<rawhash>', methods = ['GET'])
def scorepage(rawhash):
    mongoobj = param_cache
    print(param_cache)
    if mongoobj is not None:
        isthisarat = mongoobj['isthisarat']
        confidence = mongoobj['confidence']
        hashvalue = mongoobj['hashvalue']
        md5hash = mongoobj['md5hash']
        aiconfyes = mongoobj['aiconfyes']
        aiconfno = mongoobj['aiconfno']
        sigstring = mongoobj['sigstring']
        viofiles = mongoobj['viofiles']
        violator = mongoobj['violator']
        violation = mongoobj['violation']
        viodesc = mongoobj['viodesc']
        vcount = mongoobj['vcount']
        str_data = mongoobj['str_data']
        return render_template('score.html', isthisarat=isthisarat, confidence=confidence, hashvalue=hashvalue,
                               md5hash=md5hash, aiconfyes=aiconfyes, aiconfno=aiconfno, sigstring=sigstring, viofiles=viofiles,
                               violator=violator, violation=violation, viodesc=viodesc, vcount=vcount, str_data=str_data)
    else:
        return 'This file has not been scanned yet or needs to be rescanned'



if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)