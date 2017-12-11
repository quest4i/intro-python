from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime


def get_time():
    return datetime.isoformat(datetime.now())


server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(get_time, "get_time")
server.serve_forever()