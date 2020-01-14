# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:22:40 2020

@author: Ayooluwa
"""

import socket, time
from multiprocessing import Process

def main():
    
    HOST = ''
    PORT = 8001
    BUFFER_SIZE = 1024
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(HOST, PORT)
        s.listen(2)
        while True:
            conn, addr = s.accept()
            #p = Process(target=handle_echo, args=(addr,conn))      multiprocess
            print(addr)
            fulldata = conn.recv(BUFFER_SIZE)
            time.sleep(0.5)
            conn.sendall(fulldata)
            conn.close()