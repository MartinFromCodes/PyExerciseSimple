#coding=utf-8
import socket;

s=socket.socket();
host=socket.gethostname();
port=8888
print host,port

s.bind((host,port));

s.listen(5);

while True:
    c,addr=s.accept();
    print 'connection addr',addr;
    c.send('Weclom python');
    c.close();
      
