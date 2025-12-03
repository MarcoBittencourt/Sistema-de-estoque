# **Sistema de Estoque**

Um sistema desenvolvido em **Python** para o controle e gerenciamento de produtos em um **galpão de armazenamento**.  
O projeto visa otimizar o registro de itens, acompanhar movimentações de entrada e saída, gerar relatórios e manter o controle de usuários de forma simples e eficiente.

---

# Autores

- **João Victor Lindberg Gomes de Moraes** -**Product owner**
- **Joaquim Paulo Vieira de Melo**         -**Time de desenvolvedores**
- **José Miguel Correia Dias**             -**Time de desenvolvedores**
- **José Rodrigo de Santana Lima**         -**Time de desenvolvedores**
- **Marco Antônio Bittencourt Costa**      -**Scrumm Master**

---

# Funcionalidades Principais

- **Cadastro de produtos:** registre novos itens com informações como nome, código, quantidade, categoria e fornecedor.  
- **Movimentação de estoque:** controle as **entradas e saídas** de produtos, com histórico detalhado.  
- **Relatórios:** gere relatórios de estoque atual, movimentações e produtos com baixo nível de quantidade.    

---

# trello

<img width="1250" height="817" alt="image" src="https://github.com/user-attachments/assets/2a247a1b-1253-426b-8934-1853bf8d6a1a" />



**link:** https://trello.com/invite/b/69035c1fe594dab62bf05b80/ATTI1fa56aab5c213bfe82ac4c4fae93108313BBA7AA/projeto-final-sandeison

---

# Diagrama de Classes

<img width="1277" height="293" alt="Captura de tela 2025-11-26 183534" src="https://github.com/user-attachments/assets/efd45175-7472-416c-863c-b38f6bcb8c21" />




# Diagrama de casos de uso

<img width="570" height="692" alt="Captura de tela 2025-11-10 091625" src="https://github.com/user-attachments/assets/6b06960c-c8bb-4434-8c6c-9eafc5b66910" />


# Diagrama desequência

<img width="880" height="572" alt="Captura de tela 2025-11-13 081711" src="https://github.com/user-attachments/assets/cc46c113-b169-41f3-a4da-c62da2c43ac6" />


# Modelo entidade relacionamento

<img width="1270" height="433" alt="Captura de tela 2025-11-26 183653" src="https://github.com/user-attachments/assets/f2c8c23a-20e6-4f33-b194-54355a25e479" />



---

# Tecnologias Utilizadas

- **Linguagem:** Python + HTML + CSS 
- **Banco de Dados:** SQLite3
- **Bibliotecas:** django

---

# Estrutura de dados


**arquivo raiz**: SQLite 3

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

·         Relatórios (snapshot por data, total por categoria, itens abaixo do estoque mínimo, auditoria).

 ##  Requisitos Não Funcionais

·         Persistência durável: banco relacional (Postgres, MySQL) ou NoSQL quando apropriado.
·         Autenticação segura e autorização baseada em papéis (RBAC).

·         Escalabilidade horizontal e vertical para suportar desde 1 até dezenas de milhares de itens e usuários.

·         Segurança: TLS/HTTPS, criptografia em repouso para documentos sensíveis, proteção contra injections e XSS.

·         Internacionalização: formatos de data, multilíngue quando necessário.

·         Logs, monitoramento e estratégia de backups com testes periódicos de restore.


**Link:**  https://docs.google.com/document/d/1AcYf1uLQNP1-pEKIbFG9oFyqUw3kATcOblzQKo8zAnI/edit?tab=t.0

# **Testes**

# Testes unitários realizados:
·    Função adicionar item

·    Função  remover item

·    Função limpar estoque

# Teste de integração:
·   Classe estoque

**Link:** https://docs.google.com/document/d/1zFkvGLDfj65pnoVK0iUFj36kBWI0w3nAYn71Fvb2yfg/edit?usp=sharing



