import sys
import io
import os
import subprocess
from pipalertproject.pipalert.app import runserver
import threading
import uuid

def runprocess():
    print(subprocess.run([os.getcwd(),"pipalertproject","pipalert","manage.py"]))
class Redirector():
    def __init__(self):
        self.content=""
        self.iofile="./pipalertproject/pipalert/demo.txt"
        self.io=open("./pipalertproject/pipalert/demo.txt","w")
        self.original=sys.stdout
        threading.Thread(target=lambda: runserver()).start()    
        print("Created")
    def __enter__(self):
        return self.io
    def __exit__(self,a,b,c):
        import sys
        sys.stdout=self.original
    def reset(self):
        sys.io=self.original