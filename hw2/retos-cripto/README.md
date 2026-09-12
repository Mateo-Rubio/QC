# Retos de criptografia - Taller 2 (fugas en criptografia)

Estos cinco retos son la parte de "flags" del Taller 2. Cada uno es un servicio
de red al que se conecta, lo ataca aprovechando una debilidad en el **modo de
operacion** o en la **implementacion** (nunca en AES), y obtiene un flag con la
forma `uniandes{...}`. Ese flag es la respuesta que pega en `qc2_flags.py`.

Van en orden de dificultad; conviene hacerlos en orden, porque cada uno prepara
el siguiente.

| Reto | Tema | Puerto | Instrucciones |
|---|---|---|---|
| 0 | ECB deja ver la estructura | 1338 | [reto-0-pinguino.md](reto-0-pinguino.md) |
| 1 | ECB: cortar y pegar bloques | 1339 | [reto-1-cookie-bloques.md](reto-1-cookie-bloques.md) |
| 2 | ECB: leer un secreto byte a byte | 1340 | [reto-2-byte-a-byte.md](reto-2-byte-a-byte.md) |
| 3 | CBC: voltear bits (integridad) | 1341 | [reto-3-voltear-bits.md](reto-3-voltear-bits.md) |
| 4 | Padding oracle (descifrar y forjar) | 1342 | [reto-4-padding-oracle.md](reto-4-padding-oracle.md) |

Todos estan en el servidor `32.199.164.87`. Se conecta, por ejemplo, con:

```
nc 32.199.164.87 1338
```

## Antes de empezar: el formato hexadecimal

Los servicios le hablan en **hexadecimal**, y esto suele confundir al principio:

- El hexadecimal NO es cifrado. Es solo una forma de escribir bytes crudos como
  texto: cada byte se escribe con dos caracteres (0-9, a-f).
- Ejemplo: la letra `A` vale 0x41, asi que se escribe `41`. La palabra `admin` se
  escribe `61646d696e`.
- Se usa para poder enviar cualquier byte en una sola linea, incluso los que no
  son letras imprimibles (como el relleno PKCS#7).

En Python:

```python
b"admin".hex()             # -> '61646d696e'   (lo que usted ENVIA)
bytes.fromhex("61646d696e")# -> b'admin'         (para LEER una respuesta)
```

## Como trabajar

Puede explorar a mano con `nc`, pero los ataques necesitan muchas consultas
(hasta cientos), asi que se resuelven con un **script**. Cada instruccion trae
un esqueleto de conexion en Python listo para adaptar. Puede usar sockets
directamente (como en los ejemplos) o la libreria `pwntools` si la conoce.

## Requisitos

```bash
pip install pwntools     # opcional; los ejemplos usan solo 'socket' de la libreria estandar
```

## Entrega

Cada flag capturado va en el diccionario `FLAGS` de `qc2_flags.py`, y se valida
al entregar el Taller 2 en la plataforma.
