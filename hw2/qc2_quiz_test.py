"""
Tests de las preguntas de seleccion multiple (qc2_quiz.py).

Se ejecutan con pytest (igual que qc2_test.py):

    pytest

o de forma individual:

    python qc2_quiz_test.py

##########################
# NO MODIFIQUE ESTE ARCHIVO.  SOLO EJECUTELO PARA VER LOS RESULTADOS.
##########################
"""
import hashlib

import qc2_quiz

_SAL = "QC2-taller2-uniandes"
_CLAVES = {
    1: "b49cc67f4079cb91923f122810da6238799a9244468b5fe17b3c98449e4f8274",
    2: "7415acc07eae14dbb5f97686ca46d06b669d2cfd50aa78da9f14fb64e235721c",
    3: "b2bc3d99e6ca50764b435b8a2dde3421d2b6860b2fe251ccd927eb0578a94bfb",
    4: "5bce3696601988e37581dd64fa09dd7ee223f4c0a8b32d52e3a8ef0676af4584",
    5: "15475eb8f330a5cb43364d822564df9398165fa95b16a1521959a008193e5473",
    6: "1af03960a8cbc27e94d7d31d27f9007ad530f858e86983ea062f76ecc3f10eea",
    7: "fec4525f07321770a1c3e9a4e70102cd4643a2965ca460c16db045a7ac0e7115",
    8: "a7ca88123b5445c9a0b1705b80aa281edb0272da68eea3abe1fedef472f6c02a",
    9: "a2f889d58fa4acd0e8db1c3f3455797329231e2f30c64fab16973dbd183a7c4c",
    10: "d28b4ff161dc6d53bc9d2fdf8223e2091d747d427bb0754dd2b91523080cb274",
}
PREGUNTAS = sorted(_CLAVES)


def _huella(numero, respuesta):
    return hashlib.sha256(f"{_SAL}|{numero}|{respuesta}".encode("utf-8")).hexdigest()


def _normalizar(respuesta):
    """'c', ' C) ', 'C' -> 'C'.  None o vacio -> None."""
    if respuesta is None:
        return None
    r = str(respuesta).strip().upper().rstrip(")").strip()
    return r or None


def verificar(numero):
    """Devuelve (respuesta_normalizada, es_correcta) para la pregunta `numero`."""
    r = _normalizar(dict(getattr(qc2_quiz, "RESPUESTAS", {})).get(numero))
    if r is None:
        return None, False
    return r, _huella(numero, r) == _CLAVES[numero]


def _comprobar(numero):
    r, ok = verificar(numero)
    assert r is not None, f"Pregunta {numero}: sin responder"
    assert ok, f"Pregunta {numero}: la respuesta '{r}' es incorrecta"
    print("SUCCESSFUL TEST")


##########################
# NO MODIFIQUE ESTE ARCHIVO.  SOLO EJECUTELO PARA VER LOS RESULTADOS.
##########################
def test_pregunta_01():
    """Pregunta 1: convenio de orden de qubits (little-endian)."""
    _comprobar(1)


def test_pregunta_02():
    """Pregunta 2: producto tensor de dos qubits."""
    _comprobar(2)


def test_pregunta_03():
    """Pregunta 3: la definicion del SWAP."""
    _comprobar(3)


def test_pregunta_04():
    """Pregunta 4: CNOT con control en |+> produce un estado de Bell."""
    _comprobar(4)


def test_pregunta_05():
    """Pregunta 5: grados de libertad de un qubit puro."""
    _comprobar(5)


def test_pregunta_06():
    """Pregunta 6: que controla phi en la esfera de Bloch."""
    _comprobar(6)


def test_pregunta_07():
    """Pregunta 7: relaciones entre S, T y Z."""
    _comprobar(7)


def test_pregunta_08():
    """Pregunta 8: por que ECB filtra informacion."""
    _comprobar(8)


def test_pregunta_09():
    """Pregunta 9: que permite un padding oracle en CBC."""
    _comprobar(9)


def test_pregunta_10():
    """Pregunta 10: cifrado no da integridad; HMAC o AES-GCM."""
    _comprobar(10)


##########################
# NO MODIFIQUE ESTE ARCHIVO.  SOLO EJECUTELO PARA VER LOS RESULTADOS.
##########################
if __name__ == "__main__":
    """Run this to verify if tests are failing"""
    test_pregunta_01()
    test_pregunta_02()
    test_pregunta_03()
    test_pregunta_04()
    test_pregunta_05()
    test_pregunta_06()
    test_pregunta_07()
    test_pregunta_08()
    test_pregunta_09()
    test_pregunta_10()
