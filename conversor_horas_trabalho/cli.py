from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from conversor_horas_trabalho.converte_horas import converte_horas
from conversor_horas_trabalho.converte_horas_semanais import (
    converte_horas_semanais,
)
from conversor_horas_trabalho.total_horas_mes import (
    total_horas_mes as _total_horas_mes,
)

console = Console()
app = Typer()


@app.command()
def converte_hora(
    hora: str = Argument('12:30', help='Hora em formato 12:30 ou 12.50')
):
    table = Table()
    hora_convertida = converte_horas(hora)
    for hr in hora_convertida:
        table.add_column(hr)
        table.add_row(hora_convertida['hora'][0])

    console.print(table)


@app.command()
def converte_hora_semanal(
    horas_semana: str = Argument('nm09.00,nm09.00', help='Tag mais Hora'),
    formato: int = Argument(
        '1', help='Formato de retorno com 1 para ":" ou 2 para "."'
    ),
):
    table = Table()
    lista_semana = []
    lista_semana_split = horas_semana.split(',')
    for hrstr in lista_semana_split:
        prefix = hrstr[:2]
        hr = hrstr[2:]
        lista_semana.append([prefix, hr])

    total_horas = converte_horas_semanais(lista_semana, formato)

    table.add_column('total_horas_da_semana')
    table.add_column('total_horas_extra')
    table.add_column('total_horas_faltantes')
    table.add_row(
        total_horas['total_horas_da_semana'],
        total_horas['total_horas_extra'],
        total_horas['total_horas_faltantes'],
    )

    console.print(table)


@app.command()
def total_horas_mes(
    horas_semana: str = Argument(
        '44,44,44,44', help='Horas totais de cada semana seguido de virgula'
    ),
    ano: int = Argument('2024', help='Digite o Ano que deseja calcular'),
    mes: int = Argument('09', help='Digite o Mes que deseja calcular'),
):
    table = Table()
    total_horas_mes = []
    total_horas_mes_split = horas_semana.split(',')
    for hr in enumerate(total_horas_mes_split):
        total_horas_mes_split[hr[0]] = int(hr[1])

    total_horas = _total_horas_mes(total_horas_mes_split, ano, mes)

    table.add_column('total_de_horas_esperadas_no_mes')
    table.add_column('total_horas_trabalhadas')
    table.add_column('total_horas_faltantes')
    table.add_row(
        total_horas['total_de_horas_esperadas_no_mes'],
        total_horas['total_horas_trabalhadas'],
        total_horas['total_horas_faltantes'],
    )

    console.print(table)
