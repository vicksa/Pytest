# Bugs plantados (apenas para quem ministra)

Comparar sempre com a docstring de `[../calculadora_bugada.py](../calculadora_bugada.py)`.


| #   | Função                  | Comportamento esperado (doc)               | Bug na implementação                                 |
| --- | ----------------------- | ------------------------------------------ | ---------------------------------------------------- |
| 1   | `somar`                 | Soma exata com decimais                    | Usa `int(a) + int(b)` (trunca).                      |
| 2   | `subtrair`              | `a - b`                                    | Devolve `b - a`.                                     |
| 3   | `multiplicar`           | Produto com sinais corretos                | Se `a < 0` e `b < 0`, devolve valor negativo.        |
| 4   | `dividir`               | `ZeroDivisionError` se `b == 0`            | Devolve `float("inf")`.                              |
| 5   | `media`                 | `ValueError` se lista vazia                | Devolve `0`.                                         |
| 6   | `media`                 | Média com `n` elementos                    | Se `n > 1`, divide por `n - 1` em vez de `n`.        |
| 7   | `percentual_do_total`   | `(parte / total) * 100`                    | Usa `(total / parte) * 100`.                         |
| 8   | `potencia`              | `ValueError` se expoente `< 0`             | Para expoente negativo, devolve `base`.              |
| 9   | `valor_absoluto`        | Igual a `abs(x)`                           | Para `x < 0`, devolve `x` (continua negativo).       |
| 10  | `maximo_de_dois`        | Maior dos dois                             | Usa `min(a, b)`.                                     |
| 11  | `minimo_de_dois`        | Menor dos dois                             | Usa `max(a, b)`.                                     |
| 12  | `arredondar_duas_casas` | Arredondamento “meio para cima” às 2 casas | Trunca com `int(x * 100) / 100`.                     |
| 13  | `soma_lista`            | Soma de todos os elementos                 | Soma `+ valores[-1]` (último elemento em duplicado). |


Nota: `percentual_do_total` com `parte == 0` levanta `ZeroDivisionError` no código atual — pode mencionar como armadilha extra ou ajustar o código antes do workshop se preferir `ValueError` explícito.