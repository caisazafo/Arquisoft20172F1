import socket
def makeConnection( host, port, destino ):
    # creamos un socket tcp
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Conexion en protocolo TCP (localhost)
    client.connect((host, port))
    
    # Enviamos una peticion get al servidor
    client.send('GET /'+ destino + ' HTTP/1.0\r\nHost: \r\n\r\n')
    
    # Recibimos la respuesta del servidor
    
    print ("Timeout : " + str(client.gettimeout()))
    response = (client.recv(4096))
    #print (response)
    lista = (client.recv(4096)).split("<body>")
    #print client.recv(4096)
    #print lista[1]
    lista2= lista[1].split("</body>")
    print lista2[0]


host = "1"
while (len(host)>0):
    host = raw_input("address: ")
    port = int(raw_input("port: "))
    url = str(raw_input("destino: "))
    if(len(host)>1):
        makeConnection(host,port, url)
        

