import socket
s = socket.socket(); s.connect(("32.199.164.87", 1342))
f = s.makefile("rwb")
enc = None
while True:                              # leer el saludo hasta 'LISTO'
    linea = f.readline()
    print(linea.decode())
    if linea.startswith(b"Cookie cifrada (hex): "):
        enc = bytes.fromhex(linea.split(b"hex): ")[1].strip().decode())
    if linea.strip() == b"LISTO":
        break

def padding_valido(cookie: bytes) -> bool:
    f.write(cookie.hex().encode() + b"\n"); f.flush()
    return b"Padding Invalido" not in f.readline()