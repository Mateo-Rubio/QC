# Reto 4: padding oracle (AES-CBC + PKCS#7)

## Contexto

Este es el reto final de la serie, y reune todo lo anterior: el modo CBC, el
padding PKCS#7 y la propiedad del XOR. El servicio tiene un solo defecto: al
recibir una cookie, **le dice si el padding PKCS#7 es valido o no**. Ese unico
bit de informacion, repetido, es suficiente para romper el cifrado sin conocer
la llave.

Cualquier servicio que se comporte distinto cuando el padding falla es un
**padding oracle**.

## Como hablarle al servicio

Se conecta con netcat:

```
nc 32.199.164.87 1342
```

Al conectarse le entregan una cookie cifrada y una linea `LISTO` que marca el
fin del saludo. Despues, usted envia cookies cifradas (una por linea, en
**hexadecimal**) y por cada una el servicio responde UNA linea:

- `Padding Invalido` -> el padding PKCS#7 no es valido (este es el "no" del
  oraculo).
- Cualquier otra respuesta -> el padding SI es valido (este es el "si"). Puede
  ser un aviso de cookie valida, o `Su entrada causo un error...` si el
  contenido no es una cookie con sentido. Para el ataque, lo unico que importa
  es distinguir `Padding Invalido` de todo lo demas.

El formato de la cookie es `IV (16 bytes) || texto_cifrado`, todo en hex. La
cookie que le entregan al inicio tiene la forma
`Cookie cifrada (hex): <hex>`.

### Ejemplo de la sesion

```
== Servicio inseguro de cifrado AES-CBC ==
Cookie cifrada (hex): 5f3c...      <- IV + cifrado de una cookie de ejemplo
Envie una cookie cifrada (hex) por linea. Le indicare si el padding es
valido; si resulta ser admin y no esta expirada, le entrego el flag.
LISTO
5f3c...                            <- usted envia una cookie (posiblemente modificada)
Padding Invalido                   <- respuesta del oraculo para esa cookie
```

### Esqueleto del oraculo en Python

```python
import socket
s = socket.socket(); s.connect(("32.199.164.87", 1342))
f = s.makefile("rwb")
enc = None
while True:                              # leer el saludo hasta 'LISTO'
    linea = f.readline()
    if linea.startswith(b"Cookie cifrada (hex): "):
        enc = bytes.fromhex(linea.split(b"hex): ")[1].strip().decode())
    if linea.strip() == b"LISTO":
        break

def padding_valido(cookie: bytes) -> bool:
    f.write(cookie.hex().encode() + b"\n"); f.flush()
    return b"Padding Invalido" not in f.readline()
```

## Recordatorio de CBC

Al descifrar: `P_i = D(C_i) xor C_(i-1)`. `D(C_i)` es la salida del descifrador
de bloque, que usted nunca ve; llamela `intermedio`. Pero `C_(i-1)` esta en sus
manos, asi que el ultimo byte del texto plano que ve el servidor es
`intermedio[15] xor C_(i-1)[15]`.

## La propiedad del XOR (como sacar cada byte)

El servidor valida el padding, es decir, revisa si el texto plano termina en
`0x01`, o en `0x02 0x02`, etc. Fije un bloque anterior falso y vaya probando su
ultimo byte de 0 a 255. Cuando el servidor deje de decir `Padding Invalido`,
sabe que:

```
intermedio[15] xor su_byte = 0x01     =>   intermedio[15] = su_byte xor 0x01
```

Con `Y xor X xor X = Y`, una vez que conoce `intermedio`, el texto plano real es
`intermedio xor C_(i-1)_real`. Luego fuerza el ultimo byte a `0x02`, busca el
penultimo para que el padding sea `0x02 0x02`, y asi hasta recuperar los 16
bytes del bloque. Repita por cada bloque.

## Las dos partes de la tarea

### Parte A: descifrar

Use el oraculo para recuperar el texto plano de la cookie que le entregaron.
Deberia ver un JSON con `username`, `is_admin` y `expires`.

### Parte B: forjar (CBC-R)

El mismo oraculo permite recuperar el `intermedio` de **cualquier** bloque
cifrado, incluso uno inventado por usted. Con eso puede construir, de atras hacia
adelante, una secuencia de bloques cifrados que al descifrarse produzca el texto
plano que usted elija. Fije como texto deseado una cookie con `is_admin=true` y
una fecha `expires` futura, forje su cifrado y envielo para obtener el flag.

## Objetivo y entrega

El flag (`uniandes{...}`) sale cuando el servidor acepta una cookie forjada de
admin no expirada (parte B). Peguelo en el archivo `qc2_flags.py` del Taller 2.
Se recomienda entregar tambien, en su reporte, el texto plano de la cookie
original (parte A).
