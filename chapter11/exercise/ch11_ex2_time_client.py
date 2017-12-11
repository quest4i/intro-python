import zmq


host = '127.0.0.1'
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s" % (host, port))

for message in ['time', 'second']:
    print('this message : ', message)
    client.send(message.encode('utf-8'))
    reply_bytes = client.recv()
    print("received : %s" % (reply_bytes.decode('utf-8')))




