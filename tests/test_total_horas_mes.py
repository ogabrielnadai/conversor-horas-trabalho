from pytest import mark, raises

from conversor_horas_trabalho.total_horas_mes import total_horas_mes


def test_total_horas_mes_deve_funcionar():
    horas = [44, 44, 44, 44, 30]
    ano = 2024
    mes = 10

    result = total_horas_mes(horas, ano, mes)

    assert result


def test_total_horas_mes_deve_retornar_horas_totais_mes():
    horas = [44, 44, 44, 44, 30]
    ano = 2024
    mes = 10
    esperado = '206:00'
    result = total_horas_mes(horas, ano, mes)

    assert esperado in result['total_de_horas_esperadas_no_mes']


def test_total_horas_mes_deve_retornar_horas_totais_trabalhadas():
    horas = [44, 44, 44, 44, 30]
    ano = 2024
    mes = 10
    esperado = '206:00'
    result = total_horas_mes(horas, ano, mes)

    assert esperado in result['total_horas_trabalhadas']


def test_total_horas_mes_deve_retornar_horas_totais_faltantes():
    horas = [44, 44, 44, 44]
    ano = 2024
    mes = 10
    esperado = '030:00'
    result = total_horas_mes(horas, ano, mes)

    assert esperado in result['total_horas_faltantes']


def test_total_horas_mes_deve_retornar_horas_totais_trabalhadas_maior_total():
    horas = [44, 44, 44, 44, 44, 44]
    ano = 2024
    mes = 11
    esperado = '000:00'
    result = total_horas_mes(horas, ano, mes)

    assert esperado in result['total_horas_faltantes']


def test_total_horas_mes_deve_retornar_horas_totais_trabalhadas_maior_total():
    horas = [44, 44, 44, 44, 44, 44]
    ano = 2024
    mes = 10
    esperado = '000:00'
    result = total_horas_mes(horas, ano, mes)

    assert esperado in result['total_horas_faltantes']


def test_total_horas_mes_deve_retornar_erro_campo_horas_str():
    horas = [44, 44, 44, 'aa']
    ano = 2024
    mes = 10

    mensagem_de_erro = 'Erro ao converter o valor de horas indicado aa'

    with raises(ValueError) as error:
        total_horas_mes(horas, ano, mes)

    assert mensagem_de_erro == error.value.args[0]


def test_total_horas_mes_deve_retornar_erro_campo_ano_ou_mes_errados():
    horas = [44, 44, 44, 44]
    ano = 2024
    mes = 13

    mensagem_de_erro = 'Mes 13 ou Ano 2024 indicados errado'

    with raises(ValueError) as error:
        total_horas_mes(horas, ano, mes)

    assert mensagem_de_erro == error.value.args[0]
