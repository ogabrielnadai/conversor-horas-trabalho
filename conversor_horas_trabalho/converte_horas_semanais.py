from conversor_horas_trabalho.converte_horas import converte_horas


def converte_horas_semanais(
    lista_horas: dict[str, list[str]], formato: int
) -> dict[str, list[str]]:
    """
    Recebe um Dicionario de horas e calcula a quantidade para fechar a semana

    Args:
        lista_horas: Dicionario contendo o lançamento das horas
        formato: Inteiro que define qual formato de saida dos horarios

    Examples:
        >>> converte_horas_semanais([['nm', '09.00']], 1)
        {'total_horas_da_semana': '09:00', 'total_horas_extra': '00:00', 'total_horas_faltantes': '35:00'}

        >>> converte_horas_semanais([['nm', '09.00'],['nm', '09.00']], 1)
        {'total_horas_da_semana': '18:00', 'total_horas_extra': '00:00', 'total_horas_faltantes': '26:00'}

        >>> converte_horas_semanais([['nm', '09.00'],['ov', '02.00']], 1)
        {'total_horas_da_semana': '09:00', 'total_horas_extra': '02:00', 'total_horas_faltantes': '35:00'}

        >>> converte_horas_semanais([['nm', '09.00']], 2)
        {'total_horas_da_semana': '09.00', 'total_horas_extra': '00.00', 'total_horas_faltantes': '35.00'}

        >>> converte_horas_semanais([['nm', '09.00'],['ov', '02.00']], 2)
        {'total_horas_da_semana': '09.00', 'total_horas_extra': '02.00', 'total_horas_faltantes': '35.00'}

    Returns:
        Um Dicionario contendo a totalização das horas

    Raises:
        ValueError: Caso a hora nao seja uma hora válida
        KeyError: Não foi encontrado o tipo de lançamento ou formato informado

    """
    retorna = {}
    qnt_tot_hr_seg = 0
    qnt_tot_hr_ext_seg = 0
    qnt_tot_hr_falt_diff_seg = 0
    for lancamento in lista_horas:
        tipo_lancamento = lancamento[0]
        try:
            qnt_hr_result = converte_horas(lancamento[1])
            hr, minutos = map(int, qnt_hr_result['hora'][0].split(':'))
        except ValueError:
            raise ValueError(
                f'Não foi possivel extrair a hora corretamente {lancamento[1]}'
            )
        qnt_horas_seg = hr * 3600 + minutos * 60

        if tipo_lancamento == 'nm':
            qnt_tot_hr_seg = qnt_tot_hr_seg + qnt_horas_seg
        elif tipo_lancamento == 'ov':
            qnt_tot_hr_ext_seg = qnt_tot_hr_ext_seg + qnt_horas_seg
        else:
            raise KeyError(
                f'Não existe esse tipo de lancamento {tipo_lancamento}'
            )
    if qnt_tot_hr_seg > 158400:
        total_horas_faltantes = '00:00'
    else:
        qnt_tot_hr_falt_diff_seg = 158400 - qnt_tot_hr_seg
        total_horas_faltantes = _segundos_para_hh_mm(qnt_tot_hr_falt_diff_seg)
    total_horas_da_semana = _segundos_para_hh_mm(qnt_tot_hr_seg)
    total_horas_extra = _segundos_para_hh_mm(qnt_tot_hr_ext_seg)
    if formato == 2:
        total_horas_da_semana = converte_horas(total_horas_da_semana)['hora'][
            0
        ]
        total_horas_extra = converte_horas(total_horas_extra)['hora'][0]
        total_horas_faltantes = converte_horas(total_horas_faltantes)['hora'][
            0
        ]
    elif formato == 1:
        pass
    else:
        raise KeyError(f'Não existe esse tipo de formato {formato}')

    retorna = {
        'total_horas_da_semana': total_horas_da_semana,
        'total_horas_extra': total_horas_extra,
        'total_horas_faltantes': total_horas_faltantes,
    }

    return retorna


def _segundos_para_hh_mm(segundos: int) -> str:
    """
    Transforma segundos no formato 00:00
    """
    hr = segundos // 3600
    minuto = (segundos % 3600) // 60

    hora_formatada = '{:02}:{:02}'.format(int(hr), int(minuto))

    return hora_formatada
