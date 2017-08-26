import socket
def makeConnection( host, port, destino ):
    # creamos un socket tcp
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Conexion en protocolo TCP (localhost)
    client.connect((host, port))
    
    # Enviamos una peticion get al servidor
    client.send('GET /'+ destino + ' HTTP/1.0\r\nHost: \r\n\r\n')
    
    # Recibimos la respuesta del servidor
    response = client.recv(4096)
    print "Timeout : " + str(client.gettimeout())
    
    print response



host = "1"
while (len(host)>0):
    host = raw_input("address: ")
    port = int(raw_input("port: "))
    url = raw_input("destino: ")
    if(len(host)>1):
        makeConnection(host,port, url)

