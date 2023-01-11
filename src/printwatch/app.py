from flask import Flask, render_template,redirect,url_for,request
import logging
import os
from .utils import calculateChunks
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
FILENAME=""
file_contents=""
PAGESIZE=1024
def chunkread(file,size=1024):
    while True:
        data = file.read(size)
        if not data:
            break
        yield data

@app.route("/")
def home():
    print(os.getcwd())
    return redirect(url_for("logs",logidentifier=FILENAME.split(os.sep)[-1]))

@app.route("/logs/<logidentifier>", defaults={'pagenumber': 1})
@app.route("/logs/<logidentifier>/<pagenumber>")
def logs(logidentifier,pagenumber):
    global FILENAME,PAGESIZE
    FILENAME=logidentifier
    no_of_chunks=calculateChunks(os.path.join(os.getcwd(),"logs",FILENAME),PAGESIZE)

    with open(os.path.join(os.getcwd(),"logs",FILENAME),"r") as f:
        f.seek(PAGESIZE*(int(pagenumber)-1))
        file_contents=f.read(PAGESIZE)
        file_contents=file_contents
        return render_template("home.html",content=file_contents,logidentifier=logidentifier,pages=no_of_chunks,currentpage=int(pagenumber))

@app.route("/search")
def search():
    print(str(request.args['search']))
    return redirect(url_for("logs",logidentifier=request.args['search']+'.txt'))


@app.route("/alllogs")
def alllogs():
    return render_template("logs.html",logidentifier=FILENAME,listcontent=os.listdir(os.path.join(os.getcwd(),"logs")))

def runserver(fname,pagesize):
    global FILENAME
    FILENAME=fname
    global PAGESIZE
    PAGESIZE=pagesize
    app.run(host='0.0.0.0', port=5001,use_reloader=False)
