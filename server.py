import socket

Headersize = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"{address} Connected")
    
    msg = "Welcome"
    msg = f'{len(msg):<{Headersize}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))

    command = input("what do want to do: ")

    if command == "help":
        print("Commands: stop(kick all who are connected)")


    if command == "stop":
        clientsocket.close()
