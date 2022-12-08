import requests

def imgSend():
    #files = [('file',open('test1.jpg', 'rb')), ('file',open('test2.jpg', 'rb'))]
    files = open('test1.jpg', 'rb')
    upload = {'file' : files}
    res = requests.post('http://127.0.0.1:8080/fileUpload', files=upload)
