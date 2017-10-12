import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')

def udplink(data, addr):
    print('Accept new connection from %s:%s' % addr)
    s.sendto(b'Welcome UDP', addr)
    while True:
        time.sleep(1)
        print(data.decode('utf-8'))
        if not data or data.decode('utf-8') == 'exit':
            break
        s.sendto(('hello %s!' % data.decode('utf-8')).encode('utf-8'), addr)
    s.close()
    print('Connection from %s:%s closed' % addr)

while True:
    data, addr = s.recvfrom(1024)
    t = threading.Thread(target=udplink, args=(data, addr))
    t.start()