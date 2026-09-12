# Reto 1: cookie de admin por bloques (ECB cut and paste)

## Contexto

En ECB cada bloque de 16 bytes se cifra de forma independiente, siempre con la
misma llave. Esa independencia permite algo peligroso: **recortar bloques
cifrados y pegarlos en otro orden**. El servidor los descifra sin quejarse,
porque cada bloque sigue descifrando correctamente por si solo.

Aqui usara esa idea para fabricarse una cookie de administrador sin conocer la
llave y sin robarle la cookie a nadie.

## Como hablarle al servicio

Se conecta con netcat:

```
nc 32.199.164.87 1339
```

Tiene dos comandos:

- `token <email_en_hex>`  -> le devuelve su cookie cifrada, en hexadecimal.
- `login <cookie_en_hex>` -> descifra la cookie que envie; si su rol es `admin`,
  le entrega el flag.

### Que significa "email en hex" (esto es lo que suele confundir)

**No es el email cifrado.** Es un email que USTED inventa, escrito en
hexadecimal. El servidor toma ese email, lo mete en un perfil con esta forma
fija:

```
email=<su_email>&uid=10&role=user
```

cifra TODO el perfil con AES-128 en ECB, y le devuelve el resultado. Es decir,
usted elige el email; el servidor arma el perfil y se lo cifra.

El hexadecimal es solo una forma de escribir bytes como texto (dos caracteres
por byte, 0-9 y a-f). Se pide en hex, y no como texto plano, para que usted
pueda incluir CUALQUIER byte en el email, incluso los bytes de relleno que va a
necesitar (que no son letras imprimibles). El servidor si elimina los
caracteres `&` y `=` de su email, para que no haga trampa cambiando el perfil
directamente.

Un error comun es enviar el email como texto normal. Por ejemplo, `token hola`
falla con "Entrada invalida", porque `hola` no es hexadecimal valido (la `h`, la
`o` y la `l` no son digitos hex). Primero convierta su email a hexadecimal: el
email `aaaa` en hex es `61616161`, asi que se escribe `token 61616161`.

Convertir en Python:

```python
b"aaaa".hex()             # -> '61616161'   (lo que usted envia tras 'token ')
bytes.fromhex("3f2a...")  # convierte a bytes la cookie que le devuelven
```

### Ejemplo de una sesion

```
== Perfiles cifrados (AES-128 ECB) ==
El perfil tiene la forma:  email=<tu_email>&uid=10&role=user
Comandos:
  token <email_en_hex>   -> te devuelvo tu cookie cifrada (hex)
  login <cookie_en_hex>  -> si tu rol es admin, te doy el flag
token 61616161                 <- usted pide un token para el email "aaaa"
token: 3f2a9c...               <- cifrado de "email=aaaa&uid=10&role=user"
login 3f2a9c...                <- si reenvia el mismo, sigue siendo role=user
Tu rol es: user. No eres admin.
```

## Objetivo

Construir una cookie que, al descifrarse, contenga `role=admin`, y enviarla con
`login`.

## Estrategia (recortar y pegar bloques de 16 bytes)

Los limites de bloque caen cada 16 bytes. El prefijo `email=` ocupa 6 bytes.
Usted controla lo que sigue, asi que puede decidir en que bloque cae cada cosa.

1. **Fabricar el bloque `admin`.** Pida un token para un email que empuje la
   palabra `admin` (mas su relleno PKCS#7) a que empiece sola y alineada en un
   bloque. Ese bloque cifrado es `E(admin + relleno)`. Guardelo.
2. **Aislar el valor `user`.** Pida otro token para un email cuya longitud haga
   que el valor `user` empiece justo en un bloque nuevo (para poder descartarlo).
3. **Pegar.** Arme la cookie final concatenando los bloques cifrados que le
   sirven de cada token, dejando `E(admin + relleno)` donde antes iba `user`.
   Envie eso con `login`.

Para el paso 1 necesita meter bytes de relleno (por ejemplo `0x0b`) dentro del
email; por eso el email se envia en hex, no como texto. Todo el ataque es
recortar y pegar trozos de 16 bytes de los tokens que el propio servidor le da.

Recuerde: para cortar la cookie en bloques,
`cookie = bytes.fromhex(hex_recibido)` y luego `cookie[0:16]`, `cookie[16:32]`,
etc.

## Entrega

Este flag es una de las respuestas del Taller 2: pegue el `uniandes{...}` que
obtenga en el archivo `qc2_flags.py`.
