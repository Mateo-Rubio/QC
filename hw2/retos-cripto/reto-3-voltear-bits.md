# Reto 3: voltear bits (CBC bit flipping)

## Contexto

CBC resuelve el problema de ECB: encadena los bloques y usa un IV distinto por
mensaje, de modo que la estructura deja de filtrarse. Pero CBC da
**confidencialidad, no integridad**. El atacante no puede leer el mensaje, pero
si puede modificarlo de forma controlada.

La razon esta en como se descifra CBC:

```
P_i = D(C_i) xor C_(i-1)
```

El bloque de texto plano `P_i` es el XOR de la salida del descifrador con el
**bloque cifrado anterior**, `C_(i-1)`, que viaja en claro y esta en manos del
atacante. Si usted cambia un byte de `C_(i-1)`, cambia el byte correspondiente
de `P_i`, bit por bit. El precio es que `P_(i-1)` se convierte en basura, asi que
ese bloque anterior debe ser uno que no le importe.

## Como hablarle al servicio

Se conecta con netcat:

```
nc 32.199.164.87 1341
```

Apenas se conecta, el servicio le entrega una cookie cifrada y le dice, en
claro, cual es su texto plano. La cookie viene en **hexadecimal** (los bytes
como texto, dos caracteres por byte). El formato de la cookie es
`IV (16 bytes) || texto_cifrado`.

### Ejemplo de la sesion

```
== Servicio de cookies (AES-128 CBC) ==
cookie: 7c1a...            <- IV + cifrado, en hex (esto es lo que usted manipula)
El texto plano de tu cookie es exactamente (dos bloques de 16 bytes):
  bloque 1: comentario_libre
  bloque 2: ;admin=0;role=hi
Envia:  login <cookie_en_hex>
Si al descifrar aparece ';admin=1;', te doy el flag.
```

Su tarea es enviar de vuelta `login <cookie_modificada_en_hex>` de modo que, al
descifrarse, el bloque 2 diga `;admin=1;` en vez de `;admin=0;`.

En Python:

```python
cookie = bytes.fromhex(hex_recibido)   # convertir el 'cookie: ...' a bytes
iv   = cookie[0:16]
c1   = bytearray(cookie[16:32])        # bloque cifrado 1 (lo va a modificar)
resto = cookie[32:]
# ... modifica c1 ...
nueva = (iv + bytes(c1) + resto).hex() # y la envia con 'login ' + nueva
```

## La cuenta (identica a la de la clase)

Usted conoce el bloque 2, `P2 = ;admin=0;role=hi`, y quiere que se convierta en
`P2' = ;admin=1;role=hi`. Solo cambia el byte en la posicion 7 (el `0` por el
`1`).

Partiendo de `P2 = D(C2) xor C1` y `P2' = D(C2) xor C1'`, al hacer XOR de las dos
se cancela `D(C2)`:

```
C1' = C1 xor P2 xor P2'
```

Como P2 y P2' solo difieren en un byte, basta con modificar ese mismo byte de
C1 (la posicion 7 del bloque cifrado 1):

```python
c1[7] ^= ord('0') ^ ord('1')
```

El bloque 1 (el `comentario_libre`) quedara convertido en basura, pero al
servicio no le importa: solo busca `;admin=1;`. Envie `IV + C1' + (resto)` con
`login` y gana. Este ataque no necesita muchas consultas: se calcula de una.

## Moraleja

El cifrado no protege contra modificaciones. Para integridad se usa un HMAC o un
modo autenticado como AES-GCM.

## Entrega

Este flag es una de las respuestas del Taller 2: pegue el `uniandes{...}` que
obtenga en el archivo `qc2_flags.py`.
