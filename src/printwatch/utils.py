import uuid
import os
import math
def generateFileName():
    return str(uuid.uuid4().hex)+".txt"
def makedir(dname):
    try:
        os.makedirs(os.path.join(os.getcwd(),dname))
    except FileExistsError:
    # directory already exists
        pass
def calculateChunks(filename,psize):
    size=os.path.getsize(filename)
    return math.ceil(size/psize)