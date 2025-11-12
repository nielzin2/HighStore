# 📦 HighStore: Sistema de Gerenciamento de Almoxarifado Web

### ✨ Visão Geral

O **HighStore** é um **Sistema Web de Controle de Estoque** desenvolvido para digitalizar e otimizar a administração de materiais. A aplicação oferece uma interface eficiente para o gerenciamento completo do inventário através das operações essenciais de **CRUD (Create, Read, Update, Delete)**.

---

### 💡 Arquitetura e Tecnologias

O projeto é baseado em uma arquitetura **Python** robusta (Django) e está em constante melhoria, seguindo princípios de desenvolvimento ágil.

| Categoria | Tecnologia/Conceito | Descrição |
| :--- | :--- | :--- |
| **Framework Web** | **🐍 Django** | Backbone da aplicação; ORM, roteamento e segurança. |
| **Interface (UX)** | **Bootstrap 5** | Framework CSS para um design profissional, responsivo e moderno (Integração em andamento). |
| **Linguagem** | **Python 3.x** | Lógica de negócio (*backend*) e manipulação de dados. |
| **Banco de Dados** | **SQLite** | Persistência de dados (ideal para desenvolvimento). |
| **Metodologia** | **Kanban / Interativo** | Gestão de fluxo de trabalho e entregas incrementais. |
| **Controle de Versão** | **GitHub** | Hospedagem do código-fonte. |

### 📈 Status do Projeto (Quadro Kanban)

O ciclo de vida básico do produto (CRUD) está **CONCLUÍDO**. O foco atual é em **Melhorias de Interface** e **Funcionalidades Essenciais de Estoque**.

| Fase | Funcionalidade | Status |
| :--- | :--- | :--- |
| **CRUD Básico** | Criação (C), Leitura (R), Atualização (U), Exclusão (D) de itens. | ✅ **CONCLUÍDO** |
| **UX & Interface** | F-10/11/12: Integração do **Bootstrap** e criação do **`base.html`**. | ➡️ **EM FOCO** |
| **Gestão de Estoque** | F-13: **Busca e Filtragem** de itens por nome. | 🟡 Pendente |
| **Gestão de Estoque** | F-14: Implementação de **Estoque Mínimo (Alerta)**. | 🟡 Pendente |
| **Profissionalização** | F-16: Implementação de **Login e Autenticação**. | 🟡 Pendente |

---

### 🏗️ Estrutura e Módulos Principais

A estrutura reflete um projeto Django padrão, onde a lógica de negócio está isolada na aplicação `estoque`.

| Arquivo/Módulo | Função |
| :--- | :--- |
| `manage.py` | Utilitário de linha de comando do Django (Root). |
| `requirements.txt` | Lista de todas as dependências Python. |
| `templates/base.html` | **Novo Template Base** que injeta o Bootstrap e define o layout geral. |
| `estoque/models.py` | Definição da classe `Item` (Mapeamento Objeto-Relacional). |
| `estoque/views.py` | Implementação das funções de CRUD (C, R, U, D). |
| `almoxarifado_web/settings.py` | Configurações globais (Banco de Dados, Apps, Idioma). |

---

### ⚙️ Guia de Instalação e Execução Local

Para rodar esta aplicação Django, siga os passos no terminal:

#### 1. Clonar o Repositório e Configurar o Ambiente

```bash
git clone [https://github.com/nielzin2/HighStore](https://github.com/nielzin2/HighStore)
cd HighStore
python -m venv venv
.\venv\Scripts\activate  # Ativação no Windows
# source venv/bin/activate # Ativação no Linux/macOS
