import calendar
import datetime as dt

from conversor_horas_trabalho.converte_horas import converte_horas


def total_horas_mes(
    lista_horas: list[int], ano: int, mes: int
) -> dict[str, list[str]]:
    """
    Recebe um Dicionario de horas e calcula a quantidade para fechar o mes

    Args:
        lista_horas: Lista contendo o lançamento das horas
        ano: Ano que deseja calcular
        mes: Mes que deseja calcular

    Examples:
        >>> total_horas_mes([44,44,44,44,30], 2024, 10)
        {'total_de_horas_esperadas_no_mes': '206:00', 'total_horas_trabalhadas': '206:00', 'total_horas_faltantes': '000:00'}

        >>> total_horas_mes([44,44,44,44], 2024, 9)
        {'total_de_horas_esperadas_no_mes': '186:00', 'total_horas_trabalhadas': '176:00', 'total_horas_faltantes': '010:00'}

    Returns:
        Um Dicionario contendo a totalização das horas

    Raises:
        ValueError: Caso valor passado não seja o esperado
    """
    retorna = {}
    qnt_tot_hr_seg = 0
    qnt_tot_hr_falt_diff_seg = 0
    total_de_horas_esperadas_no_mes = 0
    for hr in lista_horas:
        try:
            qnt_horas_seg = hr * 3600
            qnt_tot_hr_seg = qnt_tot_hr_seg + qnt_horas_seg
        except:
            raise ValueError(
                f'Erro ao converter o valor de horas indicado {hr}'
            )

    maximo_horas_mes = _maximo_horas_trabalhadas(ano, mes)
    maximo_horas_mes_seg = maximo_horas_mes * 3600

    if qnt_tot_hr_seg >= maximo_horas_mes_seg:
        total_horas_faltantes = '000:00'
    else:
        qnt_tot_hr_falt_diff_seg = maximo_horas_mes_seg - qnt_tot_hr_seg
        total_horas_faltantes = _segundos_para_hhh_mm(qnt_tot_hr_falt_diff_seg)

    total_horas_trabalhadas = _segundos_para_hhh_mm(qnt_tot_hr_seg)
    total_de_horas_esperadas_no_mes = _segundos_para_hhh_mm(
        maximo_horas_mes_seg
    )

    retorna = {
        'total_de_horas_esperadas_no_mes': total_de_horas_esperadas_no_mes,
        'total_horas_trabalhadas': total_horas_trabalhadas,
        'total_horas_faltantes': total_horas_faltantes,
    }
    return retorna


def _segundos_para_hhh_mm(segundos: int) -> str:
    """
    Transforma segundos no formato 000:00
    """
    hr = segundos // 3600
    minuto = (segundos % 3600) // 60

    hora_formatada = '{:03}:{:02}'.format(int(hr), int(minuto))

    return hora_formatada


def _maximo_horas_trabalhadas(ano: int, mes: int) -> int:
    try:
        dias_no_mes = calendar.monthrange(ano, mes)[1]
    except:
        raise ValueError(f'Mes {mes} ou Ano {ano} indicados errado')

    horas_trabalhadas_por_dia = {0: 10, 1: 10, 2: 10, 3: 10, 4: 4}
    total_horas_trabalhadas = 0

    primeiro_dia_semana = calendar.monthrange(ano, mes)[0]

    for dia in range(1, dias_no_mes + 1):
        dia_semana = (primeiro_dia_semana + (dia - 1)) % 7

        if dia_semana in horas_trabalhadas_por_dia:
            total_horas_trabalhadas += horas_trabalhadas_por_dia[dia_semana]

    return total_horas_trabalhadas
