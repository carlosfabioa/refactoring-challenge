## [1.1.0] - 2026-06-12 (PT-BR)

### Visão geral

Refatoração completa do Sistema de Gerenciamento de Biblioteca. A base de código original foi aprimorada com melhor organização, convenções de nomenclatura mais claras, documentação abrangente e suporte à internacionalização (inglês).

### Adicionado

- **Sistema de Gerenciamento de Biblioteca**: um aplicativo de linha de comando para gerenciar empréstimos e devoluções de livros
- **Recursos principais**:
  - Visualizar todos os livros disponíveis com seu status de disponibilidade
  - Emprestar livros para usuários cadastrados (com validação de limite de empréstimos)
  - Devolver livros emprestados (com rastreamento de usuários)
  
- **Estrutura do projeto**:
  - `main.py`: ponto de entrada com interface baseada em menu
  - `app/` módulo: funções específicas da aplicação
    - `fetchFuncs.py`: operações de recuperação de dados
    - `modifyFuncs.py`: operações de modificação de dados (empréstimo e devolução)
  - `utils/` módulo: funções utilitárias
    - `helpers.py`: utilidades comuns (entrada/saída de arquivos, constantes, configuração)
  - `db/` diretório: persistência de dados
    - `books.txt`: banco de dados de livros com ID, título, autor e status de disponibilidade
    - `users.txt`: banco de dados de usuários com ID, nome e status de empréstimo
    
- **Documentação**:
  - Docstrings das funções explicando propósito e comportamento
  - Comentários claros no código para lógica complexa
  - CHANGELOG abrangente e documentação do projeto

### Alterado

- **Internacionalização do código**: migração de todo o código e da documentação do português para o inglês
  - Os nomes das funções agora seguem convenções de nomenclatura em inglês
  - Os nomes de variáveis são claros e descritivos
  - Comentários e docstrings usam inglês para colaboração internacional
  
- **Melhorias de qualidade de código**:
  - Melhoria nos nomes de métodos: `fetchFuncs` em vez de abreviações pouco claras
  - Adição de dicas de tipo nas assinaturas das funções
  - Refatoração do tratamento de arquivos com gerenciadores de contexto (`with`)
  - Melhor separação de responsabilidades entre os módulos
  
- **Arquitetura**:
  - Estrutura modular implementada com separação de responsabilidades
  - Funções utilitárias centralizadas em `helpers.py`
  - Fluxo de dados claro entre módulos

### Detalhes técnicos

#### Modelo de dados

**Livros (db/books.txt)**
```
Formato: ID;Título;Autor;StatusDisponibilidade
- ID: identificador único do livro
- Título: título do livro
- Autor: nome do autor
- StatusDisponibilidade: "1" (Disponível) ou "0" (Indisponível)
```

**Usuários (db/users.txt)**
```
Formato: ID;Nome;StatusEmpréstimo
- ID: identificador único do usuário
- Nome: nome do usuário
- StatusEmpréstimo: "1" (Possui um livro emprestado) ou "0" (Nenhum livro emprestado)
```

#### Fluxo do sistema

1. **Inicialização**: `setup()` cria os arquivos do banco de dados com dados iniciais
2. **Interação do usuário**: interface baseada em menu para operações com livros
3. **Operações com livros**: 
   - Visualizar: exibir todos os livros com disponibilidade
   - Emprestar: verificar limite de usuário, marcar livro como indisponível e atualizar status do usuário
   - Devolver: marcar livro como disponível e limpar status de empréstimo do usuário
4. **Persistência de dados**: alterações gravadas de volta aos arquivos imediatamente

#### Principais decisões de design

- **Banco de dados baseado em arquivos**: arquivos de texto simples para fins de desenvolvimento e aprendizado
- **Flags de status**: flags binárias (0/1) por simplicidade e análise
- **Limite de empréstimo**: um livro por usuário por vez
- **Persistência imediata**: alterações salvas em disco após cada operação

### Corrigido

- Removidos os comandos de impressão de depuração (por exemplo, `print(ROOT_DIR)` em helpers.py)
- Corrigido o nome de variáveis pouco claras para melhorar a legibilidade
- Resolvidos padrões lógicos confusos com uma estrutura mais clara

### Limitações conhecidas

- Os caminhos de arquivo usam barras invertidas no estilo Windows (requer correção multiplataforma)
- Não há validação de entrada para IDs de livro/usuário (assume entradas válidas)
- Não há criptografia nem medidas de segurança (para fins de desenvolvimento/aprendizado)
- Sessão única do usuário (sem tratamento de acesso simultâneo)
- Sem tratamento de erros para exceções de entrada/saída de arquivos
- Limitado a um empréstimo por usuário

Basicamente, a lógica de negócio não foi alterada, eu decidi mantê-la já que não era minha tarefa fazer essa reescrita.

### Melhorias futuras

- [ ] Implementar banco de dados adequado (SQLite/PostgreSQL)
- [ ] Adicionar validação abrangente de entrada
- [ ] Implementar tratamento de erros e logs
- [ ] Adicionar sistema de autenticação de usuários
- [ ] Suportar múltiplos empréstimos por usuário
- [ ] Implementar tratamento de caminhos de arquivo multiplataforma
- [ ] Adicionar testes unitários
- [ ] Criar camada de API para acesso externo
- [ ] Adicionar persistência de dados com ORM
- [ ] Implementar papéis e permissões de usuário
