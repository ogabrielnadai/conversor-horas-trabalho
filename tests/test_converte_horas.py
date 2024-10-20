from pytest import mark, raises

from conversor_horas_trabalho.converte_horas import converte_horas


def test_converte_horas_deve_funcionar_com_horas_dois_pontos():
    horas = '12:30'

    result = converte_horas(horas)

    assert result


def test_converte_horas_deve_funcionar_com_horas_um_ponto():
    horas = '12.50'

    result = converte_horas(horas)

    assert result


def test_converte_horas_deve_retornar_erro_dizendo_hora_invalida():
    horas = '12;30'

    mensagem_de_erro = 'Hora invalida, tente neste formato 12:30 ou 12.50'

    with raises(ValueError) as error:
        converte_horas(horas)

    assert mensagem_de_erro == error.value.args[0]


def test_converte_horas_deve_retornar_erro_dizendo_horas_menos_5_characteres():
    horas = '12:3'

    mensagem_de_erro = (
        'Sua hora deve conter pelo menos 5 caracteres, EX: 12:30 ou 12.50'
    )

    with raises(ValueError) as error:
        converte_horas(horas)

    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(
    'horas,esperado',
    [('12:05', '12.10'), ('12:10', '12.15'), ('12:60', '13.00')],
)
def test_converte_horas_deve_retornar_horas_convertidas_um_ponto_correto(
    horas, esperado
):
    # Agir
    result = converte_horas(horas)
    assert result['hora'][0] == esperado


@mark.parametrize(
    'horas,esperado',
    [('03.10', '03:05'), ('12.20', '12:10'), ('12.99', '13:00')],
)
def test_converte_horas_deve_retornar_horas_convertidas_dois_pontos_correto(
    horas, esperado
):
    # Agir
    result = converte_horas(horas)
    assert result['hora'][0] == esperado
