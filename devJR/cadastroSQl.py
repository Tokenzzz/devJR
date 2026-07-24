import sqlite3

conexao = sqlite3.connect("compras.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE,
    preco REAL
)
""")
conexao.commit()

def calcular_total():
    cursor.execute("SELECT preco FROM produtos")
    linhas = cursor.fetchall()

    soma = 0
    for linha in linhas:
        soma = soma + linha[0]
    print(f"O valor total das compras salvas no banco é: R$ {soma:.2f}")

while True:
    nome_prod = input("Digite o ingrediente ou sair para finalizar ")

    if nome_prod.lower() == "sair":
        break
    
    if any([c.isdigit() for c in nome_prod]):
        print(" ⚠️ Erro: O nome do ingrediente não pode conter números!")
        continue

    try:
        preco_prod = float(input(f"Digite o preço de '{nome_prod}': R$ "))
    except ValueError:
        print(" ⚠️ Preço inválido! Digite apenas números separados por ponto (EX: 10.50)")
        continue

    try:
        cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", (nome_prod, preco_prod))
        conexao.commit()
        print(f"✅ '{nome_prod}' salvo no banco de dados com sucesso!")
    except sqlite3.IntegrityError:
            print(f" ⚠️ Aviso: O item '{nome_prod}' já está cadastrado no banco!")
            continue
    
calcular_total()

conexao.close()