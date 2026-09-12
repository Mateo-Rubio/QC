"""
Calificador del Taller 2
========================

    python qc2_calificar.py

Nota total sobre 5.0.  Todos los items valen lo mismo (igual que el autograder
de GitHub Classroom, que reparte los puntos por partes iguales entre todos los
items):

  * 8  ejercicios de Qiskit          (qc2_test.py sobre qc2.py)
  * 10 preguntas de seleccion multiple (qc2_quiz_test.py sobre qc2_quiz.py)
  * 5  flags de los retos de cripto  (se validan en el servidor)

  23 items en total -> cada item vale 5/23 ≈ 0.217.

Las flags NO se pueden verificar en su maquina (el flag correcto vive en el
servidor, no en este archivo). Al correr localmente apareceran como pendientes
y no suman; cuando entregue en la plataforma, el servidor las valida y suman.

##########################
# NO MODIFIQUE ESTE ARCHIVO.  SOLO EJECUTELO PARA VER SU NOTA.
##########################
"""
import importlib
import io
import traceback
from contextlib import redirect_stdout

NOTA_MAXIMA = 5.0
TOTAL_FLAGS = 5

TESTS_QISKIT = [
    "test_figure_it_out_1",
    "test_figure_it_out_2",
    "test_figure_it_out_3",
    "test_figure_it_out_4",
    "test_figure_it_out_5",
    "test_figure_it_out_6",
    "test_figure_it_out_7",
    "test_figure_it_out_8",
]


def calificar_qiskit():
    """Ejecuta cada test de qc2_test.py. Devuelve (aprobados, total, detalle)."""
    detalle = []
    try:
        qc2_test = importlib.import_module("qc2_test")
    except Exception:  # noqa: BLE001
        traceback.print_exc()
        return 0, len(TESTS_QISKIT), [(t, False, "no se pudo importar qc2/qc2_test") for t in TESTS_QISKIT]

    aprobados = 0
    for nombre in TESTS_QISKIT:
        fn = getattr(qc2_test, nombre, None)
        if fn is None:
            detalle.append((nombre, False, "test no encontrado"))
            continue
        try:
            with redirect_stdout(io.StringIO()):
                fn()
            aprobados += 1
            detalle.append((nombre, True, ""))
        except AssertionError:
            detalle.append((nombre, False, "la salida no coincide"))
        except Exception as exc:  # noqa: BLE001
            detalle.append((nombre, False, f"{type(exc).__name__}: {exc}"))
    return aprobados, len(TESTS_QISKIT), detalle


def calificar_quiz():
    """Verifica RESPUESTAS de qc2_quiz.py. Devuelve (correctas, total, detalle)."""
    try:
        quiz_test = importlib.import_module("qc2_quiz_test")
    except Exception:  # noqa: BLE001
        traceback.print_exc()
        return 0, 10, []

    correctas = 0
    detalle = []
    for numero in quiz_test.PREGUNTAS:
        r, ok = quiz_test.verificar(numero)
        correctas += int(ok)
        detalle.append((numero, r, ok))
    return correctas, len(quiz_test.PREGUNTAS), detalle


def calificar_flags():
    """Lee el resultado de la verificacion de flags que produce el servidor.

    El archivo qc2_flags_verificados.py lo genera la plataforma (no existe al
    correr localmente). Devuelve (aprobadas, total, correctos, disponible).
    """
    try:
        ver = importlib.import_module("qc2_flags_verificados")
        correctos = dict(getattr(ver, "CORRECTOS", {}))
        disponible = True
    except Exception:  # noqa: BLE001
        correctos = {}
        disponible = False
    aprobadas = sum(1 for v in correctos.values() if v)
    return aprobadas, TOTAL_FLAGS, correctos, disponible


def main():
    print("=" * 64)
    print("TALLER 2 - CALIFICACION")
    print("=" * 64)

    ok_q, tot_q, det_q = calificar_qiskit()
    print(f"\n[1/3] Ejercicios de Qiskit ({ok_q}/{tot_q})")
    for nombre, paso, msg in det_q:
        print(f"  {'OK  ' if paso else 'FAIL'}  {nombre:<22} {msg}")

    ok_p, tot_p, det_p = calificar_quiz()
    print(f"\n[2/3] Seleccion multiple ({ok_p}/{tot_p})")
    for numero, r, ok in det_p:
        if r is None:
            print(f"  --    Pregunta {numero:>2}: sin responder")
        else:
            print(f"  {'OK  ' if ok else 'FAIL'}  Pregunta {numero:>2}: {r}")

    ok_f, tot_f, correctos_f, disponible_f = calificar_flags()
    if disponible_f:
        print(f"\n[3/3] Flags de cripto ({ok_f}/{tot_f})")
        for i in range(1, tot_f + 1):
            ok = correctos_f.get(i, False)
            print(f"  {'OK  ' if ok else 'FAIL'}  Flag {i}")
    else:
        print(f"\n[3/3] Flags de cripto (0/{tot_f})  [se validan en el servidor]")
        print("  Estas 5 se califican al entregar en la plataforma; localmente")
        print("  no suman porque el flag correcto no esta en este archivo.")

    total = tot_q + tot_p + tot_f
    valor_item = NOTA_MAXIMA / total
    nota_qiskit = valor_item * ok_q
    nota_quiz = valor_item * ok_p
    nota_flags = valor_item * ok_f
    nota = nota_qiskit + nota_quiz + nota_flags

    print("\n" + "-" * 64)
    print(f"  Items correctos   : {ok_q + ok_p + ok_f}/{total}  (cada item vale {valor_item:.3f})")
    print(f"  Qiskit            : {nota_qiskit:.2f} / {valor_item * tot_q:.2f}")
    print(f"  Seleccion multiple: {nota_quiz:.2f} / {valor_item * tot_p:.2f}")
    if disponible_f:
        print(f"  Flags de cripto   : {nota_flags:.2f} / {valor_item * tot_f:.2f}")
    else:
        print(f"  Flags de cripto   : pendientes (se validan en el servidor)")
    print(f"  NOTA FINAL        : {nota:.2f} / {NOTA_MAXIMA:.1f}")
    print("-" * 64)
    return nota


if __name__ == "__main__":
    main()
