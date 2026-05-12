# Roteiro do workshop — automação de testes com Python

Público: Python básico. Ferramenta: **pytest**.

---

## Versão ~1 hora


| Min   | Atividade                                                                                                                           |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 0–5   | **Caça aos bugs:** duplas, 5 min, máximo de bugs reprodutíveis vs docstring.                                                        |
| 5–10  | **Debrief:** quantos acharam só no REPL/CLI? Intro: testes = especificação executável.                                              |
| 10–22 | **Leitura guiada** de `calculadora_bugada.py`: ramificações, limites, lista vazia.                                                  |
| 22–25 | **Setup:** `python -m venv .venv`, ativar, `pip install -r requirements.txt`.                                                       |
| 25–40 | **Primeiro pytest:** criar/editar `tests/test_calculadora.py`; um `assert` que documenta um bug (pode ficar vermelho). `pytest -v`. |
| 40–55 | **Parametrização:** `@pytest.mark.parametrize` com 6–10 linhas de casos (decimais, listas, negativos).                              |
| 55–60 | **Fecho:** `pytest` reroda tudo em segundos; papel dos testes na regressão.                                                         |


Corte: não corrigir o código da calculadora no workshop curto; foque em **testes verdes/vermelhos**.

---

## Versão ~2 horas


| Min     | Atividade                                                                                                                                                                       |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0–5     | Caça aos bugs (igual).                                                                                                                                                          |
| 5–12    | Debrief + objetivos do dia.                                                                                                                                                     |
| 12–30   | Leitura guiada + cada pessoa aponta um `if` ou ramo suspeito.                                                                                                                   |
| 30–38   | Setup venv + pytest.                                                                                                                                                            |
| 38–60   | Primeiros testes: smoke + um teste que falha (bug conhecido) + `pytest.raises` para `media([])` ou `dividir(1,0)` **conforme a docstring** (esperado vs real pode surpreender). |
| 60–85   | Parametrização: meta 10–15 casos; discutir nomes de testes legíveis.                                                                                                            |
| 85–105  | **Opcional:** TDD mini — escolher **um** bug, escrever teste verde após corrigir **só essa** função (ou deixar vermelho como documentação do bug).                              |
| 105–120 | Encerramento: CI/local, rerunning, dívida técnica se não corrigir tudo.                                                                                                         |


---

## Comandos úteis (quadro)

```text
python calculadora_bugada.py
pytest -v
pytest tests/test_calculadora_exemplo.py -v
```

Windows (PowerShell): `.\.venv\Scripts\Activate.ps1`  
Linux/macOS: `source .venv/bin/activate`

---

## Materiais

- `[CASOS_SUGERIDOS.md](CASOS_SUGERIDOS.md)` — para quem travar na caça.
- `[PONTUACAO_CAÇA.md](PONTUACAO_CAÇA.md)` — folha de pontuação.
- `[BUGS_INSTRUTOR.md](BUGS_INSTRUTOR.md)` — gabarito (não distribuir aos alunos).
- `[SNIPPET_PARAMETRIZACAO.py](SNIPPET_PARAMETRIZACAO.py)` — exemplo de `@pytest.mark.parametrize` para projetar ou copiar.

