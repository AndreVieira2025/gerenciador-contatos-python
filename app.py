# app.py

def adicionar_contato(contatos, nome, telefone, email):
    """Adiciona um novo contato à lista."""
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    contatos.append(contato)
    print(f"Contato '{nome}' adicionado com sucesso!")

def listar_contatos(contatos):
    """Lista todos os contatos cadastrados."""
    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    print("\n--- Lista de Contatos ---")
    for i, contato in enumerate(contatos):
        print(f"{i+1}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    print("-------------------------\n")

def buscar_contato(contatos, termo_busca):
    """Busca contatos por nome ou telefone."""
    resultados = []
    termo_busca = termo_busca.lower()

    for contato in contatos:
        if termo_busca in contato['nome'].lower() or termo_busca in contato['telefone'].lower():
            resultados.append(contato)

    if not resultados:
        print(f"Nenhum contato encontrado para '{termo_busca}'.")
        return

    print(f"\n--- Resultados da Busca para '{termo_busca}' ---")
    for contato in resultados:
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    print("-------------------------------------------\n")

def main():
    """Função principal do gerenciador de contatos."""
    contatos = [] # Lista para armazenar os contatos

    while True:
        print("\n--- Gerenciador de Contatos ---")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato")
        print("4. Sair")
        print("-------------------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            adicionar_contato(contatos, nome, telefone, email)
        elif opcao == '2':
            listar_contatos(contatos)
        elif opcao == '3':
            termo = input("Digite o nome ou telefone para buscar: ")
            buscar_contato(contatos, termo)
        elif opcao == '4':
            print("Saindo do Gerenciador de Contatos. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()

