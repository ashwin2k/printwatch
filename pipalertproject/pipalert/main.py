import sys
import io
import os
import subprocess
from pipalertproject.pipalert.app import runserver
from pipalertproject.pipalert.utils import generateFileName
import threading
import uuid
import os

class Redirector():
    def initialize(self):
        threading.Thread(target=lambda: runserver(self.iofile)).start()
    def __init__(self):
        self.content=""
        self.original=sys.stdout
        temp=os.path.join(os.getcwd(),"pipalertproject","pipalert","logs",generateFileName())
        self.iofile=temp
    def __enter__(self):
        print("Creating new - temp",self.iofile)
        try:
            self.io=open(self.iofile,"a")
        except:
            print("DD")
        return self.io
    def __exit__(self,a,b,c):
        self.io.close()
        import sys
        sys.stdout=self.original
