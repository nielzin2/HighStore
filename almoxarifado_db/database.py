import sqlite3

# Define o nome do arquivo do banco de dados
DB_FILE = 'almoxarifado.db'

def get_db_connection():
    """
    Estabelece a conexão com o banco de dados SQLite e configura para 
    retornar linhas como dicionários (acesso por nome da coluna).

    Returns:
        sqlite3.Connection: O objeto de conexão.
    """
    conn = sqlite3.connect(DB_FILE)
    # Define o row_factory para sqlite3.Row para acesso por nome (dicionário)
    conn.row_factory = sqlite3.Row 
    return conn

def inicializar_banco_de_dados():
    """
    Cria a tabela 'Itens' no banco de dados se ela não existir, 
    definindo a estrutura básica do almoxarifado.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL para criar a tabela Itens
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                unidade_medida TEXT NOT NULL
            );
        """)
        conn.commit()
        print("Estrutura do banco de dados inicializada com sucesso (Tabela 'Itens' verificada/criada).")
    except sqlite3.Error as e:
        print(f"ERRO: Não foi possível inicializar o banco de dados. {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    # Teste para garantir que o banco de dados é criado ao executar este arquivo
    inicializar_banco_de_dados()
