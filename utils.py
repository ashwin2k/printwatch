import uuid
import os
def generateFileName():
    return str(uuid.uuid4().hex)+".txt"
def makedir(dname):
    try:
        os.makedirs(os.path.join(os.getcwd(),dname))
    except FileExistsError:
    # directory already exists
        pass
