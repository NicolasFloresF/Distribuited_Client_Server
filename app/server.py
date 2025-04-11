from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 5050))
s.listen(1)
print("Server is listening on port 5050...")

try:
    while True:
        conn, addr = s.accept()
        print("Connected by", addr)

        data = conn.recv(1024)
        if not data:
            break

        print("Received:", data.decode())
        conn.send(data + b"*")
        conn.close()
except KeyboardInterrupt:
    print("Server is shutting down...")
finally:
    s.close()
