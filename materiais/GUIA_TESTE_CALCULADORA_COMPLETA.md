# Guia didático: `tests/test_calculadora_completa.py`

Este documento explica **ficheiro por ficheiro / linha a linha** o que o código faz, para poderes **replicar** com outro módulo e **ensinar** os alunos.

---

## 1. Objetivo do ficheiro

- **Ficheiro testado:** `calculadora_bugada.py` (importado no teste).
- **Fonte da verdade:** a **docstring** no topo de `calculadora_bugada.py` — o que a API *deveria* fazer.
- **Efeito prático:** enquanto a implementação tiver **bugs de propósito**, muitos testes **falham**. Quando o código for corrigido para cumprir a docstring, o objetivo é **tudo a verde** (`pytest` sem falhas).

Conceito-chave para a turma: *teste automatizado = regra escrita em código; o computador verifica se o programa cumpre a regra em segundos.*

---

## 2. Estrutura geral


| Parte do ficheiro                                  | Função                                                                                             |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Docstring do módulo (linhas 1–5)                   | Explica o propósito e o que significa “falhas esperadas”.                                          |
| Imports (7–25)                                     | `Decimal` para o arredondamento; `pytest` para correr testes; funções **públicas** da calculadora. |
| Função auxiliar `_arredondar_conforme_doc` (28–30) | Define o “resultado certo” do arredondamento segundo a docstring.                                  |
| Blocos `test_`*                                    | Um bloco por função da calculadora, com comentários `# --- nome ---` para leitura no editor.       |


O **pytest** procura funções cujo nome começa por `test_` e executa-as. Cada `test_`* é **um** teste lógico; com `@pytest.mark.parametrize` um único `test_`* corre **várias** vezes (uma por linha da tabela).

---

## 3. Docstring do módulo (linhas 1–5)

```text
""" ... """
```

- Explica que os testes medem o código **contra a docstring** de `calculadora_bugada`.
- Avisa que, com bugs plantados, **falhas são normais** no workshop; com implementação correta, **todos passam**.

**Para ensinar:** distingue “o teste está mal” de “o **código** não cumpre a regra” — aqui a regra é a docstring.

---

## 4. Imports (linhas 7–25)

**Linha 7** — `from decimal import ROUND_HALF_UP, Decimal`  

- `Decimal` evita confusão de **vírgula flutuante** (ex.: `0.1 + 0.2` em `float` não é exatamente `0.3`).  
- `ROUND_HALF_UP` implementa o “**meio para cima**” da docstring da calculadora (arredondar a duas casas).

**Linha 10** — `import pytest`  

- Biblioteca de testes: fornece `pytest.mark.parametrize`, `pytest.raises`, `pytest.approx`, etc.

**Linhas 12–25** — `from calculadora_bugada import (...)`  

- Importa **só** o que o ficheiro de teste precisa (cada função pública a testar).  
- Não se importa `_cli` (interface de linha de comandos) porque estes testes focam a **lógica** em funções.

**Para ensinar:** o teste e o módulo testado são ficheiros **separados**; o teste “puxa” a API pública com `import`, como faria outro módulo.

---

## 5. Função auxiliar (linhas 28–30)

```python
def _arredondar_conforme_doc(x: float) -> float:
    """Duas casas, meio para cima (regra da docstring)."""
    return float(Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
```

- Nome com **underscore** (`_arredondar_...`): convenção de “**uso interno** deste ficheiro**; o pytest **não** trata isto como teste (não começa por `test_`).
- `str(x)`: passa o `float` a texto e depois a `Decimal` — reduz surpresas de representação binária.
- `quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)`: arredonda a **duas casas** com a regra da docstring.
- O **retorno** volta a `float` para comparar com `arredondar_duas_casas` da calculadora.

**Para ensinar:** em testes, é comum ter **pequenos “oráculos”** (funções que calculam o valor esperado por uma regra clara) em vez de copiar números à mão.

---

## 6. Bloco `somar` (linhas 33–49)

`**@pytest.mark.parametrize` (linhas 36–44)**  

- **Primeiro argumento:** nomes dos parâmetros em string, aqui `"a,b,esperado"`.  
- **Segundo argumento:** lista de **tuplos**; cada tuplo é **uma** execução do teste.  
- Ex.: `(1.9, 1.1, 3.0)` chama o mesmo `test_somar` com `a=1.9`, `b=1.1`, `esperado=3.0`.

`**def test_somar(a, b, esperado):` (linhas 44–45)**  

- Nome `test_` + `assert` → o pytest sabe que é teste.  
- `assert somar(a, b) == esperado` — se for falso, o teste **falha** e o pytest mostra os valores.

`**test_somar_floats_sem_perder_decimais` (48–49)**  

- Caso à parte: `0.1 + 0.2` em ponto flutuante nunca é **igual** a `0.3` com `==`.  
- `pytest.approx(0.3)` diz: “aceita valores **muito próximos** de 0.3” (tolerância numérica).

**Para ensinar:** *parametrização* = tabela de casos; *approx* = comparação de `float` com tolerância.

---

## 7. Bloco `subtrair` (linhas 52–57)

- Uma linha de `parametrize` com três casos: `(10,3,7)`, `(0,5,-5)`, `(-1,-4,3)`.
- Cada um verifica se `subtrair(a, b)` devolve `a - b` segundo a docstring.

**Para ensinar:** o mesmo padrão `a, b, esperado` repete-se noutros testes; só mudam a função e a tabela.

---

## 8. Bloco `multiplicar` (linhas 60–73)

- Tabela com casos de sinais, negativos×negativos, e zero.
- Tudo com `==` exato, porque estes resultados são inteiros exatos (não precisam de `approx`).

---

## 9. Bloco `dividir` (linhas 76–86)

`**test_dividir_ok` (79–81)**  

- Testa divisões **normais** (divisor ≠ 0).

`**test_dividir_por_zero_levanta` (84–86)**  

- `with pytest.raises(ZeroDivisionError):` abre um **contexto**: o bloco `with` exige que, ao correr `dividir(1, 0)`, o Python levante **exatamente** `ZeroDivisionError`.  
- Se a função devolver um número (ex.: infinito) em vez de levantar, o teste **falha** — o que acontece com a calculadora bugada.

**Para ensinar:** *“não basta o resultado ser errado; às vezes a regra é: tem de **dar erro**”* — aí usa-se `pytest.raises(TipoDeErro)`.

---

## 10. Bloco `media` (linhas 89–99)

`**test_media_lista_vazia_levanta` (92–94)**  

- Espera `ValueError` ao chamar `media([])` (regra da docstring). A implementação bugada pode devolver `0` — o teste falha.

`**test_media_lista_nao_vazia` (97–99)**  

- Lista com um elemento, três elementos (média 20), quatro elementos (média 2.5).

---

## 11. Bloco `percentual_do_total` (linhas 102–119)

`**test_percentual_do_total_ok` (105–114)**  

- Fórmula da docstring: `(parte / total) * 100`.  
- Usa `pytest.approx(esperado)` porque os resultados são floats.

`**test_percentual_total_zero_levanta` (117–119)**  

- Quando `total == 0`, a docstring exige `ValueError`. Chama-se `percentual_do_total(10, 0)` dentro de `pytest.raises(ValueError)`.

---

## 12. Bloco `potencia` (linhas 122–133)

`**test_potencia_ok` (125–127)**  

- Casos em que `base ** expoente` está bem definido e `expoente >= 0`.

`**test_potencia_expoente_negativo_levanta` (130–133)**  

- Para expoentes negativos, a docstring pede `ValueError`; a calculadora bugada pode devolver só `base`.

---

## 13. Bloco `valor_absoluto` (linhas 136–141)

- Mistura inteiros e decimais; para `-0.5` usa-se `approx` por consistência com floats.

---

## 14. Blocos `maximo_de_dois` e `minimo_de_dois` (linhas 144–154)

- Tabelas que cobrem maior distinto, menor distinto e **empate** `(7, 7, 7)` — importante para bugs que só aparecem nos limites.

---

## 15. Bloco `arredondar_duas_casas` (linhas 157–165)

- Só passa `x` no `parametrize`; o **esperado** vem de `_arredondar_conforme_doc(x)`.
- Compara a função da calculadora com o “oráculo” `Decimal` + `ROUND_HALF_UP`.
- Se a calculadora **trunca** em vez de arredondar, o teste falha em quase todos os `x`.

---

## 16. Bloco `soma_lista` (linhas 168–173)

- Três casos: lista vazia (soma 0), `[1,2,3]` (6), um só elemento `[10]` (10).  
- A implementação bugada soma o último elemento em duplicado — o teste de `[1,2,3]` detecta isso.

---

## 17. Como replicar este padrão noutro projeto

1. **Escrever a docstring** do módulo (regras claras: o que fazer, que erros levantar).
2. **Uma função = um grupo de testes** com comentário `# ---`.
3. **Casos normais:** `parametrize` com tuplos `(entrada..., resultado_esperado)`.
4. **Erros obrigatórios:** `with pytest.raises(ErroEsperado): funcão(...)`.
5. **Floats:** usar `pytest.approx` ou `Decimal` quando a igualdade estrita não for fiável.
6. **Rodar:** na raiz do projeto, `pytest tests/test_calculadora_completa.py -v`.

---

## 18. Comandos úteis para demonstração em sala

```powershell
# Todos os testes deste ficheiro, verboso
pytest tests/test_calculadora_completa.py -v

# Parar no primeiro erro (menos ruído ao explicar um caso)
pytest tests/test_calculadora_completa.py -x

# Só um teste pelo nome
pytest tests/test_calculadora_completa.py::test_dividir_por_zero_levanta -v
```

---

## 19. Glossário rápido para alunos


| Termo              | Significado                                                      |
| ------------------ | ---------------------------------------------------------------- |
| `assert`           | Afirma uma condição; se for falsa, o teste falha.                |
| `pytest`           | Programa que descobre e executa funções `test_*`.                |
| `parametrize`      | Repete o mesmo teste com várias linhas de dados (tabela).        |
| `pytest.raises(E)` | Garante que o código levanta exceção `E`.                        |
| `pytest.approx(x)` | Compara números à vírgula com tolerância.                        |
| Oráculo            | Função auxiliar que calcula o valor esperado por uma regra fixa. |


---

## Referência cruzada

- Código comentado neste guia: `[../tests/test_calculadora_completa.py](../tests/test_calculadora_completa.py)` (a partir de `materiais/`, sobe um nível com `..`).  
- Regras que os testes verificam: docstring de `[../calculadora_bugada.py](../calculadora_bugada.py)`.  
- Exemplo mínimo de teste: `[../tests/test_calculadora_exemplo.py](../tests/test_calculadora_exemplo.py)`.

---

## Anexo: mapa rápido **linha a linha** (ficheiro `test_calculadora_completa.py`)


| Linha(s) | O que faz                                                                                                                          |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 1–5      | Docstring do módulo de testes: avisa que os testes seguem a docstring da calculadora e que falhas são esperadas com código bugado. |
| 7        | Importa `ROUND_HALF_UP` e `Decimal` da biblioteca padrão `decimal` (arredondamento fiável).                                        |
| 8        | (vazio) separação visual.                                                                                                          |
| 10       | Importa o pacote `pytest`.                                                                                                         |
| 11       | (vazio)                                                                                                                            |
| 12–25    | Import multi-linha (`from calculadora_bugada import ...`) — lista todas as funções públicas que vão ser testadas.                  |
| 26–27    | Linhas em branco entre imports e código próprio.                                                                                   |
| 28–30    | Define `_arredondar_conforme_doc`: função auxiliar (oráculo) para comparar com `arredondar_duas_casas`.                            |
| 31       | (vazio)                                                                                                                            |
| 32–33    | Comentário de secção `# --- somar ---`.                                                                                            |
| 34       | (vazio)                                                                                                                            |
| 36–43    | Decorador `@pytest.mark.parametrize`: nome das variáveis `"a,b,esperado"` e lista de tuplos com casos de soma.                     |
| 44–45    | Função `test_somar`: para cada linha da tabela, verifica `somar(a,b) == esperado`.                                                 |
| 46       | (vazio)                                                                                                                            |
| 48–49    | Teste extra só para floats `0.1 + 0.2` com `pytest.approx`, porque `float` não é exato.                                            |
| 50–51    | Linhas em branco + secção subtrair.                                                                                                |
| 55–57    | `parametrize` numa linha + `test_subtrair`.                                                                                        |
| 60–73    | Secção multiplicar: tabela com vários sinais e zero.                                                                               |
| 76–81    | Dividir: casos válidos em tabela.                                                                                                  |
| 84–86    | Dividir por zero: **tem** de levantar `ZeroDivisionError` (`pytest.raises`).                                                       |
| 92–94    | Lista vazia na média: **tem** de levantar `ValueError`.                                                                            |
| 97–99    | Média com listas não vazias (1, 3 e 4 elementos).                                                                                  |
| 105–114  | Percentual em vários casos; `approx` nos resultados float.                                                                         |
| 117–119  | Total zero: **tem** de levantar `ValueError`.                                                                                      |
| 125–127  | Potências válidas (expoente ≥ 0).                                                                                                  |
| 130–133  | Expoente negativo: **tem** de levantar `ValueError`.                                                                               |
| 139–141  | Valor absoluto: tabela + `approx` onde há decimal.                                                                                 |
| 147–154  | Máximo e mínimo: inclui empates.                                                                                                   |
| 160–165  | Arredondar: quatro valores de `x`; esperado vem de `_arredondar_conforme_doc(x)`.                                                  |
| 171–173  | Soma de lista: vazio, três números, um número.                                                                                     |


*(Linhas vazias e comentários `# ---` não alteram o comportamento — só organizam o ficheiro.)*