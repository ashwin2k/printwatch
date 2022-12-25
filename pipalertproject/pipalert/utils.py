import uuid
def generateFileName():
    return str(uuid.uuid4().hex)+".txt"