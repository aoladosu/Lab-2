# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:32:53 2020

and multi processor
"""

import socket
from multiprocess import Pool

host = "localhost"
port = 8001
buffersize = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
        
        full_data = s.recv(buffersize)
        print(full_data)
        
    except Exception as e:
        print(e)
        
def main():
    address = [('127.0.0.1',8001)]
    with Pool() as p:
        p.map(connect, address*10)