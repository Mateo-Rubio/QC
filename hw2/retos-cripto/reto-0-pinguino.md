# Reto 0: El pinguino (deteccion de ECB)

## Contexto

AES por si mismo no es el problema. El problema es como se usa. Uno de los
modos de operacion mas simples y mas peligrosos es **ECB** (Electronic Code
Book): el mensaje se parte en bloques de 16 bytes y cada bloque se cifra por
separado, siempre con la misma llave.

La consecuencia es directa: **un mismo bloque de texto plano produce siempre el
mismo bloque de texto cifrado**. El cifrado deja de ocultar la estructura de los
datos. Ese es el defecto que hizo famosa la imagen del pinguino cifrado con ECB:
la silueta seguia siendo visible.

## Como hablarle al servicio

Se conecta con netcat:

```
nc 32.199.164.87 1338
```

El servicio le habla en **hexadecimal**. Esto es importante y suele confundir:

- El hexadecimal NO es cifrado. Es solo una forma de escribir bytes crudos como
  texto: cada byte se escribe con dos caracteres (0-9, a-f). Se usa para poder
  enviar cualquier byte en una sola linea, incluso los que no son imprimibles.
- Ejemplo: la letra `A` vale 65 = 0x41, asi que se escribe `41`. La palabra
  `hola` se escribe `686f6c61`. Enviar 32 letras `A` es `41` repetido 32 veces.

Para producir y leer hexadecimal en Python:

```python
b"AAAA".hex()             # -> '41414141'   (lo que usted ENVIA)
bytes.fromhex("41414141") # -> b'AAAA'       (para LEER la respuesta)
```

Al conectarse, el servicio imprime un saludo y luego espera. Usted envia una
linea con su texto en hexadecimal y el responde `cifrado: <hexadecimal>`.

### Ejemplo de una sesion (por netcat)

```
== Detector de ECB ==
...
Envia tu texto en hexadecimal (o 'salir'):
41414141                 <- usted escribe esto (son 4 letras 'A')
cifrado: e2b9...          <- el servicio responde el cifrado en hex
```

### Automatizarlo con un script

Puede explorar a mano, pero es comodo usar un script:

```python
import socket
s = socket.socket(); s.connect(("32.199.164.87", 1338))
f = s.makefile("rwb")
for _ in range(5):                       # leer las 5 lineas del saludo
    print(f.readline().decode().rstrip())

datos = b"A" * 32                        # los bytes que quiere cifrar
f.write(datos.hex().encode() + b"\n")    # se envian en hex + salto de linea
f.flush()
print(f.readline().decode())             # 'cifrado: ...'
```

## Objetivo

Lograr que dos bloques del texto cifrado sean identicos. Cuando el servicio lo
detecte, entregara el flag (con la forma `uniandes{...}`).

## Pista

Si dos bloques cifrados iguales provienen de dos bloques planos iguales, y un
bloque son 16 bytes, ¿que texto deberia enviar para forzar esa coincidencia?
Usted controla la entrada por completo.

## Entrega

Este flag es una de las respuestas del Taller 2: pegue el `uniandes{...}` que
obtenga en el archivo `qc2_flags.py`.
