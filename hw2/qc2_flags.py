"""
Taller 2 - Preguntas de flag (retos de criptografia)
=====================================================

Esta parte no se responde con teoria, sino resolviendo los retos de la sesion
"Avoiding leaks in cryptography". Cada reto es un servicio de red al que se
conecta, lo ataca, y obtiene un flag con la forma  uniandes{...}.

Pegue cada flag capturado, como texto entre comillas, en el diccionario FLAGS.

Los retos estan en el servidor  32.199.164.87  en estos puertos:

    Flag 1  -> reto ECB "el pinguino"        nc 32.199.164.87 1338
    Flag 2  -> reto ECB "cortar y pegar"     nc 32.199.164.87 1339
    Flag 3  -> reto ECB "byte a byte"        nc 32.199.164.87 1340
    Flag 4  -> reto CBC "voltear bits"       nc 32.199.164.87 1341
    Flag 5  -> reto "padding oracle"         nc 32.199.164.87 1342

Los flags NO se verifican en su maquina: se validan en el servidor cuando
entrega en la plataforma. Al correr 'python qc2_calificar.py' localmente
apareceran como pendientes; eso es normal.

No modifique nada mas de este archivo.
"""

# Pegue aqui los flags capturados (texto entre comillas). Deje "" los que no tenga.
FLAGS = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
}
