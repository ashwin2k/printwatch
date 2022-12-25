from flask import Flask
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
FILENAME=""
file_contents=""

@app.route("/")
def hello_world():
    print(FILENAME)
    with open(FILENAME,"r") as f:
        file_contents=f.read()
        print(file_contents)
        return file_contents

def runserver(fname):
    global FILENAME
    FILENAME=fname
    app.run(host='0.0.0.0', port=5001,use_reloader=False)
