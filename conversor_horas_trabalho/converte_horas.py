def converte_horas(horas: str) -> dict[str, list[str]]:
    """
    Recebe uma Hora e modifica para outro sistema

    Args:
        horas: Horas no formato ex: 12:30 ou 12.50

    Examples:
        >>> converte_horas('12:30')
        {'hora': ['12.50']}

        >>> converte_horas('12.50')
        {'hora': ['12.30']}

    Returns:
        Um dicionario com a hora convertida    
    """
    temp = []
    if ':' in horas:
        hora = horas[0:2]
        minutos = horas[3:2]
        temp.append('12.50')

    if '.' in horas:
        hora = horas[0:2]
        minutos = horas[3:2]
        temp.append('12.30')

    return {'hora': temp}
