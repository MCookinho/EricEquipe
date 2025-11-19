# PetroBahia S.A.

A **PetroBahia S.A.** é uma empresa fictícia do setor de óleo e gás. Seu sistema interno calcula preços de combustíveis, valida clientes e gera relatórios. 
O código está **mal estruturado** e **difícil de manter**. O objetivo é **refatorar** aplicando **PEP8**, **Clean Code** e **princípios SOLID** (SRP e OCP).

## Objetivos
- Melhorar legibilidade e clareza do código
- Extrair funções e classes coesas
- Eliminar duplicações e efeitos colaterais
- Melhorar nomes e modularidade

## COMO EXECUTAR
no dir ```/workspaces/EricEquipe/repo_petrobahia``` rode no cmd ```python -m src.main```

## COMO EXECUTAR O TESTES PYTEST

Para executar o pytest navegue ate o dir ```/workspaces/EricEquipe/repo_petrobahia``` rode no cmd ```pytest -v```

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

“legacy” sugere codigo legado sem especificar o que esta fazendo

“services” representa bem as regras de negócio.

“data/” guarda os dados, deixando src/ limpo.


## MUDANÇAS FEITAS

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


### PYTEST MUDANCAS FEITAS

As mudanças realizadas para habilitar a execução correta do pytest no projeto foram essenciais para tornar a estrutura mais sólida, padronizada e compatível com boas práticas de desenvolvimento Python. A primeira etapa foi configurar o arquivo pytest.ini, definindo o caminho base para que o pytest reconhecesse o diretório src como um pacote importável, eliminando erros de importação que impediam a coleta de testes. Em seguida, foi necessário ajustar toda a lógica de importação interna do projeto, substituindo imports relativos ou inválidos por imports absolutos, garantindo consistência e previsibilidade em qualquer ambiente — local, contêiner, pipeline ou Codespaces.

Outra mudança importante foi a refatoração do módulo file_utils.py, que originalmente utilizava uma classe estática (FileUtils). Os testes unitários, porém, esperavam funções soltas, e a refatoração tornou o módulo mais simples, direto e aderente ao padrão pythonista. Como consequência, os serviços que dependiam dessa utilidade precisaram ser atualizados para chamar as novas funções diretamente, substituindo referências à antiga classe. Além disso, os testes de serviço foram ajustados para usar tmp_path, isolando operações de leitura e escrita em arquivos temporários, evitando que o repositório fosse poluído durante a execução dos testes. Essas melhorias combinadas não apenas permitiram que todo o conjunto de testes rodasse com sucesso, como também deixaram o código mais limpo, mais seguro e mais fácil de manter.
