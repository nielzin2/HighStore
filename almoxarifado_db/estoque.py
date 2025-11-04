from .database import get_db_connection
import sqlite3

# --- CRUD: CREATE (C) ---

def adicionar_item(nome: str, quantidade: int, unidade_medida: str):
    """
    Adiciona um novo item ao estoque (tabela Itens).
    
    Args:
        nome (str): Nome do item (ex: "Parafuso").
        quantidade (int): Quantidade inicial.
        unidade_medida (str): Unidade (ex: "un", "m", "cx").
    
    Returns:
        bool: True se o item foi adicionado com sucesso, False caso contrário.
    """
    if quantidade <= 0:
        print("ERRO: A quantidade deve ser um número inteiro positivo.")
        return False
        
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO Itens (nome, quantidade, unidade_medida) VALUES (?, ?, ?)",
            (nome, quantidade, unidade_medida)
        )
        conn.commit()
        print(f"\n[SUCESSO] Item '{nome}' adicionado ao estoque.")
        return True
    except sqlite3.Error as e:
        print(f"\n[ERRO] Falha ao adicionar item: {e}")
        return False
    finally:
        conn.close()


# --- CRUD: READ (R) ---

def listar_todos_itens():
    """
    Retorna todos os itens presentes na tabela Itens.
    
    Returns:
        list of sqlite3.Row: Uma lista de objetos Item, ou uma lista vazia.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    itens = []
    
    try:
        cursor.execute("SELECT id, nome, quantidade, unidade_medida FROM Itens ORDER BY nome")
        # O fetchall() retorna todas as linhas como objetos sqlite3.Row (dicionários)
        itens = cursor.fetchall() 
    except sqlite3.Error as e:
        print(f"\n[ERRO] Falha ao listar itens: {e}")
    finally:
        conn.close()
        
    return itens
