"""
Taller 2 - Preguntas de seleccion multiple
===========================================

Responda cada pregunta escribiendo la LETRA de la opcion (por ejemplo "A",
"B", "C"...) dentro del diccionario RESPUESTAS, al final de este archivo.
No modifique nada mas.

Las preguntas cubren las tres sesiones del taller: operar varios qubits
(producto tensor, SWAP, CNOT), la esfera de Bloch y las compuertas de un
qubit, y las fugas en criptografia (ECB, CBC, padding oracle).

Para calificar (preguntas + ejercicios de Qiskit) ejecute:

    python qc2_calificar.py

------------------------------------------------------------------------

Pregunta 1.  Convenio de orden de qubits. El estado "qubit 0 en 1 y el
             resto en 0" se escribe distinto segun la convencion.
             ¿Cual es correcto?

    A) |100> tanto en Qiskit como en Nielsen y Chuang.
    B) |001> en Qiskit (little-endian) y |100> en Nielsen y Chuang.
    C) |010> en Qiskit.
    D) Es igual en ambos; la convencion no afecta el ket.

------------------------------------------------------------------------

Pregunta 2.  Producto tensor. Con

                 psi1 = [ 1/2 , sqrt(3)/2 ]^T      (qubit de la izquierda)
                 psi2 = [ 0   , 1         ]^T      (qubit de la derecha)

             ¿cual es psi1 (x) psi2 en el orden de base
             [ |00> , |01> , |10> , |11> ]?

    A) [ 0 , 1/2 , 0 , sqrt(3)/2 ]
    B) [ 1/2 , 0 , sqrt(3)/2 , 0 ]
    C) [ 1/2 , sqrt(3)/2 , 0 , 0 ]
    D) [ 0 , 0 , 1/2 , sqrt(3)/2 ]

------------------------------------------------------------------------

Pregunta 3.  De las tres descripciones del SWAP vistas en clase, ¿cual es
             la DEFINICION que funciona siempre (en cualquier base, esten
             o no entrelazados los qubits)?

    A) "Intercambia el estado de los dos qubits": |a> (x) |b> -> |b> (x) |a>.
    B) "Intercambia las amplitudes de |01> y |10>".
    C) "Manda cada etiqueta de base |ab> a |ba>".
    D) "Se intercambian y se recalcula el tensor", y eso siempre funciona.

------------------------------------------------------------------------

Pregunta 4.  Se aplica un CNOT con el control en el estado
             |+> = (|0> + |1>)/sqrt(2) y el target en |0>.
             ¿Cual es el resultado?

    A) El estado producto |+> (x) |0>.
    B) El estado de Bell entrelazado (|00> + |11>)/sqrt(2).
    C) |11>.
    D) (|01> + |10>)/sqrt(2).

------------------------------------------------------------------------

Pregunta 5.  ¿Por que el espacio de estados de un qubit puro es la
             superficie de una esfera (2 grados de libertad)?

    A) Tiene 2 amplitudes complejas = 4 numeros reales; la normalizacion
       quita 1 y la fase global quita otro, quedan 2.
    B) Porque solo tiene 2 estados de base.
    C) Porque theta y phi siempre son iguales.
    D) Porque al medir hay 2 resultados posibles.

------------------------------------------------------------------------

Pregunta 6.  En |psi> = cos(theta/2)|0> + e^(i*phi) sin(theta/2)|1>,
             ¿que controla phi (el angulo azimutal) y cuando es visible?

    A) Las probabilidades; siempre es visible.
    B) La fase relativa; es invisible al medir en la base computacional y
       visible al cambiar de base.
    C) La fase global; nunca es medible.
    D) La normalizacion del estado.

------------------------------------------------------------------------

Pregunta 7.  Sobre las compuertas S y T del catalogo, ¿cual afirmacion es
             correcta?

    A) S = raiz(Z) y T = raiz-cuarta(Z); aplicar T dos veces da S, y S dos
       veces da Z.
    B) S = raiz(X) y T = raiz(Y).
    C) T = raiz(Z) y S = raiz-cuarta(Z).
    D) S y T son la misma compuerta.

------------------------------------------------------------------------

Pregunta 8.  ¿Por que el modo ECB filtra informacion?

    A) Porque la llave cambia en cada bloque.
    B) Porque bloques de texto plano identicos producen siempre bloques de
       texto cifrado identicos, y la estructura sobrevive al cifrado.
    C) Porque usa un IV aleatorio por bloque.
    D) Porque AES en si esta roto matematicamente.

------------------------------------------------------------------------

Pregunta 9.  En CBC se cumple  P_i = D(C_i) xor C_(i-1).  Un "padding
             oracle" (un servicio que revela si el relleno PKCS#7 es valido)
             le permite a un atacante:

    A) Recuperar directamente la llave de AES.
    B) Descifrar, e incluso forjar textos cifrados, sin la llave, usando
       solo la senal de padding valido/invalido.
    C) Nada; que el padding sea valido o no, no filtra informacion.
    D) Solo acelerar la fuerza bruta de la llave.

------------------------------------------------------------------------

Pregunta 10. "El cifrado da confidencialidad, no integridad." Segun la
             sesion, ¿que se concluye?

    A) El bit flipping en CBC muestra que un atacante puede alterar el texto
       plano de forma predecible; para integridad se usa HMAC o un modo
       autenticado como AES-GCM.
    B) CBC garantiza que el mensaje no puede modificarse.
    C) ECB da integridad porque los bloques son independientes.
    D) Un padding oracle proporciona integridad.

------------------------------------------------------------------------
"""

# Escriba aqui sus respuestas (la letra entre comillas, p. ej. "A").
# Deje None en las que no responda.
RESPUESTAS = {
    1: "B",
    2: "A",
    3: "C",
    4: "B",
    5: "A",
    6: "B",
    7: "A",
    8: "B",
    9: "B",
    10: "A",
}
