from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from conversor_horas_trabalho.converte_horas import converte_horas

console = Console()
app = Typer()


@app.command()
def converte_hora(
    hora: str=Argument('12:30', help='Hora em formato 12:30 ou 12.50')
):
    table = Table()
    hora_convertida = converte_horas(hora)
    for hr in hora_convertida:
        table.add_column(hr)
        table.add_row(hora_convertida['hora'][0])

    console.print(table)
