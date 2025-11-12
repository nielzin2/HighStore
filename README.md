# 📦 Sistema de Gerenciamento de Almoxarifado Web

### 🌟 Visão Geral

Este projeto é um **Sistema Web de Controle de Estoque (Almoxarifado)** desenvolvido para digitalizar e otimizar a administração de materiais. Nosso foco é fornecer uma interface eficiente para o gerenciamento do ciclo completo de vida dos itens através das operações **CRUD (Criação, Leitura, Atualização, Exclusão)**.

---

### 💡 Arquitetura e Tecnologias

O sistema é construído sobre uma arquitetura **Python** robusta, garantindo escalabilidade e manutenibilidade.

| Categoria | Tecnologia/Conceito | Descrição |
| :--- | :--- | :--- |
| **Framework Web** | **🐍 Django** | Backbone da aplicação web; responsável pelo roteamento, ORM e segurança. |
| **Linguagem** | **Python 3.x** | Usada para toda a lógica de negócio (*backend*), modelos e views. |
| **Banco de Dados** | **SQLite** | Banco de dados embutido, ideal para desenvolvimento e MVP. |
| **Metodologia** | **Kanban / Interativo** | Desenvolvimento incremental, focado na visualização do fluxo de trabalho e entregas contínuas. |
| **Controle de Versão** | **GitHub** | Rastreamento de código e colaboração. |

### 📋 Funcionalidades Chave (CRUD)

| Operação | Funcionalidade | Status |
| :--- | :--- | :--- |
| **C - Criação (`Create`)** | Formulários para registrar novos itens no estoque (nome, quantidade, unidade). | 🟢 Em Desenvolvimento |
| **R - Leitura (`Read`)** | Listagem completa de todos os itens e visualização detalhada. | 🟢 Em Desenvolvimento |
| **U - Atualização (`Update`)** | Edição de informações e ajuste de quantidades de itens existentes. | 🟢 Em Desenvolvimento |
| **D - Exclusão (`Delete`)** | Remoção permanente de itens do registro. | 🟢 Em Desenvolvimento |

---

### 🏗️ Estrutura e Status Atual

Estamos na fase de **Setup do Projeto Django (F-07)**, com a base de dados (Models) e configurações globais definidas.

| Arquivo/Módulo | Detalhe |
| :--- | :--- |
| `requirements.txt` | Lista de todas as dependências Python (`Django>=4.0`). |
| `estoque/models.py` | Definição da classe `Item`, o coração da base de dados. |
| `almoxarifado_web/settings.py` | Configurações do projeto, idioma (`pt-br`) e fuso horário. |
| `almoxarifado_web/urls.py` | Roteamento principal, direcionando o tráfego para a aplicação `estoque`. |

---
