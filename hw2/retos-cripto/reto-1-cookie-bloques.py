import socket

# E(admin + relleno): 0442f2b537c6de74ab1728dcd479658d
# cookie: ba5916f2674f144f9fc4010b2aa36aa74396b7f104aa100ffef2d32ef7043277
def enviar(comando_txt: str):
    f.write(comando_txt.encode() + b"\n")
    f.flush()  
    
s = socket.socket(); s.connect(("32.199.164.87", 1339))
f = s.makefile("rwb")

for _ in range(5):                      
    print(f.readline().decode(errors="replace").rstrip())

#email = "A"*10 + "admin" + "\x0b"*11
email = "A"*13
email_hex = email.encode().hex()
enviar(f"token {email_hex}")

respuesta_token = f.readline().decode(errors="replace")
cookie_hex = respuesta_token.strip().split()[-1]
print(cookie_hex[0:64])
#enviar(f"login {cookie_hex}")
enviar(f"login ba5916f2674f144f9fc4010b2aa36aa74396b7f104aa100ffef2d32ef70432770442f2b537c6de74ab1728dcd479658d")
print(f.readline().decode(errors="replace").rstrip())
print(f.readline().decode(errors="replace").rstrip())

