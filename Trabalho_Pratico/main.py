import csv

# ===================== Carregar dados =====================
def carregar_usuarios():
    usuarios = []
    try:
        with open('usuarios.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                usuarios.append(row)
    except FileNotFoundError:
        print("Arquivo usuarios.csv não encontrado!")
    return usuarios

def carregar_produtos():
    produtos = []
    try:
        with open('produtos.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['preco'] = float(row['preco'])
                row['quantidade'] = int(row['quantidade'])
                produtos.append(row)
    except FileNotFoundError:
        print("Arquivo produtos.csv não encontrado!")
    return produtos

# ===================== Salvar dados =====================
def salvar_usuarios(usuarios):
    with open('usuarios.csv', 'w', newline='') as file:
        fieldnames = ['id','nome','usuario','senha','tipo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for u in usuarios:
            writer.writerow(u)

def salvar_produtos(produtos):
    with open('produtos.csv', 'w', newline='') as file:
        fieldnames = ['codigo','nome','preco','quantidade','categoria']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for p in produtos:
            writer.writerow(p)

# ===================== CRUD Usuários =====================
def criar_usuario(usuarios):
    print("\n=== Criar Usuário ===")
    id = str(int(usuarios[-1]['id']) + 1 if usuarios else 1)
    nome = input("Nome: ")
    usuario = input("Login: ")
    senha = input("Senha: ")
    tipo = input("Tipo (admin/funcionario/cliente): ").lower()
    usuarios.append({"id": id, "nome": nome, "usuario": usuario, "senha": senha, "tipo": tipo})
    salvar_usuarios(usuarios)
    print("Usuário criado com sucesso!")

def listar_usuarios(usuarios):
    print("\n=== Lista de Usuários ===")
    for u in usuarios:
        print(f"{u['id']} - {u['nome']} ({u['tipo']})")

def atualizar_usuario(usuarios):
    listar_usuarios(usuarios)
    id = input("Digite o ID do usuário para atualizar: ")
    for u in usuarios:
        if u['id'] == id:
            u['nome'] = input(f"Novo nome ({u['nome']}): ") or u['nome']
            u['usuario'] = input(f"Novo login ({u['usuario']}): ") or u['usuario']
            u['senha'] = input(f"Nova senha ({u['senha']}): ") or u['senha']
            u['tipo'] = input(f"Novo tipo ({u['tipo']}): ") or u['tipo']
            salvar_usuarios(usuarios)
            print("Usuário atualizado!")
            return
    print("Usuário não encontrado!")

def deletar_usuario(usuarios):
    listar_usuarios(usuarios)
    id = input("Digite o ID do usuário para deletar: ")
    for u in usuarios:
        if u['id'] == id:
            usuarios.remove(u)
            salvar_usuarios(usuarios)
            print("Usuário deletado!")
            return
    print("Usuário não encontrado!")

# ===================== CRUD Produtos =====================
def criar_produto(produtos):
    print("\n=== Criar Produto ===")
    codigo = input("Código: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    categoria = input("Categoria: ")
    produtos.append({"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade, "categoria": categoria})
    salvar_produtos(produtos)
    print("Produto criado com sucesso!")

def listar_produtos(produtos):
    print("\n=== Lista de Produtos ===")
    for p in produtos:
        print(f"{p['codigo']} - {p['nome']} | R${p['preco']} | Qtde: {p['quantidade']} | {p['categoria']}")

def buscar_produto(produtos):
    termo = input("Digite código ou nome do produto: ").lower()
    for p in produtos:
        if termo == p['codigo'].lower() or termo in p['nome'].lower():
            print(f"{p['codigo']} - {p['nome']} | R${p['preco']} | Qtde: {p['quantidade']} | {p['categoria']}")
            return
    print("Produto não encontrado!")

def atualizar_produto(produtos):
    listar_produtos(produtos)
    codigo = input("Digite o código do produto para atualizar: ")
    for p in produtos:
        if p['codigo'].lower() == codigo.lower():
            p['nome'] = input(f"Novo nome ({p['nome']}): ") or p['nome']
            p['preco'] = float(input(f"Novo preço ({p['preco']}): ") or p['preco'])
            p['quantidade'] = int(input(f"Nova quantidade ({p['quantidade']}): ") or p['quantidade'])
            p['categoria'] = input(f"Nova categoria ({p['categoria']}): ") or p['categoria']
            salvar_produtos(produtos)
            print("Produto atualizado!")
            return
    print("Produto não encontrado!")

def deletar_produto(produtos):
    listar_produtos(produtos)
    codigo = input("Digite o código do produto para deletar: ")
    for p in produtos:
        if p['codigo'].lower() == codigo.lower():
            produtos.remove(p)
            salvar_produtos(produtos)
            print("Produto deletado!")
            return
    print("Produto não encontrado!")

def listar_produtos_nome(produtos):
    print("\n=== Produtos Ordenados por Nome ===")
    for p in sorted(produtos, key=lambda x: x['nome']):
        print(f"{p['nome']} - R${p['preco']} | Qtde: {p['quantidade']}")

def listar_produtos_preco(produtos):
    print("\n=== Produtos Ordenados por Preço ===")
    for p in sorted(produtos, key=lambda x: x['preco']):
        print(f"{p['nome']} - R${p['preco']} | Qtde: {p['quantidade']}")

# ===================== Login e Menu =====================
def login(usuarios):
    print("\n=== Login ===")
    user = input("Login: ")
    senha = input("Senha: ")
    for u in usuarios:
        if u['usuario'] == user and u['senha'] == senha:
            print(f"Bem-vindo, {u['nome']} ({u['tipo']})!")
            return u['tipo']
    print("Login inválido!")
    return None

def menu():
    usuarios = carregar_usuarios()
    produtos = carregar_produtos()
    tipo_usuario = login(usuarios)
    if not tipo_usuario:
        return

    while True:
        print("\n=== Menu Principal ===")
        if tipo_usuario == "admin":
            print("1- Criar Usuário\n2- Listar Usuários\n3- Atualizar Usuário\n4- Deletar Usuário")
            print("5- Criar Produto\n6- Listar Produtos\n7- Buscar Produto\n8- Atualizar Produto\n9- Deletar Produto")
            print("10- Listar Produtos por Nome\n11- Listar Produtos por Preço\n0- Sair")
            escolha = input("Escolha: ")

            if escolha == "1": criar_usuario(usuarios)
            elif escolha == "2": listar_usuarios(usuarios)
            elif escolha == "3": atualizar_usuario(usuarios)
            elif escolha == "4": deletar_usuario(usuarios)
            elif escolha == "5": criar_produto(produtos)
            elif escolha == "6": listar_produtos(produtos)
            elif escolha == "7": buscar_produto(produtos)
            elif escolha == "8": atualizar_produto(produtos)
            elif escolha == "9": deletar_produto(produtos)
            elif escolha == "10": listar_produtos_nome(produtos)
            elif escolha == "11": listar_produtos_preco(produtos)
            elif escolha == "0": break
            else: print("Opção inválida!")

        elif tipo_usuario == "funcionario":
            print("1- Criar Produto\n2- Listar Produtos\n3- Buscar Produto\n4- Atualizar Produto\n5- Deletar Produto")
            print("6- Listar Produtos por Nome\n7- Listar Produtos por Preço\n0- Sair")
            escolha = input("Escolha: ")

            if escolha == "1": criar_produto(produtos)
            elif escolha == "2": listar_produtos(produtos)
            elif escolha == "3": buscar_produto(produtos)
            elif escolha == "4": atualizar_produto(produtos)
            elif escolha == "5": deletar_produto(produtos)
            elif escolha == "6": listar_produtos_nome(produtos)
            elif escolha == "7": listar_produtos_preco(produtos)
            elif escolha == "0": break
            else: print("Opção inválida!")

        elif tipo_usuario == "cliente":
            print("1- Listar Produtos\n2- Buscar Produto\n3- Listar Produtos por Nome\n4- Listar Produtos por Preço\n0- Sair")
            escolha = input("Escolha: ")

            if escolha == "1": listar_produtos(produtos)
            elif escolha == "2": buscar_produto(produtos)
            elif escolha == "3": listar_produtos_nome(produtos)
            elif escolha == "4": listar_produtos_preco(produtos)
            elif escolha == "0": break
            else: print("Opção inválida!")

if __name__ == "__main__":
    menu()
