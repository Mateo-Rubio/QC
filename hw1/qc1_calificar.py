"""
Calificador del Taller 1
========================

    python qc1_calificar.py

Nota total sobre 5.0.  Todos los ítems valen lo mismo (igual que el
autograder de GitHub Classroom, que reparte los puntos por partes iguales
entre todos los tests de pytest):

  * 8 tests de Qiskit (qc1_test.py: example_not + las 7 funciones de qc1.py)
  * 16 preguntas de selección múltiple (qc1_quiz_test.py sobre qc1_quiz.py)

  24 ítems en total -> cada ítem vale 5/24 ≈ 0.21.

##########################
# NO MODIFIQUE ESTE ARCHIVO.  SOLO EJECÚTELO PARA VER SU NOTA.
##########################
"""
import importlib
import io
import traceback
from contextlib import redirect_stdout

NOTA_MAXIMA = 5.0

TESTS_QISKIT = [
    "test_example_not",
    "test_hadamard",
    "test_one_state",
    "test_phase",
    "test_figure_it_out_1",
    "test_figure_it_out_2",
    "test_figure_it_out_3",
    "test_figure_it_out_4",
]


def calificar_qiskit():
    """Ejecuta cada test de qc1_test.py. Devuelve (aprobados, total, detalle)."""
    detalle = []
    try:
        qc1_test = importlib.import_module("qc1_test")
    except Exception:  # noqa: BLE001
        traceback.print_exc()
        return 0, len(TESTS_QISKIT), [(t, False, "no se pudo importar qc1/qc1_test") for t in TESTS_QISKIT]

    aprobados = 0
    for nombre in TESTS_QISKIT:
        fn = getattr(qc1_test, nombre, None)
        if fn is None:
            detalle.append((nombre, False, "test no encontrado"))
            continue
        try:
            with redirect_stdout(io.StringIO()):
                fn()
            aprobados += 1
            detalle.append((nombre, True, ""))
        except AssertionError:
            detalle.append((nombre, False, "el statevector no coincide"))
        except Exception as exc:  # noqa: BLE001
            detalle.append((nombre, False, f"{type(exc).__name__}: {exc}"))
    return aprobados, len(TESTS_QISKIT), detalle


def calificar_quiz():
    """Verifica RESPUESTAS de qc1_quiz.py. Devuelve (correctas, total, detalle)."""
    try:
        quiz_test = importlib.import_module("qc1_quiz_test")
    except Exception:  # noqa: BLE001
        traceback.print_exc()
        return 0, 16, []

    correctas = 0
    detalle = []
    for numero in quiz_test.PREGUNTAS:
        r, ok = quiz_test.verificar(numero)
        correctas += int(ok)
        detalle.append((numero, r, ok))
    return correctas, len(quiz_test.PREGUNTAS), detalle


def main():
    print("=" * 64)
    print("TALLER 1 - CALIFICACIÓN")
    print("=" * 64)

    ok_q, tot_q, det_q = calificar_qiskit()
    print(f"\n[1/2] Ejercicios de Qiskit ({ok_q}/{tot_q})")
    for nombre, paso, msg in det_q:
        print(f"  {'OK  ' if paso else 'FAIL'}  {nombre:<22} {msg}")

    ok_p, tot_p, det_p = calificar_quiz()
    print(f"\n[2/2] Selección múltiple ({ok_p}/{tot_p})")
    for numero, r, ok in det_p:
        if r is None:
            print(f"  --    Pregunta {numero:>2}: sin responder")
        else:
            print(f"  {'OK  ' if ok else 'FAIL'}  Pregunta {numero:>2}: {r}")

    total = tot_q + tot_p
    valor_item = NOTA_MAXIMA / total
    nota_qiskit = valor_item * ok_q
    nota_quiz = valor_item * ok_p
    nota = nota_qiskit + nota_quiz

    print("\n" + "-" * 64)
    print(f"  Ítems correctos   : {ok_q + ok_p}/{total}  (cada ítem vale {valor_item:.3f})")
    print(f"  Qiskit            : {nota_qiskit:.2f} / {valor_item * tot_q:.2f}")
    print(f"  Selección múltiple: {nota_quiz:.2f} / {valor_item * tot_p:.2f}")
    print(f"  NOTA FINAL        : {nota:.2f} / {NOTA_MAXIMA:.1f}")
    print("-" * 64)
    return nota


if __name__ == "__main__":
    main()
