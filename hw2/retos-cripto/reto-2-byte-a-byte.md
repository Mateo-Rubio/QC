# Reto 2: byte a byte (ECB byte-at-a-time)

## Contexto

Un patron muy comun y muy inseguro es cifrar la concatenacion de algo que
controla el atacante con un secreto:

```
cifrar( entrada_del_atacante || SECRETO )
```

Como ECB es determinista (mismo bloque plano, mismo bloque cifrado), ese secreto
se puede leer **un byte a la vez**, sin atacar AES y sin conocer la llave.

## Como hablarle al servicio

Se conecta con netcat:

```
nc 32.199.164.87 1340
```

El servicio le habla en **hexadecimal**: los bytes se escriben como texto, dos
caracteres por byte (0-9, a-f). No es cifrado, es solo una forma de escribir
bytes crudos. Por ejemplo, `A` (0x41) es `41`, y 15 letras `A` son `41` repetido
15 veces.

Usted envia una linea con su entrada en hexadecimal, y el responde
`cifrado: <hexadecimal>`, que es el cifrado ECB de `su_entrada + SECRETO`. El
SECRETO es el flag. Enviar una **linea vacia** equivale a una entrada vacia (util
para medir el largo del secreto).

En Python:

```python
b"A" * 15                 # 15 bytes de relleno
(b"A" * 15).hex()         # -> '414141...'  (lo que usted envia)
bytes.fromhex(respuesta)  # convierte el 'cifrado: ...' a bytes
```

### Esqueleto de conexion

```python
import socket
s = socket.socket(); s.connect(("32.199.164.87", 1340))
f = s.makefile("rwb")
for _ in range(3):                       # leer el saludo (3 lineas)
    f.readline()

def oraculo(prefijo: bytes) -> bytes:
    f.write(prefijo.hex().encode() + b"\n"); f.flush()
    linea = f.readline().decode()        # 'cifrado: <hex>'
    return bytes.fromhex(linea.split("cifrado: ")[1].strip())
```

## La idea

Suponga que el secreto empieza con una letra desconocida `S`.

1. Envie 15 bytes de relleno. Entonces el primer bloque que se cifra es
   `AAAAAAAAAAAAAAA` + `S`: 15 bytes conocidos y un solo byte desconocido al
   final. Anote ese bloque cifrado (los primeros 16 bytes de la respuesta): es
   su objetivo.
2. Ahora pruebe usted mismo los 256 candidatos: para cada `X` de 0 a 255, cifre
   `AAAAAAAAAAAAAAA` + `X` y compare su primer bloque con el objetivo. El `X` que
   coincide es el primer byte del secreto.
3. Corra el relleno una posicion (14 bytes) y repita para el segundo byte,
   usando el primero que ya conoce. Y asi hasta que salga el secreto completo.

Cada byte cuesta a lo sumo 256 consultas, asi que conviene un script. AES nunca
se ataca.

## Objetivo

Recuperar el SECRETO completo. Ese secreto es el flag (`uniandes{...}`).

## Entrega

Este flag es una de las respuestas del Taller 2: pegue el `uniandes{...}` que
obtenga en el archivo `qc2_flags.py`.
