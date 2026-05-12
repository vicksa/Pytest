# Workshop: automação de testes com Python (calculadora bugada)

Material para 1–2 horas 
## Arranque rápido

```bash
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -v
```

**Linux / macOS:**

```bash
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## Ficheiros principais


| Ficheiro                                                                     | Descrição                                                                           |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `[calculadora_bugada.py](calculadora_bugada.py)`                             | API com regras na docstring do módulo; implementação intencionalmente incorreta.    |
| `[tests/test_calculadora_exemplo.py](tests/test_calculadora_exemplo.py)`     | Um teste que **passa** — exemplo de sintaxe.                                        |
| `[tests/test_calculadora_completa.py](tests/test_calculadora_completa.py)`   | Testes de **toda** a API segundo a docstring (enquanto houver bugs, muitos falham). |
| `[materiais/ROTEIRO.md](materiais/ROTEIRO.md)`                               | Cronograma 1 h e 2 h.                                                               |
| `[materiais/PONTUACAO_CAÇA.md](materiais/PONTUACAO_CAÇA.md)`                 | Folha da competição 5 minutos.                                                      |
| `[materiais/CASOS_SUGERIDOS.md](materiais/CASOS_SUGERIDOS.md)`               | Pistas sem soluções.                                                                |
| `[materiais/SNIPPET_PARAMETRIZACAO.py](materiais/SNIPPET_PARAMETRIZACAO.py)` | Exemplo de parametrização para demonstração.                                        |
| `[materiais/GUIA_TESTE_CALCULADORA_COMPLETA.md](materiais/GUIA_TESTE_CALCULADORA_COMPLETA.md)` | Guia didático do `test_calculadora_completa.py` (para replicar e ensinar). |


## Brincar na linha de comandos

```bash
python calculadora_bugada.py somar 2 3.7
python calculadora_bugada.py media 10 20 30
```

## Testar a calculadora inteira

```powershell
pytest tests/test_calculadora_completa.py -v
```

Os testes comparam o código com a **docstring** do módulo. Com a calculadora “bugada”, **esperam-se falhas** até corrigires a implementação (ou comentares/ignorares testes durante o workshop).

## `ModuleNotFoundError: No module named 'calculadora_bugada'`

- Corre `pytest` **na raiz** do projeto (a pasta onde está `calculadora_bugada.py`,
