"""
Exemplo para copiar no workshop (não é importado pelo pytest).

Coloquem isto dentro de tests/test_calculadora.py e ajustem os valores.
"""

import pytest

from calculadora_bugada import somar


@pytest.mark.parametrize(
    "a,b,esperado_pela_docstring",
    [
        (2, 3, 5),
        (1.9, 1.1, 3.0),
        (-1, 1, 0),
    ],
)
def test_somar_contra_docstring(a, b, esperado_pela_docstring):
    assert somar(a, b) == esperado_pela_docstring
