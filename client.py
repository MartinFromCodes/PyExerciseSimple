#coding=utf-8
import socket;

s=socket.socket();

host='192.168.1.75';

port=8888;

s.connect((host,port));

print s.recv(2048);