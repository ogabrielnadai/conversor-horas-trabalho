def converte_horas(hr_recebida: str) -> dict[str, list[str]] | None:
    """
    Recebe uma Hora e modifica para outro sistema

    Args:
        hr_recebida: hr_recebida no formato ex: 12:30 ou 12.50

    Examples:
        >>> converte_horas('12:30')
        {'hora': ['12.50']}

        >>> converte_horas('12.50')
        {'hora': ['12:30']}

    Returns:
        Um dicionario com a hora convertida

    Raises:
        ValueError: Caso a hora nao seja uma hora válida

    """
    temp = []
    if len(hr_recebida) < 5:
        raise ValueError(
            'Sua hora deve conter pelo menos 5 caracteres, EX: 12:30 ou 12.50'
        )

    if ':' in hr_recebida:
        hora_int = int(hr_recebida[0:2])
        minutos_int = int(hr_recebida[3:5])
        minutos_int_calc = int(minutos_int // 0.6 * 1)
        minutos_int_show = round(minutos_int_calc / 5) * 5
        temp.append(f'{hora_int}.{minutos_int_show:02d}')
    elif '.' in hr_recebida:
        hora_total_float = float(hr_recebida)
        hora_int = int(hora_total_float)
        hora_calc = hora_total_float - hora_int
        minutos_int_calc = int(hora_calc * 60)
        minutos_int_show = round(minutos_int_calc / 5) * 5
        temp.append(f'{hora_int}:{minutos_int_show:02d}')
    else:
        raise ValueError(f'Hora invalida, tente neste formato 12:30 ou 12.50')

    return {'hora': temp}
