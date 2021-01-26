import socket

Headersize = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))



while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(9999)
        if new_msg:
            print(f"New msg length: {msg[:Headersize]}")
            msglen = int(msg[:Headersize])
            new_msg = False

        full_msg += msg.decode("utf-8")
        if len(full_msg)-Headersize == msglen:
            print("recvd")
            print(full_msg[Headersize:])
            new_msg = True
            full_msg = ''
    print(full_msg)
