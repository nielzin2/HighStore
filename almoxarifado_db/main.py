# main.py
# Este é o ponto de entrada da aplicação para teste

from almoxarifado_db.database import inicializar_banco_de_dados
from almoxarifado_db.estoque import adicionar_item, listar_todos_itens

def exibir_itens(itens):
    """
    Formata e exibe a lista de itens.
    """
    if not itens:
        print("\n--- O estoque está vazio. ---")
        return
        
    print("\n--- Estoque Atual ---")
    print(f"{'ID':<4} | {'Nome':<30} | {'Quantidade':<12} | {'Unidade':<10}")
    print("-" * 60)
    for item in itens:
        print(f"{item['id']:<4} | {item['nome']:<30} | {item['quantidade']:<12} | {item['unidade_medida']:<10}")
    print("-" * 60)


if __name__ == "__main__":
    print("--- Inicializando Sistema de Almoxarifado ---")
    
    # 1. (F-01) Garante que o banco de dados e a tabela existem
    inicializar_banco_de_dados()
    
    # 2. (F-02) Testando a função de Adicionar Item (CREATE)
    print("\nAdicionando itens de teste...")
    adicionar_item("Parafuso Sextavado M10", 500, "unidades")
    adicionar_item("Cabo de Rede CAT6", 150, "metros")
    adicionar_item("Chave Phillips 5mm", 10, "peças")
    
    # 3. (F-03) Testando a função de Listar Todos (READ)
    print("\nListando todos os itens:")
    itens_em_estoque = listar_todos_itens()
    exibir_itens(itens_em_estoque)
    
    print("\n--- Fim do Teste Básico ---")
    
    # Observação: Na prática, você executaria este main.py
    # em seu ambiente local (VS Code, terminal, etc.) para criar o arquivo 
    # almoxarifado.db e ver o resultado no console.
