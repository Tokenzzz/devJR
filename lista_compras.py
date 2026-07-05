lista_compras = []
item_digitado = ""

while item_digitado != "sair":
    item_digitado = input ("Digite um ingrediente (ou 'sair'): ")

    if item_digitado != "sair":
        lista_compras.append(item_digitado)
        
        
print (" --- SUA LISTA DE COMPRAS ---")
for item in lista_compras:
    print(item)

