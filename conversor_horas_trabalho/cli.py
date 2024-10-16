from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from conversor_horas_trabalho.converte_horas import converte_horas
from conversor_horas_trabalho.converte_horas_semanais import (
    converte_horas_semanais,
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
