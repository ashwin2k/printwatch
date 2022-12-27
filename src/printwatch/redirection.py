import sys
import os
from printwatch.app import runserver
from printwatch.utils import generateFileName,makedir
import threading
import os

class Redirector():
    def initialize(self):
        self.server=threading.Thread(target=lambda: runserver(self.relpath))
        self.server.start()
    def shutdown(self):
        self.server.terminate()
        self.server.join()

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
