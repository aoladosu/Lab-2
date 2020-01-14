# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:07:23 2020

@author: Ayooluwa
"""

import socket, sys



def main():
    try:
        host = "google.com"
        port = 80
        payload = "GET / HTTP/1.0\r\nHost: "+host+"\r\n\r\n"
        buffer_size = 4096
        
        s = create_tcp_socket()
        remote_ip = get_remote_ip(host)
        s.connect()
        
        send_data(s, payload)
        s.shutdown
        
        
        
        
        
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