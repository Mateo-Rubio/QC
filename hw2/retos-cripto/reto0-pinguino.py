import socket
s = socket.socket(); s.connect(("32.199.164.87", 1338))
f = s.makefile("rwb")
for _ in range(5):                       # leer las 5 lineas del saludo
    print(f.readline().decode().rstrip())
for i in range(32,200):
    datos = b"A" * 32                        # los bytes que quiere cifrar
    f.write(datos.hex().encode() + b"\n")    # se envian en hex + salto de linea
    f.flush()
    print(f.readline().decode())             # 'cifrado: ...'