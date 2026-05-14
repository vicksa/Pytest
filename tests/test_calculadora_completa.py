# Aspas triplas abrem um texto de documentação (docstring) explicando o objetivo geral do arquivo.
"""
Testes da calculadora segundo a **docstring** de `calculadora_bugada` (comportamento esperado).

Enquanto o código tiver bugs plantados, **vários testes falham** — isso é esperado no workshop.
Quando a implementação estiver correta, todos devem passar.
"""

# Importa a regra de arredondamento escolar (ROUND_HALF_UP) e o tipo de número super preciso (Decimal).
from decimal import ROUND_HALF_UP, Decimal

# Importa o nosso "inspetor de qualidade", a biblioteca pytest, que vai executar as verificações.
import pytest

# Importa do nosso arquivo principal (calculadora_bugada.py) todas as funções que serão testadas.
# Os parênteses servem apenas para permitir a quebra de linha nas importações e deixar o código bonito.
from calculadora_bugada import (
    arredondar_duas_casas,
    dividir,
    maximo_de_dois,
    media,
    minimo_de_dois,
    multiplicar,
    percentual_do_total,
    potencia,
    soma_lista,
    somar,
    subtrair,
    valor_absoluto,
)

# Define uma função auxiliar nossa, que não será testada, mas ajudará nos testes.
# O "x: float" e "-> float" são apenas dicas de tipo dizendo que ela recebe e devolve números com vírgula.
def _arredondar_conforme_doc(x: float) -> float:
    # Docstring explicando o que essa nossa função auxiliar faz.
    """Duas casas, meio para cima (regra da docstring)."""
    # Pega o número x, transforma em texto, depois em Decimal exato, trava em duas casas ("0.01"), 
    # arredonda para cima se terminar em 5, e devolve como um float (número quebrado normal).
    return float(Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


# --- somar ---


# Decorador do pytest que diz: "Rode o teste abaixo várias vezes usando esta tabela de dados".
@pytest.mark.parametrize(
    # Nomes das "colunas" da nossa tabela.
    "a,b,esperado",
    [
        # Linha 1 da tabela: 2 + 3 tem que ser 5.
        (2, 3, 5),
        # Linha 2 da tabela: 1.9 + 1.1 tem que ser 3.0.
        (1.9, 1.1, 3.0),
        # Linha 3 da tabela: -2 + 5 tem que ser 3.
        (-2, 5, 3),
    ],
)
# Define a função de teste de soma. O pytest vai preencher o 'a', 'b' e 'esperado' com os dados da tabela.
def test_somar(a, b, esperado):
    # O comando principal: Garante (assert) que o resultado da função somar(a,b) é IGUAL (==) ao esperado.
    assert somar(a, b) == esperado


# Define um teste específico para checar a falha de precisão natural dos computadores.
def test_somar_floats_sem_perder_decimais():
    # Garante que 0.1 + 0.2 dê APROXIMADAMENTE 0.3 (já que o PC calcula como 0.30000000000000004).
    assert somar(0.1, 0.2) == pytest.approx(0.3)


# --- subtrair ---


# Tabela de dados compacta para testar a subtração.
@pytest.mark.parametrize("a,b,esperado", [(10, 3, 7), (0, 5, -5), (-1, -4, 3)])
# Define a função de teste de subtração.
def test_subtrair(a, b, esperado):
    # Garante que subtrair 'b' de 'a' resulte no valor esperado.
    assert subtrair(a, b) == esperado


# --- multiplicar ---


# Tabela de dados para testar a multiplicação (incluindo números negativos e multiplicação por zero).
@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (3, 4, 12),
        (-2, 5, -10),
        (-2, -3, 6),
        (0, 99, 0),
    ],
)
# Define a função de teste de multiplicação.
def test_multiplicar(a, b, esperado):
    # Garante que o produto de 'a' por 'b' seja igual ao valor esperado.
    assert multiplicar(a, b) == esperado


# --- dividir ---


# Tabela de dados para testar divisões felizes (que dão certo).
@pytest.mark.parametrize("a,b,esperado", [(10, 2, 5.0), (-9, 3, -3.0), (7, 2, 3.5)])
# Define a função de teste da divisão bem-sucedida.
def test_dividir_ok(a, b, esperado):
    # Garante que a divisão resulte no valor esperado.
    assert dividir(a, b) == esperado


# Define um teste do "caminho triste" (situação proibida).
def test_dividir_por_zero_levanta():
    # O "with pytest.raises" avisa o pytest: "Fique de olho, a linha de baixo TEM QUE gerar o erro ZeroDivisionError".
    with pytest.raises(ZeroDivisionError):
        # Tenta executar a divisão proibida (1 dividido por 0). Se der erro, o teste passa!
        dividir(1, 0)


# --- media ---


# Teste do caminho triste para a função média.
def test_media_lista_vazia_levanta():
    # Avisa o pytest: "A próxima linha TEM QUE gerar um erro de valor (ValueError)".
    with pytest.raises(ValueError):
        # Tenta calcular a média de uma lista vazia (o que é matematicamente impossível).
        media([])


# Tabela de dados para testar médias que dão certo (passando listas de números).
@pytest.mark.parametrize("valores,esperado", [([42], 42.0), ([10, 20, 30], 20.0), ([1, 2, 3, 4], 2.5)])
# Define a função de teste da média.
def test_media_lista_nao_vazia(valores, esperado):
    # Garante que a média calculada bate com o gabarito.
    assert media(valores) == esperado


# --- percentual_do_total ---


# Tabela de dados para testar o cálculo de porcentagem.
@pytest.mark.parametrize(
    "parte,total,esperado",
    [
        (25, 200, 12.5),
        (1, 4, 25.0),
        (0, 100, 0.0),
    ],
)
# Define o teste de porcentagem.
def test_percentual_do_total_ok(parte, total, esperado):
    # Garante que a porcentagem está correta, usando 'approx' por via das dúvidas, já que lida com decimais.
    assert percentual_do_total(parte, total) == pytest.approx(esperado)


# Teste do caminho triste para porcentagem.
def test_percentual_total_zero_levanta():
    # Avisa o pytest que espera um ValueError.
    with pytest.raises(ValueError):
        # Tenta calcular a porcentagem onde o total é zero (impossível).
        percentual_do_total(10, 0)


# --- potencia ---


# Tabela de dados para testar exponenciação.
@pytest.mark.parametrize("base,exp,esperado", [(2, 10, 1024), (5, 0, 1), (3, 4, 81)])
# Define o teste da potência.
def test_potencia_ok(base, exp, esperado):
    # Garante que a conta de "base elevada ao expoente" bate com o gabarito.
    assert potencia(base, exp) == esperado


# Tabela de dados focada apenas no caminho triste da potência.
@pytest.mark.parametrize("base,exp", [(2, -1), (10, -3)])
# Define o teste para proibir expoentes negativos.
def test_potencia_expoente_negativo_levanta(base, exp):
    # Avisa o pytest que espera um ValueError.
    with pytest.raises(ValueError):
        # Executa a função passando expoentes proibidos pelas regras da calculadora.
        potencia(base, exp)


# --- valor_absoluto ---


# Tabela de dados misturando positivos, negativos, zeros e quebras para testar o valor absoluto.
@pytest.mark.parametrize("x,esperado", [(5, 5), (-5, 5), (0, 0), (-0.5, 0.5)])
# Define o teste de valor absoluto.
def test_valor_absoluto(x, esperado):
    # Garante que números negativos virem positivos e os positivos fiquem iguais, usando approx para segurança.
    assert valor_absoluto(x) == pytest.approx(esperado)


# --- maximo / minimo ---


# Tabela de dados para descobrir qual é o maior número de uma dupla.
@pytest.mark.parametrize("a,b,esperado", [(3, 8, 8), (10, 2, 10), (7, 7, 7)])
# Define o teste da função "máximo".
def test_maximo_de_dois(a, b, esperado):
    # Garante que a função está escolhendo o maior número corretamente.
    assert maximo_de_dois(a, b) == esperado


# Tabela de dados para descobrir qual é o menor número de uma dupla.
@pytest.mark.parametrize("a,b,esperado", [(3, 8, 3), (10, 2, 2), (7, 7, 7)])
# Define o teste da função "mínimo".
def test_minimo_de_dois(a, b, esperado):
    # Garante que a função está escolhendo o menor número corretamente.
    assert minimo_de_dois(a, b) == esperado


# --- arredondar ---


# Tabela contendo APENAS a "coluna" de entrada (x), sem o resultado esperado.
@pytest.mark.parametrize(
    "x",
    [2.345, 1.005, -3.456, 0.333],
)
# Define o teste de arredondamento.
def test_arredondar_duas_casas(x):
    # Garante que o arredondamento da calculadora seja igual (aprox) ao resultado da nossa função gabarito perfeita lá de cima.
    assert arredondar_duas_casas(x) == pytest.approx(_arredondar_conforme_doc(x))


# --- soma_lista ---


# Tabela de dados passando listas vazias, listas com vários itens e listas com um item só.
@pytest.mark.parametrize("valores,esperado", [([], 0), ([1, 2, 3], 6), ([10], 10)])
# Define o teste de soma da lista.
def test_soma_lista(valores, esperado):
    # Garante que a soma de todos os itens dentro da lista bata com o gabarito.
    assert soma_lista(valores) == esperado