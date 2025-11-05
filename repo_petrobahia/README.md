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

