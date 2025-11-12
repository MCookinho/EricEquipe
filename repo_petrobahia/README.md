# PetroBahia S.A.

A **PetroBahia S.A.** é uma empresa fictícia do setor de óleo e gás. Seu sistema interno calcula preços de combustíveis, valida clientes e gera relatórios. 
O código está **mal estruturado** e **difícil de manter**. O objetivo é **refatorar** aplicando **PEP8**, **Clean Code** e **princípios SOLID** (SRP e OCP).

## Objetivos
- Melhorar legibilidade e clareza do código
- Extrair funções e classes coesas
- Eliminar duplicações e efeitos colaterais
- Melhorar nomes e modularidade

## Estrutura
```
src/
├── main.py
└── legacy/
    ├── clientes.py
    ├── pedido_service.py
    └── preco_calculadora.py
```

## Instruções
1. Leia o código legado.
2. Liste os problemas encontrados.
3. Refatore sem mudar o comportamento principal.
4. Documente suas **decisões de design** neste README.

---

## DECISÕES DE DESIGN
Etapas ideais de refatoração
1️⃣ Organizar a estrutura do projeto

Primeiro, cria uma estrutura limpa e sem ambiguidade de import:
```
seu-repositorio/
│
├── data/
│   └── clientes.txt             # arquivos de dados ficam fora do código
│
├── src/
│   ├── main.py
│   ├── __init__.py
│   ├── services/                # novo nome para “legacy”
│   │   ├── __init__.py
│   │   ├── clientes_service.py
│   │   ├── pedido_service.py
│   │   └── preco_service.py
│   └── utils/
│       └── file_utils.py        # funções genéricas de leitura/escrita
│
└── tests/
    └── test_pedido_service.py   # depois faremos testes automatizados
```

🔄 Por quê:

“legacy” sugere código velho, e queremos evoluir.

“services” representa bem as regras de negócio.

“data/” guarda os dados, deixando src/ limpo.

            


| Antes (`clientes.py`)              | Agora (`clientes_service.py`)        |
| ---------------------------------- | ------------------------------------ |
| Função solta `cadastrar_cliente()` | Classe organizada `ClienteService`   |
| Prints misturados com lógica       | Prints só pra logar (controlados)    |
| Regex inline e duplicada           | Constante `REG_EMAIL` compilada      |
| Arquivo aberto manualmente         | Uso de `Path.open()` com contexto    |
| Difícil testar                     | Fácil de testar por métodos isolados |


| Antes(`pedido_service.py`)            | Agora(`pedido_service.py`)                                       |
| ------------------------------------- | ---------------------------------------------------------------- |
| `if/else` aninhados e difíceis de ler | Métodos separados por tipo (`_calc_diesel`, `_calc_gasolina`...) |
| Prints misturados com lógica          | Saídas controladas, fáceis de substituir por `logging`           |
| Dicionário global fixo                | Pode ser injetado via construtor (`bases`)                       |
| Sem reaproveitamento ou teste isolado | Cada método pode ser testado separadamente                       |


O código atual funciona, mas mistura lógica de negócio, prints de debug, e regras específicas para cada produto tudo no mesmo lugar — o que dificulta manutenção e testes.

| Antes(`preco_calculadora.py`)         | Agora(`preco_service`)                                           |
| ------------------------------------- | ---------------------------------------------------------------- |
| `if/else` aninhados e difíceis de ler | Métodos separados por tipo (`_calc_diesel`, `_calc_gasolina`...) |
| Prints misturados com lógica          | Saídas controladas, fáceis de substituir por `logging`           |
| Dicionário global fixo                | Pode ser injetado via construtor (`bases`)                       |
| Sem reaproveitamento ou teste isolado | Cada método pode ser testado separadamente                       |

| Antes                                                | Agora(`file_utils.py`)                          |
| ---------------------------------------------------- | ----------------------------------------------- |
| Cada módulo abria e fechava arquivos manualmente     | Um único ponto de leitura/escrita (`FileUtils`) |
| Código duplicado (`open()`, `close()`, `try/except`) | Centralização e reutilização segura             |
| Dificuldade para testar sem gravar de verdade        | Facilmente mockável em testes                   |
| Prints e erros silenciosos                           | Comportamento previsível e controlável          |

Vamos então atualizar o clientes_service.py para usar o novo utilitário FileUtils, deixando o código mais limpo, desacoplado e pronto para testes.

| Antes(`clientes_service.py`)      | Agora(`clientes_service.py`)            |
| --------------------------------- | --------------------------------------- |
| Usava `open()` diretamente        | Usa `FileUtils.append_line()`           |
| Repetição de lógica de gravação   | Código mais limpo e reutilizável        |
| Difícil testar gravação em disco  | `FileUtils` pode ser mockado nos testes |
| Tratamento manual de erros de I/O | Centralizado em `FileUtils`             |



| Antes                        | Agora                                            |
| ---------------------------- | ------------------------------------------------ |
| Muitos `print()` soltos      | Log estruturado e controlado                     |
| Difícil filtrar mensagens    | Usa níveis (`INFO`, `WARNING`, `ERROR`, `DEBUG`) |
| Nenhum histórico             | Arquivo `logs/app.log` mantém o registro         |
| Duplicação em vários módulos | Configuração central e reutilizável              |


| Situação                                  | Como rodar           | Como importar                                     |
| ----------------------------------------- | -------------------- | ------------------------------------------------- |
| Rodando do diretório raiz (✅ recomendado)| `python -m src.main` | `from src.clientes_service import ClienteService` |
| Rodando dentro de `src/`                  | `python main.py`     | `from clientes_service import ClienteService`     |
