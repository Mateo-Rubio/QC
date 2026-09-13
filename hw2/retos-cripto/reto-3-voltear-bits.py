import socket

def enviar(comando_txt: str):
    f.write(comando_txt.encode() + b"\n")
    f.flush()  
    
s = socket.socket(); s.connect(("32.199.164.87", 1341))
f = s.makefile("rwb")

for i in range(7):
    server_response = f.readline().decode(errors="replace").rstrip()
    if i == 1:
        cookie = bytes.fromhex(server_response.strip().split()[-1])
    print(server_response)

iv   = cookie[0:16]
c1   = bytearray(cookie[16:32])
resto = cookie[32:]
c1[7] ^= ord('0') ^ ord('1') 
nueva = (iv + bytes(c1) + resto).hex()

enviar(f"login {nueva}")
print(f.readline().decode(errors="replace").rstrip())
print(f.readline().decode(errors="replace").rstrip())

