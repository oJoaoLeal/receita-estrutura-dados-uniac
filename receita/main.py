def gravar_receita():
    nome_receita = input("Digite o nome da receita: ")
    ingredientes = []
    print("Digite os ingredientes. Digite 'fim' quando terminar.")
    while True:
        ingrediente = input("Ingrediente: ")
        if ingrediente.lower() == 'fim':
            break
        ingredientes.append(ingrediente)
    modo_preparo = input("Digite o modo de preparo: ")

    with open("receitas.txt", "a") as arquivo:
        arquivo.write(nome_receita + "\n\n")
        arquivo.write("Ingredientes:\n")
        for ingrediente in ingredientes:
            arquivo.write("- " + ingrediente + "\n")
        arquivo.write("\nModo de Preparo:\n")
        arquivo.write(modo_preparo + "\n\n")
    print("Receita gravada com sucesso!")
    menu_opt()


def listar_receitas():
    try:
        with open("receitas.txt", "r") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Nenhuma receita encontrada.")


def consultar_receita():
    nome_receita = input("Digite o nome da receita: ")
    try:
        with open("receitas.txt", "r") as arquivo:
            receitas = arquivo.read().split("\n\n")
            for receita in receitas:
                if nome_receita in receita:
                    print(receita)
                    break
            else:
                print("Receita não encontrada.")
    except FileNotFoundError:
        print("Nenhuma receita encontrada.")


def limpar_arquivo():
    try:
        open("receitas.txt", "w").close()
        print("Arquivo de receitas limpo com sucesso!")
    except FileNotFoundError:
        print("Nenhuma receita encontrada.")


def menu_opt():
    print("1 - Criar Receita\n2 - Consultar Receita\n3 - Listar Receitas\n4 - Limpar Arquivo\n5 - Sair")
    usr_opt = input("\nDigite uma opção válida: ")

    if usr_opt == '1':
        gravar_receita()
    elif usr_opt == '2':
        consultar_receita()
    elif usr_opt == '3':
        listar_receitas()
    elif usr_opt == '4':
        limpar_arquivo()
    elif usr_opt == '5':
        print("Saindo...")
    else:
        print("Opção inválida")


if __name__ == '__main__':
    menu_opt()
