# Casos para explorar (sem dar a solução)

Use o REPL ou `python calculadora_bugada.py ...` (corra sem argumentos para ver a ajuda).

- Decimais: `somar(1.9, 1.1)` — o que *deveria* sair pela regra da docstring?
- Negativos: `multiplicar(-2, -3)`, `subtrair(1, 2)`.
- Divisão: `dividir(1, 0)` — o que a docstring diz sobre erros?
- Listas: `media([])`, `media([10])`, `media([10, 20, 30])`.
- Percentagem: `percentual_do_total(25, 200)` — confere com a fórmula da docstring?
- Potência: `potencia(2, -1)` — é um caso válido segundo a docstring?
- Valor absoluto: `valor_absoluto(-7)`.
- Máximo/mínimo: `maximo_de_dois(3, 8)`, `minimo_de_dois(3, 8)`.
- Arredondamento: `arredondar_duas_casas(2.345)` — compare com uma calculadora ou com a regra “meio para cima”.
- Lista: `soma_lista([1, 2, 3])`.

Quando um caso falhar em relação à docstring, anota: **entrada**, **saída obtida**, **o que a docstring pede**.