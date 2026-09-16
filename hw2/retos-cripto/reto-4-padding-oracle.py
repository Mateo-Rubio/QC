import socket
import math
import os
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
    linea = f.readline()
    return b"Padding Invalido" not in linea

def descifrar_cookie(cook: bytes) -> None:
    max_blocks = 6
    cookie = bytearray(cook)
    Xf_array = bytearray(16*max_blocks)
    Yf_array = bytearray(16*max_blocks)
    Pf_array = bytearray(16*max_blocks)
    for i in range(max_blocks-1):
        val = True
        C1 = cookie[i*16: (i+1)*16];C1_real = cookie[i*16: (i+1)*16]
        C2 = cookie[(i+1)*16: (i+2)*16]
        X = Xf_array[i*16: (i+1)*16]
        Y = Yf_array[(i+1)*16: (i+2)*16]
        P = Pf_array[(i+1)*16: (i+2)*16]
        for j in range(15,-1,-1):
            for k in range(15,j,-1):
                C1[k] = Y[k] ^ (16-j) 
            for byte_value in range(256):
                C1[j] = byte_value
                val = padding_valido(bytes(C1 + C2))
                if val:
                    X[j] = byte_value
                    Y[j] = byte_value ^ (16-j) 
                    P[j] = Y[j] ^ C1_real[j]
                    print(bytes(P).decode())
                    break
            if not val:
                print("no funcionó")
                break
        Xf_array[i*16: (i+1)*16] = X
        Yf_array[(i+1)*16: (i+2)*16] = Y
        Pf_array[(i+1)*16: (i+2)*16] = P
        if not val: 
            break 
    return Xf_array, Yf_array, Pf_array

'''
IV            = cookie[0:16]
Bloque A [16:32]: {"username":"inv
Bloque B [32:48]: itado","is_admin
Bloque C [48:64]: ":"false","expir
Bloque D [64:80]: es":"2020-01-01"
Bloque E [80:96]: } + padding
'''
if os.path.exists('archivo.bin'):
    with open('archivo.bin', 'rb') as f:
        data = f.read()
    tam = len(data) // 3
    Y_array = bytearray(data[0:tam])
    X_array = bytearray(data[tam:2*tam])
    P_array = bytearray(data[2*tam:3*tam])
else:
    X_array, Y_array, P_array = descifrar_cookie(enc)
    with open('archivo.bin', 'wb') as f:
        f.write(Y_array)
        f.write(X_array)
        f.write(P_array)
print("Plain text descifrado/cargado:", bytes(P_array).decode())
C = []
mensajes = [ b'es":"2099-12-31"', b'":"true" ,"expir', b'itado","is_admin', ]
for i in range(2,-1,-1):
    val = True
    CX1 = bytearray(a ^ b for a, b in zip(Y_array[16*(i+2):16*(i+3)], mensajes[2-i]))
    C.append(CX1)
    CX0 = enc[i*16: (i+1)*16];CX0_real = enc[i*16: (i+1)*16]
    X = X_array[i*16: (i+1)*16]
    P = P_array[(i+1)*16: (i+2)*16]
    Y = Y_array[(i+1)*16: (i+2)*16]
    for j in range(15,-1,-1):
            for k in range(15,j,-1):
                CX0[k] = Y[k] ^ (16-j) 
            for byte_value in range(256):
                CX0[j] = byte_value
                val = padding_valido(bytes(CX0 + CX1))
                if val: 
                    Y[j] = byte_value ^ (16-j) 
                    P[j] = Y[j] ^ CX0_real[j]
                    break
            if not val:
                print("no funcionó")
                break
    X_array[i*16: (i+1)*16] = X
    Y_array[(i+1)*16: (i+2)*16] = Y
    P_array[(i+1)*16: (i+2)*16] = P

## Calculo IV
C.append(bytearray(a ^ b for a, b in zip(Y_array[16:32], b'{"username":"inv')))
forged_cookie = C[3] + C[2] + C[1] + C[0] + enc[64:]
_ = decifrar_cookie(forged_cookie)
f.write(forged_cookie.hex().encode() + b"\n"); f.flush()
print(f.readline())








