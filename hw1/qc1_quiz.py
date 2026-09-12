"""
Taller 1 - Preguntas de selección múltiple
==========================================

Responda cada pregunta escribiendo la LETRA de la opción (por ejemplo "A",
"B", "C"...) dentro del diccionario RESPUESTAS, al final de este archivo.
No modifique nada más.

Los circuitos se dibujan como lo hace Qiskit (qc.draw('text')): el qubit
entra por la izquierda en |0⟩ y las compuertas se aplican de IZQUIERDA a
DERECHA.  Recuerde que, como se dijo en clase, la matriz del circuito se
obtiene multiplicando las matrices de DERECHA a IZQUIERDA.

Para calificar (preguntas + ejercicios de Qiskit) ejecute:

    python qc1_calificar.py

------------------------------------------------------------------------

Pregunta 1.  Si tenemos α|0⟩ + β|1⟩, ¿cuál es la probabilidad de que al
             hacer una medición el resultado sea |0⟩?

    A) 1/2
    B) β
    C) α
    D) α^2

------------------------------------------------------------------------

Pregunta 2.  Si tenemos α|0⟩ + β|1⟩ con

                 α = sqrt(3)/2
                 β = 1/2

             ¿cuál es el resultado con mayor probabilidad si medimos?

    A) |0⟩
    B) |1⟩
    C) no sé

------------------------------------------------------------------------

Pregunta 3.  Si tenemos un qubit con el estado 0.8|0⟩ + 0.6|1⟩, ¿cuál es
             la probabilidad de que la medición sea |1⟩?

    A) 0.38
    B) 0.6
    C) 0.64
    D) 0.36

------------------------------------------------------------------------

Pregunta 4.  Encuentre la matriz correspondiente al siguiente circuito.

                ┌───┐
            q0: ┤ X ├
                └───┘

    A) [[1,0],[1,0]]
    B) [[1,0],[0,1]]
    C) [[0,1],[1,0]]
    D) no sé

------------------------------------------------------------------------

Pregunta 5.  Encuentre la matriz correspondiente al siguiente circuito.
             Recuerde que el orden importa y se multiplica de derecha a
             izquierda.

                ┌───┐┌───┐
            q0: ┤ X ├┤ Z ├
                └───┘└───┘

    A) [[0,1],[-1,0]]
    B) [[1,0],[0,1]]
    C) [[0,1],[1,0]]
    D) no sé

------------------------------------------------------------------------

Pregunta 6.  Encuentre la matriz correspondiente al siguiente circuito.
             Recuerde que el orden importa y se multiplica de derecha a
             izquierda.

                ┌───┐┌───┐
            q0: ┤ Z ├┤ X ├
                └───┘└───┘

    A) [[0,-1],[1,0]]
    B) [[1,0],[0,-1]]
    C) [[0,1],[1,0]]
    D) no sé

------------------------------------------------------------------------

Pregunta 7.  Encuentre la matriz correspondiente al siguiente circuito.
             Recuerde que el orden importa y se multiplica de derecha a
             izquierda.

                ┌───┐┌───┐
            q0: ┤ X ├┤ H ├
                └───┘└───┘

    A) [[0,-1],[1,0]]
    B) [[0, 0.70710678+0.j], [0, 0.70710678+0.j]]
    C) [[ 0.70710678+0.j, 0.70710678+0.j], [-0.70710678+0.j, 0.70710678+0.j]]
    D) no sé

------------------------------------------------------------------------

Pregunta 8.  Encuentre la matriz correspondiente al siguiente circuito.
             Recuerde que el orden importa y se multiplica de derecha a
             izquierda.

                ┌───┐┌───┐
            q0: ┤ H ├┤ X ├
                └───┘└───┘

    A) [[ 0.70710678+0.j, -0.70710678+0.j], [ 0.70710678+0.j, 0.70710678+0.j]]
    B) [[0, 0.70710678+0.j], [0, 0.70710678+0.j]]
    C) [[ 0.70710678+0.j, 0.70710678+0.j], [-0.70710678+0.j, 0.70710678+0.j]]
    D) no sé

------------------------------------------------------------------------

Pregunta 9.  Encuentre la matriz correspondiente al siguiente circuito.
             Recuerde que el orden importa y se multiplica de derecha a
             izquierda.

                ┌───┐┌───┐┌───┐┌───┐
            q0: ┤ Z ├┤ X ├┤ Z ├┤ H ├
                └───┘└───┘└───┘└───┘

    A) H
    B) Z
    C) X
    D) (1/math.sqrt(2)) * [[1,1],[1,-1]]
    E) [[1,0],[1,0]]
    F) (1/math.sqrt(2)) * [[-1,-1],[1,-1]]

------------------------------------------------------------------------

Pregunta 10. ¿Cuál es el statevector del siguiente circuito?  Es decir,
             ¿cuál sería el estado de un qubit al operarse con ese
             circuito?  Recuerde que el qubit inicia en |0⟩.

                ┌───┐┌───┐┌───┐┌───┐
            q0: ┤ Z ├┤ X ├┤ Z ├┤ H ├
                └───┘└───┘└───┘└───┘

    A) [0, 1]
    B) [9, 9]
    C) [1, 0]
    D) [-0.70710678+0.j,  0.70710678+0.j]
    E) [ 0.70710678+0.j, -0.70710678+0.j]

------------------------------------------------------------------------

Pregunta 11. ¿Con qué compuerta (gate) operamos el qubit en estado
             1/sqrt(2)(|0⟩ + |1⟩) para quedar en el estado de la figura?
             (ver matrices en
             https://qiskit.org/textbook/ch-states/single-qubit-gates.html)

             Figura (esfera de Bloch): la flecha está sobre el ecuador y
             apunta exactamente a lo largo del eje +y.
             Vector de Bloch ≈ (x, y, z) = (0, 1, 0).

    A) H
    B) X
    C) Z
    D) S

------------------------------------------------------------------------

Pregunta 12. ¿Con qué compuerta (gate) operamos |0⟩ para quedar en el
             estado de la figura?

             Figura (esfera de Bloch): la flecha apunta hacia abajo, al
             polo sur |1⟩.
             Vector de Bloch ≈ (x, y, z) = (0, 0, -1).

    A) H
    B) X
    C) Z
    D) S

------------------------------------------------------------------------

Pregunta 13. ¿Con qué compuerta (gate) operamos el qubit en estado
             1/sqrt(2)(|0⟩ + |1⟩) para quedar en el estado de la figura?
             (ver matrices en
             https://qiskit.org/textbook/ch-states/single-qubit-gates.html)

             Figura (esfera de Bloch): la flecha está sobre el ecuador, a
             mitad de camino (45°) entre el eje +x y el eje +y.
             Vector de Bloch ≈ (x, y, z) = (0.71, 0.71, 0).

    A) H
    B) T
    C) Z
    D) S

------------------------------------------------------------------------

Pregunta 14. Sobre el vector de estado α|0⟩ + β|1⟩ y la esfera de Bloch:

    A) Contienen exactamente la misma información.
    B) La esfera de Bloch contiene más información (agrega la dirección
       espacial).
    C) El vector de estado contiene más: la esfera descarta la fase
       global γ.
    D) Ninguno de los dos describe completamente un qubit aislado.

------------------------------------------------------------------------

Pregunta 15. En |Ψ⟩ = cos(c)·e^(ia)|0⟩ + sin(c)·e^(ib)|1⟩, ¿qué se puede
             medir en un qubit *aislado*?

    A) Solo c.
    B) c y la diferencia (b − a), pero nunca a y b por separado.
    C) a y b por separado, si se rota el instrumento.
    D) Los tres ángulos.

------------------------------------------------------------------------

Pregunta 16. "Pitágoras" aparece tres veces en esa fórmula (dentro de cada
             coeficiente polar, y en cos²(c) + sin²(c) = 1).  ¿Cuál de
             esas apariciones es una *ley de la naturaleza*?

    A) La que está dentro del coeficiente de α.
    B) Solo la normalización cos²(c) + sin²(c) = 1; las otras dos son
       identidades automáticas de la forma polar.
    C) Las tres por igual.
    D) Ninguna: las tres son notación.

------------------------------------------------------------------------
"""

# Escriba aquí sus respuestas (la letra entre comillas, p. ej. "A").
# Deje None en las que no responda.
RESPUESTAS = {
    1: "D",
    2: "A",
    3: "D",
    4: "C",
    5: "A",
    6: "A",
    7: "C",
    8: "A",
    9: "F",
    10: "D",
    11: "D",
    12: "B",
    13: "B",
    14: "C",
    15: "B",
    16: "B",
}
