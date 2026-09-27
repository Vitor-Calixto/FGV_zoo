# Sistema de Controle de Animais em um Zoológico

Projeto Final de POO — aplicação em Python para controlar cadastro de animais,
tratadores, recintos e registro de atividades (alimentação, tratamento, limpeza
e banho de sol), com persistência em arquivos CSV.

## Objetivo

Demonstrar na prática os conceitos de Programação Orientada a Objetos:
classes, objetos, construtores (`__init__`), encapsulamento, herança,
polimorfismo e responsabilidade única, aplicados a um problema real.

## Como executar

Pré-requisito: Python 3.8+ instalado.

```bash
python main.py
```

O sistema abre o menu interativo:

```
===== SISTEMA DE ZOOLÓGICO =====
1 - Cadastrar animal
2 - Listar animais
3 - Cadastrar tratador
4 - Listar tratadores
5 - Cadastrar recinto
6 - Listar recintos
7 - Alimentar animal
8 - Tratar animal
9 - Limpar recinto
10 - Registrar banho de sol
11 - Relatório de atividades
0 - Sair
```

## Estrutura do projeto

```
.
├── main.py                 # Menu e interação com o usuário
├── modelos/
│   ├── animal.py           # Classe base Animal
│   ├── mamifero.py         # Herda de Animal (tipo_pelagem)
│   ├── ave.py              # Herda de Animal (pode_voar)
│   ├── reptil.py           # Herda de Animal (venenoso)
│   ├── tratador.py         # Funcionário que cuida dos animais
│   ├── recinto.py          # Local onde os animais ficam
│   ├── atividade.py        # Ação realizada (alimentação, etc.)
│   └── administrador.py    # Relatórios e consultas
├── servicos/
│   ├── animal_service.py   # Validações e cadastro de animais
│   ├── tratador_service.py # Validações e cadastro de tratadores
│   ├── recinto_service.py  # Validações, cadastro e limpeza
│   └── atividade_service.py# Registro das 4 atividades
├── repositorios/
│   ├── animal_repository.py
│   ├── tratador_repository.py
│   ├── recinto_repository.py
│   ├── atividade_repository.py
│   └── base_repository.py  # Helpers CSV (criar, ler, gravar, próximo ID)
├── dados/
│   ├── animais.csv
│   ├── tratadores.csv
│   ├── recintos.csv
│   └── atividades.csv
└── README.md
```

Responsabilidades:
- `modelos/` — dados + comportamentos (ex.: `alimentar()`, `limpar()`).
- `repositorios/` — leitura/gravação em CSV com cabeçalho.
- `servicos/` — regras de negócio (animal/tratador/recinto precisam existir,
  campos obrigatórios, toda atividade gera registro).
- `main.py` — apenas menu e entrada/saída.

## Classes principais

| Classe | Responsabilidade | Herança/Polimorfismo |
|---|---|---|
| `Animal` | id, nome, espécie, idade, alimentação, recinto, saúde; `alimentar()`, `tratar()`, `tomar_banho_de_sol()`, `exibir_dados()` | Classe base |
| `Mamifero` | + `tipo_pelagem` | Herda `Animal`, sobrescreve `alimentar()` e `tratar()` |
| `Ave` | + `pode_voar` | Herda `Animal`, sobrescreve `alimentar()` e `tratar()` |
| `Reptil` | + `venenoso` | Herda `Animal`, sobrescreve `alimentar()` e `tratar()` |
| `Tratador` | id, nome, turno, especialidade; `alimentar_animal()`, `tratar_animal()`, `limpar_recinto()` | — |
| `Recinto` | id, nome, tipo, capacidade, localização, limpeza; `limpar()`, `verificar_disponibilidade()` | — |
| `Atividade` | id, tipo, data, hora, animal, tratador, descrição; `registrar()` | — |
| `Administrador` | `gerar_relatorio_atividades()`, `consultar_atividades_por_tratador()`, `consultar_total_atividades()` | — |

Herança: `Mamifero`, `Ave` e `Reptil` herdam de `Animal`.
Polimorfismo: cada tipo responde a `alimentar()`/`tratar()` de forma específica
(ex.: réptil menciona manejo com pinça/EPIs, ave menciona comedouro elevado).

## Persistência em CSV

Arquivos em `dados/` com cabeçalho, criados automaticamente se não existirem:

- `animais.csv`: `id_animal,nome,especie,idade,tipo_alimentacao,recinto,status_saude,tipo,extra`
- `tratadores.csv`: `id_tratador,nome,turno,especialidade,animais_responsaveis`
- `recintos.csv`: `id_recinto,nome,tipo,capacidade,localizacao,status_limpeza`
- `atividades.csv`: `id_atividade,tipo_atividade,data,hora,animal,tratador,descricao`

IDs são gerados automaticamente (maior ID + 1). Os dados permanecem salvos
após encerrar a aplicação.

## Regras de negócio

- Animal precisa existir para ser alimentado/tratado ou tomar banho de sol.
- Tratador precisa existir para executar qualquer atividade.
- Recinto precisa existir para ser limpo (limpeza atualiza o status para "Limpo").
- Toda atividade gera um registro em `atividades.csv`.
- Campos obrigatórios são validados; opção inválida não encerra o sistema.

## Tratamento de exceções

- `ValueError` em conversão numérica (idade, capacidade, opção do menu).
- `LookupError` quando animal/tratador/recinto não é encontrado.
- `FileNotFoundError`/`OSError` na leitura/gravação (arquivo é recriado com cabeçalho).
- Laço principal com `try/except` genérico para nunca encerrar inesperadamente.

## Exemplo de uso

1. Cadastre um recinto (opção 5), um tratador (opção 3) e um animal (opção 1).
2. Registre uma alimentação (opção 7) informando animal + tratador.
3. Veja o relatório (opção 11): total, agrupado por tipo/animal/tratador.

## Para apresentação

- Problema resolvido: controle de cuidados diários e histórico do zoológico.
- Herança: `Animal` → `Mamifero`/`Ave`/`Reptil`.
- Polimorfismo: `alimentar()` e `tratar()` sobrescritos.
- Dados: CSVs com cabeçalho em `dados/`, via camada `repositorios/`.
- Menu: `main.py` com 12 opções (0–11) e validações.
