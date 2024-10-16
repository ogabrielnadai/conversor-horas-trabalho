from pytest import mark, raises

from conversor_horas_trabalho.converte_horas_semanais import (
    converte_horas_semanais,
)


def test_converte_horas_semanais_deve_retornar_as_horas_correspondentes():
    formato = 1
    lista_semana = [
        ['nm', '09.00'],
        ['nm', '09.00'],
        ['nm', '09.00'],
        ['nm', '09.00'],
        ['nm', '07.00'],
    ]
    esperado = {
        'total_horas_da_semana': '43:00',
        'total_horas_extra': '00:00',
        'total_horas_faltantes': '01:00',
    }

    resultado = converte_horas_semanais(lista_semana, formato)

    assert esperado == resultado


def test_converte_horas_semanais_deve_retornar_as_horas_extra():
    formato = 1
    lista_semana = [
        ['nm', '04.30'],
        ['nm', '09.00'],
        ['ov', '02.00'],
        ['nm', '09.00'],
        ['nm', '09.00'],
        ['nm', '08.00'],
    ]
    esperado = {
        'total_horas_da_semana': '39:15',
        'total_horas_extra': '02:00',
        'total_horas_faltantes': '04:45',
    }

    resultado = converte_horas_semanais(lista_semana, formato)

    assert esperado == resultado


def test_converte_horas_semanais_deve_retornar_em_formato_dois_pontos():
    formato = 1
    lista_semana = [
        ['nm', '09.00'],
        ['nm', '05.00'],
    ]
    esperado = {
        'total_horas_da_semana': '14:00',
        'total_horas_extra': '00:00',
        'total_horas_faltantes': '30:00',
    }

    resultado = converte_horas_semanais(lista_semana, formato)

    assert esperado == resultado


def test_converte_horas_semanais_deve_retornar_em_formato_um_ponto():
    formato = 2
    lista_semana = [
        ['nm', '09.00'],
        ['nm', '05.00'],
    ]
    esperado = {
        'total_horas_da_semana': '14.00',
        'total_horas_extra': '00.00',
        'total_horas_faltantes': '30.00',
    }

    resultado = converte_horas_semanais(lista_semana, formato)

    assert esperado == resultado


@mark.parametrize(
    'lista_semana,formato,esperado',
    [([['nm', '04.30']], 1, '04:15'), ([['nm', '02.10']], 2, '02.10')],
)
def test_converte_horas_semanais_deve_retornar_total_hora_semana_correto(
    lista_semana, formato, esperado
):
    resultado = converte_horas_semanais(lista_semana, formato)

    assert esperado in resultado['total_horas_da_semana']


@mark.parametrize(
    'lista_semana,formato,esperado',
    [([['ov', '04.30']], 1, '04:15'), ([['ov', '02.10']], 2, '02.10')],
)
def test_converte_horas_semanais_deve_retornar_total_hora_extra_correto(
    lista_semana, formato, esperado
):
    resultado = converte_horas_semanais(lista_semana, formato)

    assert esperado in resultado['total_horas_extra']


@mark.parametrize(
    'lista_semana,formato,esperado',
    [([['ov', '04.30']], 1, '44:00'), ([['nm', '02.10']], 2, '41.90')],
)
def test_converte_horas_semanais_deve_retornar_total_hora_faltantes_correto(
    lista_semana, formato, esperado
):
    resultado = converte_horas_semanais(lista_semana, formato)

    assert esperado in resultado['total_horas_faltantes']


def test_converte_horas_semanais_deve_retornar_erro_formato_incorreto():
    formato = 3
    lista_semana = [
        ['nm', '09.00'],
        ['nm', '05.00'],
    ]
    mensagem_de_erro = 'Não existe esse tipo de formato 3'

    with raises(KeyError) as error:
        converte_horas_semanais(lista_semana, formato)

    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(
    'lista_semana,formato,mensagem_de_erro',
    [
        (
            [['ov', '04;30']],
            1,
            'Não foi possivel extrair a hora corretamente 04;30',
        ),
        (
            [['nm', '04:30']],
            2,
            'Não foi possivel extrair a hora corretamente 04:30',
        ),
    ],
)
def test_converte_horas_semanais_deve_retornar_erro_hora_formato_incorreto(
    lista_semana, formato, mensagem_de_erro
):
    with raises(ValueError) as error:
        converte_horas_semanais(lista_semana, formato)

    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(
    'lista_semana,formato,mensagem_de_erro',
    [
        (
            [['mm', '04.30']],
            1,
            'Não existe esse tipo de lancamento mm',
        ),
        (
            [['os', '12.30']],
            2,
            'Não existe esse tipo de lancamento os',
        ),
    ],
)
def test_converte_horas_semanais_deve_retornar_erro_lancamento_incorreto(
    lista_semana, formato, mensagem_de_erro
):
    with raises(KeyError) as error:
        converte_horas_semanais(lista_semana, formato)

    assert mensagem_de_erro == error.value.args[0]


def test_converte_horas_semanais_deve_retornar_mais_de_44_horas_formato2():
    formato = 2
    lista_semana = [
        ['nm', '09.00'],
        ['nm', '09.00'],
        ['nm', '09.00'],
        ['nm', '09.00'],
        ['nm', '09.00'],
        ['nm', '09.00'],
    ]
    esperado = {
        'total_horas_da_semana': '54.00',
        'total_horas_extra': '00.00',
        'total_horas_faltantes': '00.00',
    }

    resultado = converte_horas_semanais(lista_semana, formato)

    assert esperado == resultado


def test_converte_horas_semanais_deve_retornar_mais_de_44_horas_formato_1():
    formato = 1
    lista_semana = [
        ['nm', '09.00'],
        ['nm', '09.00'],
        ['nm', '09.00'],
        ['nm', '09.00'],
        ['nm', '09.00'],
        ['nm', '09.00'],
    ]
    esperado = {
        'total_horas_da_semana': '54:00',
        'total_horas_extra': '00:00',
        'total_horas_faltantes': '00:00',
    }

    resultado = converte_horas_semanais(lista_semana, formato)

    assert esperado == resultado
