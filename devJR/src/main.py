contatos = []

def cadastrar_contato():
    print("\n--- NOVO CADASTRO ---")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    cidade = input("Digite a cidade: ")
    
    contato = {
        "nome": nome,
        "email": email,
        "cidade": cidade
    }
    
    contatos.append(contato)
    print(f"\n✅ Contato {nome} cadastrado com sucesso!\n")

def listar_contatos():
    print("\n--- LISTA DE CONTATOS ---")
    if not contatos:
        print("Nenhum contato cadastrado ainda.\n")
        return
        
    for i, c in enumerate(contatos, start=1):
        print(f"{i}. Nome: {c['nome']} | Email: {c['email']} | Cidade: {c['cidade']}")
    print()

def menu():
    while True:
        print("=== SISTEMA DE CADASTRO DEVJR ===")
        print("1. Cadastrar novo contato")
        print("2. Listar contatos")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1-3): ")
        
        if opcao == "1":
            cadastrar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    menu()