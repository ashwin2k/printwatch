import sys
import os
from pipalert.app import runserver
from pipalert.utils import generateFileName,makedir
import threading
import uuid
import os

class Redirector():
    def initialize(self):
        threading.Thread(target=lambda: runserver(self.relpath)).start()
    def __init__(self):
        self.content=""
        self.original=sys.stdout
        fname=generateFileName()
        temp=os.path.join(os.getcwd(),"logs",fname)
        self.relpath=os.path.join("logs",fname)
        self.iofile=temp
    def __init__(self,identifier):
        self.content=""
        self.original=sys.stdout
        self.currentLog=identifier+".txt"
        temp=os.path.join(os.getcwd(),"logs",self.currentLog)
        self.relpath=os.path.join("logs",self.currentLog)
        self.iofile=temp
    def __enter__(self):
        makedir("logs")
        print("Creating new - temp",self.iofile)
        try:
            self.io=open(self.iofile,"w")
        except:
            print("DD")
        sys.stdout=self.io
        # return self.io
    def __exit__(self,a,b,c):
        self.io.close()
        import sys
        sys.stdout=self.original
