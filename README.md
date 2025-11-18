# 📦 HighStore - Gerenciador de Almoxarifado

Projeto final desenvolvido para a disciplina **Técnicas de Desenvolvimento de Algoritmo**, focado na aplicação de lógica avançada, estruturas de dados nativas de Python e arquitetura de software profissional.

### ✨ Visão Geral

O **HighStore** é um **Sistema Web de Controle de Estoque** que oferece uma interface moderna e segura para o gerenciamento completo do inventário. O projeto valida o uso de **CRUD (Create, Read, Update, Delete)** e implementa lógicas de gestão, como alertas de estoque mínimo e rastreamento de movimentação.

---

## 🏆 Avaliação Final: Critérios da Disciplina

O projeto atinge o nível **Excelente** em todos os critérios e garante o **Ponto Extra** de modularização, conforme a ficha de avaliação.

| Critério | Status | Detalhamento da Implementação |
| :--- | :--- | :--- |
| **CRUD Completo** | ✅ **Ok** | Operações C, R, U, D completas, funcionais e seguras para Itens e Logística. |
| **Lógica e Estrutura** | ✅ **Ok** | Arquitetura MVT robusta do Django. Lógica de estoque baixo e controle transacional. |
| **Listas e Dicionários** | ✅ **Ok** | Lógica de alertas (`obter_alertas_estoque_baixo`) isolada em `services.py` que manipula e retorna **Listas de Dicionários** nativas do Python. |
| **Modularização (Extra)**| ✅ **Ok** | Lógica de negócio isolada em **`estoque/services.py`** com funções de alta coesão e baixo acoplamento. |
| **Segurança (Adicional)** | ✅ **Ok** | Todas as rotas de gestão estão protegidas por **Login e Autenticação** (`@login_required`). |

---

## 💡 Arquitetura e Tecnologias

| Categoria | Tecnologia/Conceito | Função |
| :--- | :--- | :--- |
| **Linguagem Principal**| **Python 3.13+** | Usada em todo o backend. |
| **Framework Web** | **🐍 Django** | Estrutura MVT (Model-View-Template) e ORM. |
| **Lógica de Algoritmo**| **`estoque/services.py`** | Módulo dedicado à execução de funções com Listas e Dicionários. |
| **Interface (UX)** | **Bootstrap 5** | Design moderno, limpo e responsivo. |
| **Segurança** | **Autenticação Padrão** | Sistema de Login/Logout e proteção de rotas. |

---

## ⚙️ Guia de Instalação e Execução Local

### 1. Clonar e Configurar o Ambiente

```bash
# 1. Clonar o Repositório
git clone [https://github.com/nielzin2/HighStore.git](https://github.com/nielzin2/HighStore.git)
cd HighStore

# 2. Criar e Ativar o Ambiente Virtual

# 3. Instalar Dependências (Django, etc.)
pip install -r requirements.txt

# 4. Criar e Aplicar Migrações (Cria todas as tabelas)
python manage.py migrate

#5. Criar Superusúario (login Admin)
python manage.py createsuperuser

#6 Iniciar Servidor
python manage.py runserver

Acesse o sistema no navegador: http://127.0.0.1:8000/ (você será redirecionado para a tela de Login).

python -m venv venv
.\venv\Scripts\activate # Windows
# source venv/bin/activate # Linux/macOS
