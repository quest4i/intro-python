import zmq
from datetime import datetime

host = '127.0.0.1'
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://%s:%s" % (host, port))

while True:
    request_bytes = server.recv()
    request_str = request_bytes.decode('utf-8')
    print("That voice in my head says: %s" % request_str)
    reply_str = "I know time!"
    if request_str == 'time':
        reply_str = datetime.isoformat(datetime.now())
    print("Client says: %s" % request_str)
    server.send(reply_str.encode('utf-8'))


