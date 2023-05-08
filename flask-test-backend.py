from flask import *
import requests

app = Flask(__name__)

API_KEY = ""
param_cache = {}


@app.route("/")
def index():
    return render_template(
        "index.j2",
    )


@app.route("/filehandler", methods=["POST"])
def filehandler():
    if request.method != "POST":
        return "Method not allowed", 405
    clientfiles = {"fileupload": ("APIFILE.jar", request.files["fileupload"].read())}
    api_data = requests.post(
        f"https://isthisarat.com/api/frontend_tester?API_KEY={API_KEY}",
        files=clientfiles,
    )
    print(api_data.status_code)
    if api_data.status_code != 200:
        return "Error", api_data.status_code
    api_data = api_data.json()
    for param in api_data:
        param_cache.update({param: api_data[param]})
    md5hash = api_data["md5hash"]
    return md5hash


@app.route("/score/<rawhash>", methods=["GET"])
def scorepage(rawhash):
    mongoobj = param_cache
    print(param_cache)
    if "md5hash" in mongoobj:
        isthisarat = mongoobj["isthisarat"]
        confidence = mongoobj["confidence"]
        hashvalue = mongoobj["hashvalue"]
        md5hash = mongoobj["md5hash"]
        aiconfyes = mongoobj["aiconfyes"]
        aiconfno = mongoobj["aiconfno"]
        sigstring = mongoobj["sigstring"]
        viofiles = mongoobj["viofiles"]
        violator = mongoobj["violator"]
        violation = mongoobj["violation"]
        viodesc = mongoobj["viodesc"]
        vcount = mongoobj["vcount"]
        str_data = mongoobj["str_data"]
        print(
            isthisarat,
            confidence,
            hashvalue,
            md5hash,
            aiconfyes,
            aiconfno,
            sigstring,
            viofiles,
            violator,
            violation,
            viodesc,
            vcount,
            str_data,
        )
        return render_template(
            "score.j2",
            isthisarat=isthisarat,
            confidence=confidence,
            hashvalue=hashvalue,
            md5hash=md5hash,
            aiconfyes=aiconfyes,
            aiconfno=aiconfno,
            sigstring=sigstring,
            viofiles=viofiles,
            violator=violator,
            violation=violation,
            viodesc=viodesc,
            vcount=vcount,
            str_data=str_data,
        )
    else:
        return "This file has not been scanned yet or needs to be rescanned", 404


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
