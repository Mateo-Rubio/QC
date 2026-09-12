"""
Tests de las preguntas de seleccion multiple (qc1_quiz.py).

Se ejecutan con pytest (igual que qc1_test.py):

    pytest

o de forma individual:

    python qc1_quiz_test.py

##########################
# NO MODIFIQUE ESTE ARCHIVO.  SOLO EJECUTELO PARA VER LOS RESULTADOS.
##########################
"""
import hashlib

import qc1_quiz

_SAL = "QC1-taller1-uniandes"
_CLAVES = {
    1: "9deeab8950008c46cf19c61241abb659840661baa9f4a6528fe717ea7d159985",
    2: "427c4aaa3715ce5152d9878d9bb3fec10bb727e4bff0671c4cb7259996ff65b7",
    3: "9e79d0e5cf0217f9bb15886adac7586b6bb163cf925e10d14921368f3678b12d",
    4: "cc7c8af0f78bd45d050d7e11223604d564368899292d0aa3310b8d09f6a47a2a",
    5: "3ab3b9b7da873bb58b7d62961b6b84ddd8ff9c7714cb4b05516f4ddc1f9b59a5",
    6: "83d5c370b4854284f101f5aec3170ace295b81458256d14211c440920db033c6",
    7: "d8ef9927d73fe626a75c205fbccd8170ebb9072f13f69bb0749c3c4c335f0aa2",
    8: "29d7e45988aeedbf3d32dd95a847db787d4185d63a39f913b736451ff7a4e12f",
    9: "e5694d8a4d0535e52bd4617591bb10d3591111ec211defc2984ecdf0207d1eaa",
    10: "bc2e5bfb124b2ab93f41eb19df54ceabc3d8ef79ce6b412e0c6ea41d7bc75b2b",
    11: "486bbd4a0429d46c0efcf2ca6d892f5c09b6e07d9ce5d4daef2a7d3b38f6d833",
    12: "bf11a725cc61ed5b6385cb09419d1c80bbc6bce64444010c6bbbba3f126adbfe",
    13: "42862c1a6f35195bbe25c44bc96ab851bc383c8d4182ba849744f0442a57ec52",
    14: "a471c9c2babfcf6731b7cd93db1e89e6e95e0bc6809ff0a6bfef959e676c7284",
    15: "eeee510474a548793269d2b5cd2280e7c697f0b95473e5505b564e8dc2bc7a5a",
    16: "f16270c5ae014081cbd202ded5715a339e20cc3133a9bd59753e6fa91da4749d",
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
    r = _normalizar(dict(getattr(qc1_quiz, "RESPUESTAS", {})).get(numero))
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
    """Pregunta 1: probabilidad de medir |0> en a|0> + b|1>."""
    _comprobar(1)


def test_pregunta_02():
    """Pregunta 2: resultado mas probable con a=sqrt(3)/2, b=1/2."""
    _comprobar(2)


def test_pregunta_03():
    """Pregunta 3: probabilidad de medir |1> en 0.8|0> + 0.6|1>."""
    _comprobar(3)


def test_pregunta_04():
    """Pregunta 4: matriz del circuito X."""
    _comprobar(4)


def test_pregunta_05():
    """Pregunta 5: matriz del circuito X, Z."""
    _comprobar(5)


def test_pregunta_06():
    """Pregunta 6: matriz del circuito Z, X."""
    _comprobar(6)


def test_pregunta_07():
    """Pregunta 7: matriz del circuito X, H."""
    _comprobar(7)


def test_pregunta_08():
    """Pregunta 8: matriz del circuito H, X."""
    _comprobar(8)


def test_pregunta_09():
    """Pregunta 9: matriz del circuito Z, X, Z, H."""
    _comprobar(9)


def test_pregunta_10():
    """Pregunta 10: statevector del circuito Z, X, Z, H."""
    _comprobar(10)


def test_pregunta_11():
    """Pregunta 11: compuerta que lleva |+> al eje +y."""
    _comprobar(11)


def test_pregunta_12():
    """Pregunta 12: compuerta que lleva |0> a |1>."""
    _comprobar(12)


def test_pregunta_13():
    """Pregunta 13: compuerta que lleva |+> a 45 grados entre +x y +y."""
    _comprobar(13)


def test_pregunta_14():
    """Pregunta 14: statevector vs. esfera de Bloch."""
    _comprobar(14)


def test_pregunta_15():
    """Pregunta 15: que se puede medir en un qubit aislado."""
    _comprobar(15)


def test_pregunta_16():
    """Pregunta 16: cual "Pitagoras" es ley de la naturaleza."""
    _comprobar(16)


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
    test_pregunta_11()
    test_pregunta_12()
    test_pregunta_13()
    test_pregunta_14()
    test_pregunta_15()
    test_pregunta_16()
