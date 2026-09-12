# QC2 - Taller 2

Nota total: **0 a 5**. Hay 23 items y todos valen lo mismo (5/23 ≈ 0.217 cada
uno).

| Parte | Archivo a editar | Se verifica con | Items |
|---|---|---|---|
| Ejercicios de Qiskit | `qc2.py` | `qc2_test.py` | 8 |
| Seleccion multiple | `qc2_quiz.py` | `qc2_quiz_test.py` | 10 |
| Flags de criptografia | `qc2_flags.py` | el servidor (al entregar) | 5 |

Cubre tres sesiones: operar varios qubits (producto tensor, SWAP, CNOT), la
esfera de Bloch y las compuertas de un qubit, y las fugas en criptografia.

## Requisitos

```bash
pip install qiskit pytest numpy
```

## Parte 1 - Qiskit (`qc2.py`)

Implemente cada funcion siguiendo su docstring. Las funciones `figure_it_out_5`
y `figure_it_out_6` piden una matriz con numpy; las demas usan un circuito y
compuertas.

## Parte 2 - Seleccion multiple (`qc2_quiz.py`)

Las preguntas estan en el docstring al inicio del archivo. Escriba la letra de
su respuesta en el diccionario `RESPUESTAS` al final, por ejemplo `1: "C"`.

## Parte 3 - Flags de criptografia (`qc2_flags.py`)

Estas cinco no se responden con teoria: hay que resolver los retos de la sesion
"Avoiding leaks in cryptography". Cada reto es un servicio de red al que se
conecta y ataca hasta obtener un flag con la forma `uniandes{...}`:

```
Flag 1  reto ECB "el pinguino"      nc 32.199.164.87 1338
Flag 2  reto ECB "cortar y pegar"   nc 32.199.164.87 1339
Flag 3  reto ECB "byte a byte"      nc 32.199.164.87 1340
Flag 4  reto CBC "voltear bits"     nc 32.199.164.87 1341
Flag 5  reto "padding oracle"       nc 32.199.164.87 1342
```

La guia detallada de cada reto (como conectarse, que es el formato hexadecimal,
y la estrategia de ataque) esta en la carpeta **`retos-cripto/`**. Empiece por
`retos-cripto/README.md`.

Pegue cada flag en el diccionario `FLAGS` de `qc2_flags.py`. **El flag correcto
no esta en su copia**: se valida en el servidor cuando entrega. Por eso, al
calificar localmente, las flags aparecen como pendientes y no suman; cuentan al
entregar en la plataforma.

## Verificar y calificar

Ver la nota sobre 5.0 (detalle por ejercicio y por pregunta):

```bash
python qc2_calificar.py
```

Correr los tests de codigo y de quiz:

```bash
pytest
```

**No modifique** `qc2_test.py`, `qc2_quiz_test.py` ni `qc2_calificar.py`.

## Entrega

Entre a **https://uniandes.samuelsabogalpardo.com/**, escriba su correo Uniandes
y el token personal que recibio por correo, y suba `qc2.py`, `qc2_quiz.py` y
`qc2_flags.py`. La plataforma valida las flags contra el servidor y le muestra
de inmediato la nota total. Puede entregar cuantas veces quiera antes del plazo
(maximo una vez por minuto); cuenta la mejor nota.
