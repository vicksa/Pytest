"""Exemplo mínimo que passa — ponto de partida para o workshop."""

from calculadora_bugada import somar


def test_soma_de_inteiros_simples_passa():
    assert somar(2, 3) == 5
