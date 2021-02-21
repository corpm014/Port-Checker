import threading
import socket
import sys

# local host
ip = socket.gethostbyname(socket.gethostname())

# Checks ports to see if it open
def portscan(port, ip, timeout):
    # Setting up temporary connection
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(timeout)

    # Attempting to connect to the server
    try:
        con = server.connect((ip ,port))
        print('Port :',port,"is open")
        con.close()
    except:
        pass

# Run line command
if __name__ == '__main__':
    ip = str(input("host ip or website (or local): "))
    if ip == None:
        ip = socket.gethostbyname(socket.gethostname())
    for x in range(0, 10000): 
        t = threading.Thread(target=portscan,kwargs={'port':x, 'ip': ip, 'timeout': 10})
        t.start()
    

    print("\n", sys.exit("PORTS HAVE BEEN SEARCHED"))
