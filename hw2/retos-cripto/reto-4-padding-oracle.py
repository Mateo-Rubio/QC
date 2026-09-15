import socket
s = socket.socket(); s.connect(("32.199.164.87", 1342))
f = s.makefile("rwb")
enc = None
while True:                            
    linea = f.readline()
    print(linea.decode())
    if linea.startswith(b"Cookie cifrada (hex): "):
        enc = bytes.fromhex(linea.split(b"hex): ")[1].strip().decode())
    if linea.strip() == b"LISTO":
        break

def padding_valido(cookie: bytes) -> bool:
    f.write(cookie.hex().encode() + b"\n"); f.flush()
    return b"Padding Invalido" not in f.readline()

cookie = bytearray(enc)
X = bytearray(16)
Y = bytearray(16)
for i in range(2):
    C1 = cookie[i*16: (i+1)*16]
    cookie_mod = cookie
    for j in range(15,-1,-1):
        print("j:",j)
        for k in range(15,j,-1):
            print("k:", k)
            C1[k] = Y[k] ^ (16-j) 
            k+=1 
        for byte_value in range(256):
#           if byte_value == 0 and j == 15: 
#                continue 
            C1[j] = byte_value
            cookie_mod[i*16: (i+1)*16] = C1
            if padding_valido(bytes(cookie_mod)):
                print(byte_value)
                X[j] = byte_value
                Y[j] = byte_value ^ 16-j 
                break
print(X)





