"""

"""
import subprocess
from flask import Flask, request
import socket

app = Flask(__name__)

class RequestState:
    seed = 0

# seed=0
@app.route('/', methods=['POST', 'GET'])
def mywebserver():
    global seed
    if request.method == 'GET':
        # Get the local host name
        myHostName = socket.gethostname()
        print("Name of the localhost is {}".format(myHostName))

        # Get the IP address of the local host
        myIP = socket.gethostbyname(myHostName)
        print("IP address of the localhost is {}".format(myIP))
        return str(myIP)

    if request.method == 'POST':
        p = subprocess.Popen(["python", "stress_cpu.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, errors = p.communicate()
        return str(output)
   

if __name__ == '__main__':
    app.run(host='0.0.0.0')
