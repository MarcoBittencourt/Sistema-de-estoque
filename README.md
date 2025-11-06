# **Sistema de Estoque**

Um sistema desenvolvido em **Python** para o controle e gerenciamento de produtos em um **galpão de armazenamento**.  
O projeto visa otimizar o registro de itens, acompanhar movimentações de entrada e saída, gerar relatórios e manter o controle de usuários de forma simples e eficiente.

---

# Autores

- **João Victor Lindberg Gomes de Moraes** -**Product owner**
- **Joaquim Paulo Vieira de Melo**         -**Time de desenvolvedores (Back-End)**
- **José Miguel Correia Dias**             -**Time de desenvolvedores (Front-End)**
- **José Rodrigo de Santana Lima**         -**Time de desenvolvedores (desenrolado)**
- **Marco Antônio Bittencourt Costa**      -**Scrumm Master**

---

# Funcionalidades Principais

- **Cadastro de produtos:** registre novos itens com informações como nome, código, quantidade, categoria e fornecedor.  
- **Movimentação de estoque:** controle as **entradas e saídas** de produtos, com histórico detalhado.  
- **Relatórios:** gere relatórios de estoque atual, movimentações e produtos com baixo nível de quantidade.  
- **Controle de usuários:** autenticação e níveis de acesso para administradores e operadores.  

---

# trello

<img width="1641" height="766" alt="image" src="https://github.com/user-attachments/assets/487cd072-d3fa-446b-9265-74e0732c3d98" />


**link:** https://trello.com/invite/b/69035c1fe594dab62bf05b80/ATTI1fa56aab5c213bfe82ac4c4fae93108313BBA7AA/projeto-final-sandeison

---

# Diagrama de Classes

<img width="861" height="334" alt="Diagram_classes drawio" src="https://github.com/user-attachments/assets/1b91657f-13da-4d09-aab1-f001b8ee26e3" />


---

# Tecnologias Utilizadas

- **Linguagem:** Python + django 
- **Banco de Dados:** json 
- **Bibliotecas:** os, json e datetime

---

# Estrutura de dados


**arquivo raiz**: JSON object / dict

**chave (nome do item)**: string (uso atual: o código usa o próprio nome como chave key = nome — atenção a nomes duplicados/maiúsculas).

**quantidade**:

**tipo**: inteiro (int)

**restrição**: quantidade >= 0

**comportamento no código**:

adicionar_item soma à quantidade existente (se item existe).

remover_item subtrai; se chega a 0, o item é deletado do dicionário.

**validade**:

**tipo**: string com formato "dd/mm/YYYY" ou null

None/null indica sem validade (não perecível / indefinido)

**observado pelo código**:

tradutor_str_pra_data aceita entrada dd/mm/YYYY ou dd/mm/YY, retorna date.

_format_validade padroniza para dd/mm/YYYY ao salvar.

_is_vencido compara com date.today().

**Invariantes importantes**:

Se validade for null, _is_vencido trata como não vencido.

Sempre que quantidade == 0 o item é removido do JSON.

O código assume que quantidade existe e é inteiro ao gerar relatório; corrupção de arquivo pode causar exceções.

---

# **Requisitos**

## Funcionalidades Principais

· CRUD de itens (criar / ler / atualizar / excluir - preferencialmente soft delete).

· Categorias (hierarquia).

· Localizações físicas (depósito, loja, prateleira) e gerenciamento de estoques por local.

·         Controle de quantidade e unidade de medida (inteiros/decimais, conversão de unidade de medida mínima).

·         Lote e validade (suporte FIFO, bloqueio automático de vencidos).

·         Histórico de movimentação (entradas, saídas, transferências, ajustes) com registro de lote e validade.

·         Anexos e documentos (nota fiscal, matrícula, NF) com metadados e link/arquivo.

·         Avaliação de valor (contabilização, data da avaliação) e histórico de avaliações.

·         Relatórios (snapshot por data, total por categoria, itens abaixo do estoque mínimo, auditoria).

·         Permissões/usuários: read / write / admin e papéis customizáveis.
·         Auditoria detalhada (quem, quando, o quê e motivo).

·         Importação/Exportação (CSV/Excel), backups e versionamento dos dados.
·         Painel/Dashboard com KPIs e ações rápidas.

 ##  Requisitos Não Funcionais

·         Persistência durável: banco relacional (Postgres, MySQL) ou NoSQL quando apropriado.
·         Autenticação segura e autorização baseada em papéis (RBAC).

·         Escalabilidade horizontal e vertical para suportar desde 1 até dezenas de milhares de itens e usuários.

·         Segurança: TLS/HTTPS, criptografia em repouso para documentos sensíveis, proteção contra injections e XSS.

·         Internacionalização: formatos de data, moeda e multilíngue quando necessário.

·         Logs, monitoramento e estratégia de backups com testes periódicos de restore.

·         SLAs e requisitos de performance mínimos (ex.: listagens paginadas < 1s para 1000 itens).

 ·    Privacidade: políticas de retenção, acesso e anonimização onde aplicável.


**Link:**  https://docs.google.com/document/d/1AcYf1uLQNP1-pEKIbFG9oFyqUw3kATcOblzQKo8zAnI/edit?tab=t.0
