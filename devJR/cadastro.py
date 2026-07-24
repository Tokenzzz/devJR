def calcular_total(lista):
    soma = 0
    for item in lista:
        soma = soma + item["preco"]
    print(f"O valor total das compras é: R$ {soma:.2f}")

lista_produtos = []
opcao = ""

while True:
    nome_prod = input("Digite o ingrediente ou sair para finalizar ")

    if nome_prod.lower() == "sair":
         break
    
    if any([c.isdigit() for c in nome_prod]):
         print(" ⚠️ Erro: O nome do ingrediente não pode conter números!")
         continue

    if nome_prod.lower() in [p["nome"].lower() for p in lista_produtos]:
        print(f" ⚠️ Aviso: '{nome_prod}' Já cadastrado! Tente outro ingrediente.")
        continue

    try:
            preco_prod = float(input("Digite o preço do produto "))
    except ValueError:
            print("Preço inválido! Digite apenas números separados por ponto (EX: 10.50)")
    
    produto = {"nome": nome_prod, "preco": preco_prod}
    lista_produtos.append(produto)
 
calcular_total(lista_produtos)