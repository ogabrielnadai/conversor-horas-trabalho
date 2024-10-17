from pytest import mark
from typer.testing import CliRunner

from conversor_horas_trabalho.cli import app

runner = CliRunner()


def test_converte_hora_cli_deve_retornar_zero_ao_stdout():
    result = runner.invoke(app, ['converte-hora'])
    assert result.exit_code == 0


def test_converte_hora_cli_deve_conter_as_horas_na_reposta():
    hora = '12.50'
    result = runner.invoke(app, ['converte-hora'])
    assert hora in result.stdout


@mark.parametrize('hora', ['12:30'])
def test_converte_hora_cli_deve_conter_as_horas_com_um_ponto(hora):
    result = runner.invoke(app, ['converte-hora', '12.50'])
    assert hora in result.stdout


@mark.parametrize('hora', ['12.50'])
def test_converte_hora_cli_deve_conter_as_horas_com_dois_pontos(hora):
    result = runner.invoke(app, ['converte-hora', '12:30'])
    assert hora in result.stdout


def test_converte_hora_semanal_cli_deve_retornar_zero_ao_stdout():
    result = runner.invoke(app, ['converte-hora-semanal'])
    assert result.exit_code == 0


def test_converte_hora_semanal_cli_deve_conter_as_horas_na_reposta():
    hora = '18:00'
    result = runner.invoke(app, ['converte-hora-semanal'])
    assert hora in result.stdout


def test_total_horas_mes_cli_deve_retornar_zero_ao_stdout():
    result = runner.invoke(app, ['total-horas-mes'])
    assert result.exit_code == 0


def test_total_horas_mes_cli_deve_conter_as_horas_na_resposta():
    hora = '186:00'
    hora_trabalhada = '176:00'
    hora_faltantes = '010:00'
    result = runner.invoke(app, ['total-horas-mes'])
    assert hora in result.stdout
    assert hora_trabalhada in result.stdout
    assert hora_faltantes in result.stdout
