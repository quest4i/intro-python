import xmlrpc.client


proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
result = proxy.get_time()
print("ISO time : ", result)
