![Logo](assets/logo.png){ width="300" .center }
# Conversor Horas Trabalho

O Conversor de horas de trabalho é um CLI responsável por fazer algumas conversões
entre horas para calculo de horas de trabalho.

Temos três comandos disponíveis: `converte-hora`, `converte-hora-semanal` e `total-horas-mes`


---

## Como Usar?

{% include "templates/instalacao.md" %}

### Converte Horas
Você pode chamar o conversor de hora via linha de comando. Por exemplo:
```bash
{{ commands.run }} converte-hora
```
```bash
┏━━━━━━━┓
┃ hora  ┃
┡━━━━━━━┩
│ 12.50 │
└───────┘
```

#### Alteração do horário
O unico parametro do CLI é a hora que deseja converter
Voce pode usar passando um horário contendo ":" ou "." 
Todos os tipos de conversoes possiveis:
* Tipos de Horas: '12:50' ou '12.30' sendo as duas correspondentes. Por exemplo:
```bash
{{ commands.run }} converte-hora 12:40
```
```
┏━━━━━━━┓
┃ hora  ┃
┡━━━━━━━┩
│ 12.65 │
└───────┘
```
Ou no outro formato. Por exemplo:
```bash
{{ commands.run }} converte-hora 12.30
```
```
┏━━━━━━━┓
┃ hora  ┃
┡━━━━━━━┩
│ 12:20 │
└───────┘
```
### Uma tablea mostrando a conversão
![Logo](assets/img/image.png){ width="500" .center }

## Converte horas semanal
Você pode chamar o conversor de hora via linha de comando. Por exemplo:
```bash
{{ commands.run }} converte-hora-semanal
```
```bash
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ total_horas_da_semana ┃ total_horas_extra ┃ total_horas_faltantes ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ 18:00                 │ 00:00             │ 26:00                 │
└───────────────────────┴───────────────────┴───────────────────────┘
```

### Contabilizando as horas com comando
Como você pode chamar o conversor de hora semanal via linha de comando. Por exemplo:
```bash
{{ commands.run }} converte-hora-semanal --help
```
#### Informações sobre o comando converte-hora-semanal
Para você descobrir outras opções você pode usar a flag `--help`
```

 Usage: conversor-hora-trabalho converte-hora-semanal
            [OPTIONS] [HORAS_SEMANA] [FORMATO]

╭─ Arguments ────────────────────────────────────────────────────╮
│   horas_semana      [HORAS_SEMANA]  Tag mais Hora              │
│                                     [default: nm09.00,nm09.00] │
│   formato           [FORMATO]       Formato de retorno com 1   │
│                                     para ":" ou 2 para "."     │
│                                     [default: 1]               │
╰────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                    │
╰────────────────────────────────────────────────────────────────╯
```
#### Tags e Uso
Podemos observar que existem duas tags: `nm (normal)` e `ov (overtime)`
quando indicados que uma hora é normal ela será contabilizada nas horas totais
da semana.
Ja quando definimo que uma hora é overtime ela é contabilizada nas horas extras

O ultimo parametro é o formato como queremos retornar as horas `1 para decimal`
e `2 para real`.

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ total_horas_da_semana ┃ total_horas_extra ┃ total_horas_faltantes ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ 09:00                 │ 09:00             │ 35:00                 │
└───────────────────────┴───────────────────┴───────────────────────┘
```
```bash
{{ commands.run }} converte-hora-semanal nm09.00,ov09.00 2
```

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ total_horas_da_semana ┃ total_horas_extra ┃ total_horas_faltantes ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ 09.00                 │ 09.00             │ 35.00                 │
└───────────────────────┴───────────────────┴───────────────────────┘
```

```bash
{{ commands.run }} converte-hora-semanal nm09.00,nm09.00,nm09.00,nm09.00,nm08.00 1
```

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ total_horas_da_semana ┃ total_horas_extra ┃ total_horas_faltantes ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ 44:00                 │ 00:00             │ 00:00                 │
└───────────────────────┴───────────────────┴───────────────────────┘
```

```bash
{{ commands.run }} converte-hora-semanal nm05.00,ov02.00,nm09.00,nm09.00,nm09.00 1
```

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ total_horas_da_semana ┃ total_horas_extra ┃ total_horas_faltantes ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ 32:00                 │ 02:00             │ 12:00                 │
└───────────────────────┴───────────────────┴───────────────────────┘
```
## Total Horas Mensal
Você pode chamar o total horas mes via linha de comando. Por exemplo:
```bash
{{ commands.run }} total-horas-mes
```
```bash
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ total_de_horas_esperadas_no_mes ┃ total_horas_trabalhadas ┃ total_horas_faltantes ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ 186:00                          │ 176:00                  │ 010:00                │
└─────────────────────────────────┴─────────────────────────┴───────────────────────┘
```

#### Informações sobre o comando total-horas-mes
Para você descobrir outras opções você pode usar a flag `--help`

```
 Usage: conversor-hora-trabalho total-horas-mes [OPTIONS] [HORAS_SEMANA] [ANO]
                                                [MES]

╭─ Arguments ─────────────────────────────────────────────────────────────────────────╮
│   horas_semana      [HORAS_SEMANA]  Horas totais de cada semana seguido de virgula  │
│                                     [default: 44,44,44,44]                          │
│   ano               [ANO]           Digite o Ano que deseja calcular                │
│                                     [default: 2024]                                 │
│   mes               [MES]           Digite o Mes que deseja calcular [default: 09]  │
╰─────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                         │
╰─────────────────────────────────────────────────────────────────────────────────────╯
```
#### Tags e Uso
Podemos observar que existem 3 parametros `horas_semana` que é informado em formato csv
ou seja podemos colocar o total de horas daquela semana seguido de uma virgula, por exemplo,
`10,10,10`, temos o parametro ano onde indicamos o ano e o ultimo para indicar o mês.
Exemplo de Uso:

```bash
{{ commands.run }} total-horas-mes 44,43,45,44 2024 05
```
```bash
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ total_de_horas_esperadas_no_mes ┃ total_horas_trabalhadas ┃ total_horas_faltantes ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ 200:00                          │ 176:00                  │ 024:00                │
└─────────────────────────────────┴─────────────────────────┴───────────────────────┘
```

### Mais Informações sobre o CLI
Para você descobrir outras opções você pode usar a flag `--help`
```
 Usage: conversor-hora-trabalho [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.      │
│ --show-completion             Show completion for the current shell, to copy │
│                               it or customize the installation.              │
│ --help                        Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ converte-hora                                                                │
│ converte-hora-semanal                                                        │
│ total-horas-mes                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
```
