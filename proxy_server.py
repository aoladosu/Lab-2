# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:37:27 2020

and multi processor
"""



buffersize = 4096
def main():
    
    host = "www.google.com"
    port = 80
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        proxy_start.setsocketopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind(host,port)
        proxy_start.listen(1)
        while True:
            conn, addr = proxy_start.accept()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                remote_ip = get_remote_ip(host)
                proxy_end.connect((remote_ip, port))
                p = Process(target=handle_request, args=(conn, addr, proxy_end))
                p.daemon = True
                p.start()
                
            conn.close()
        
        
def handle_request(conn, addr, proxy_end):
    send_full_data = conn.recv(buffersize)
    proxy_end.sendall(send_full_data)
    proxy_end.shutdown(socket.SHUT_WR)
    
    data = proxy_end.recv(fuggersize)
    conn.send(data)
        
def create_tcp_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print("socket creation error")
        sys.exit()    
    return s

def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except: socket.gaierror:
        print("couldn't find host name")
        sys.exit()
    return remote_ip

def send_data(serversocket,payload):
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        sys.exit()