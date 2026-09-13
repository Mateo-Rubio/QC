import socket
s = socket.socket(); s.connect(("32.199.164.87", 1340))
f = s.makefile("rwb")

for _ in range(3):                       # leer el saludo (3 lineas)
    print(f.readline().decode())

def oraculo(prefijo: bytes) -> bytes:
    f.write(prefijo.hex().encode() + b"\n"); f.flush()
    linea = f.readline().decode()        # 'cifrado: <hex>'
    return bytes.fromhex(linea.split("cifrado: ")[1].strip())

resultado = ""
for i in range(3):
    for j in range(15, -1, -1):
        ref = oraculo(b"A"*j)
        print(ref[i*16:16*(i+1)])
        for byte_value in (bytes([i]) for i in range(256)):
            res = oraculo(b"A"*j + resultado.encode("utf-8") + byte_value)
            if(ref[i*16:16*(i+1)] == res[i*16:16*(i+1)]):
                print(res[i*16:16*(i+1)])
                resultado += byte_value.decode()
                print("i:" + str(i) + ", j:" + str(j) + " || " + resultado)
                print("-"*200)
                break



