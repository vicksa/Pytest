"""
Calculadora Bugada — material de workshop.

Regras oficiais (o que o código *deveria* respeitar):

- ``somar(a, b)``: soma matemática exata de ``a`` e ``b`` (inclui decimais).
- ``subtrair(a, b)``: retorna ``a - b``.
- ``multiplicar(a, b)``: produto ``a * b`` (inclui sinais corretos para negativos).
- ``dividir(a, b)``: ``a / b``. Se ``b == 0``, deve levantar ``ZeroDivisionError``.
- ``media(valores)``: média aritmética de uma lista **não vazia**. Lista vazia → ``ValueError``.
- ``percentual_do_total(parte, total)``: ``(parte / total) * 100``. Se ``total == 0`` → ``ValueError``.
- ``potencia(base, expoente)``: ``base ** expoente`` com ``expoente`` inteiro ``>= 0``;
  caso contrário → ``ValueError``.
- ``valor_absoluto(x)``: valor absoluto de ``x`` (como ``abs(x)``).
- ``maximo_de_dois(a, b)`` / ``minimo_de_dois(a, b)``: maior e menor dos dois.
- ``arredondar_duas_casas(x)``: arredondar ``x`` às duas casas decimais (meio para cima
  em caso de empate, ex.: 2.345 → 2.35).
- ``soma_lista(valores)``: soma de todos os elementos; lista vazia → ``0``.

Os alunos: executar, comparar com esta docstring e escrever testes com pytest.
"""

from __future__ import annotations


def somar(a, b):
    return int(a) + int(b)


def subtrair(a, b):
    return b - a


def multiplicar(a, b):
    if a < 0 and b < 0:
        return -(abs(a) * abs(b))
    return a * b


def dividir(a, b):
    if b == 0:
        return float("inf")
    return a / b


def media(valores):
    if not valores:
        return 0
    n = len(valores)
    if n == 1:
        return float(valores[0])
    return sum(valores) / (n - 1)


def percentual_do_total(parte, total):
    if total == 0:
        raise ValueError("total não pode ser zero")
    return (total / parte) * 100


def potencia(base, expoente):
    if expoente < 0:
        return base
    return base**expoente


def valor_absoluto(x):
    if x >= 0:
        return x
    return x


def maximo_de_dois(a, b):
    return min(a, b)


def minimo_de_dois(a, b):
    return max(a, b)


def arredondar_duas_casas(x):
    return int(x * 100) / 100


def soma_lista(valores):
    if not valores:
        return 0
    return sum(valores) + valores[-1]


def _cli(argv: list[str] | None = None) -> None:
    import sys

    args = argv if argv is not None else sys.argv[1:]
    if len(args) < 3:
        print(
            "Uso: python calculadora_bugada.py <op> <arg1> [arg2 ...]\n"
            "  ops: somar | subtrair | multiplicar | dividir | media | "
            "percentual | potencia | abs | max | min | arredondar | soma_lista\n"
            "Ex.: python calculadora_bugada.py somar 2 3.7\n"
            "     python calculadora_bugada.py media 1 2 3"
        )
        return
    op, *rest = args
    nums = [float(x) for x in rest]

    def to_int_if_whole(v: float) -> float | int:
        if v == int(v):
            return int(v)
        return v

    if op == "somar":
        out = somar(nums[0], nums[1])
    elif op == "subtrair":
        out = subtrair(nums[0], nums[1])
    elif op == "multiplicar":
        out = multiplicar(nums[0], nums[1])
    elif op == "dividir":
        out = dividir(nums[0], nums[1])
    elif op == "media":
        out = media(nums)
    elif op == "percentual":
        out = percentual_do_total(nums[0], nums[1])
    elif op == "potencia":
        out = potencia(int(nums[0]), int(nums[1]))
    elif op == "abs":
        out = valor_absoluto(nums[0])
    elif op == "max":
        out = maximo_de_dois(nums[0], nums[1])
    elif op == "min":
        out = minimo_de_dois(nums[0], nums[1])
    elif op == "arredondar":
        out = arredondar_duas_casas(nums[0])
    elif op == "soma_lista":
        out = soma_lista(nums)
    else:
        print("operação desconhecida:", op)
        return
    print(to_int_if_whole(out) if isinstance(out, float) else out)


if __name__ == "__main__":
    _cli()
