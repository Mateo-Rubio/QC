# QC1 – Taller 1

Nota total: **0 a 5**. Hay 24 ítems y todos valen lo mismo (5/24 ≈ 0.21 cada
uno), igual que en el autograder de GitHub Classroom.

| Parte | Archivo a editar | Se verifica con | Ítems |
|---|---|---|---|
| Ejercicios de Qiskit | `qc1.py` | `qc1_test.py` | 8 (`example_not` ya viene resuelto) |
| Selección múltiple   | `qc1_quiz.py` | `qc1_quiz_test.py` | 16 |

## Requisitos

```bash
pip install qiskit pytest
```

## Parte 1 – Qiskit (`qc1.py`)

Implemente cada función siguiendo su docstring. `example_not` es un ejemplo ya
resuelto que muestra cómo hacerlo.

## Parte 2 – Selección múltiple (`qc1_quiz.py`)

Las preguntas están en el docstring al inicio del archivo. Los circuitos se
dibujan como en Qiskit (`qc.draw('text')`), de izquierda a derecha:

```
    ┌───┐┌───┐
q0: ┤ X ├┤ Z ├
    └───┘└───┘
```

Escriba la letra de su respuesta en el diccionario `RESPUESTAS` al final del
archivo, por ejemplo `1: "C"`.

## Verificar y calificar

Ver la nota sobre 5.0 (detalle por ejercicio y por pregunta):

```bash
python qc1_calificar.py
```

Correr todos los tests (es lo mismo que ejecuta el autograder de GitHub
Classroom):

```bash
pytest
```

También puede correr cada parte por separado: `python qc1_test.py` o
`python qc1_quiz_test.py`.

**No modifique** `qc1_test.py`, `qc1_quiz_test.py` ni `qc1_calificar.py`.
