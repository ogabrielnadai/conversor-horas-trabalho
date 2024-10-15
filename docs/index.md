![Logo](assets/logo.png){ width="300" .center }
# Conversor Horas Trabalho
---

## Como Usar?

Você pode chamar o conversor de hora via linha de comando. Por exemplo:
```bash
poetry run converte_hora
```
```bash
┏━━━━━━━┓
┃ hora  ┃
┡━━━━━━━┩
│ 12.50 │
└───────┘
```

### Alteração do horário
O unico parametro do CLI é a hora que deseja converter
Voce pode usar passando um horário contendo ":" ou "." 
Todos os tipos de conversoes possiveis:
* Tipos de Horas: '12:50' ou '12.30' sendo as duas correspondentes. Por exemplo:
```bash
poetry run converte_hora 12:40
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
poetry run converte_hora 12.30
```
```
┏━━━━━━━┓
┃ hora  ┃
┡━━━━━━━┩
│ 12:20 │
└───────┘
```

## Mais Informações sobre o CLI
Para você descobrir outras opções você pode usar a flag `--help`
```
 Usage: converte_hora [OPTIONS] [HORA]

╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   hora      [HORA]  Hora em formato 12:30 ou 12.50 [default: 12:30]                                                        │  ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```