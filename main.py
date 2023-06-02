
def cadastrar_usuario(usuarios):
    usuario = input('Cadastre seu usuário: ')
    senha = input('Cadastre sua senha: ')
    usuarios.append({'usuario': usuario, 'senha': senha})
    print('Cadastro realizado com sucesso!')
    with open('usuarios.txt', 'w') as arquivo:
        for user in usuarios:
            linha = f"Usuario: {user['usuario']} Senha: {user['senha']}\n"
            arquivo.write(linha)

def fazer_login(usuarios):
    usuario = input('Digite o nome do usuário: ')
    senha = input('Digite a senha: ')
    for user in usuarios:
        if user['usuario'] == usuario and user['senha'] == senha:
            print('Login realizado com sucesso!')
            return True
    else:
        print('Usuário ou senha incorretos, digite novamente.')
        return False

def pagina_inicial():
    sair_sistema = False
    while True:
        print('====PÁGINA INICIAL=====')
        print('1 - Voltar para página de login')
        print('2 - Sair do sistema')
        print()
        valor_opcao = input('Digite o número de qual opção você deseja: ')
        if valor_opcao == '1':
            break
        elif valor_opcao == '2':
            print('Você saiu do sistema!')
            sair_sistema = True
            exit()

def main():
    usuarios = []
    while True:
        print(
            'Bem vindo ao NossoApp'
            '\nEscolha uma das opções abaixo'
            '\n1 - Fazer cadastro'
            '\n2 - Fazer login'
            '\n3 - Sair do sistema'
        )
        valor_opcao = input('Digite o número de qual opção você deseja: ')

        if valor_opcao == '1':
            cadastrar_usuario(usuarios)

        elif valor_opcao == '2':
            if fazer_login(usuarios):
                pagina_inicial()

        elif valor_opcao == '3':
            print('Você saiu do sistema!')
            break

        else:
            print('Opção inválida, digite novamente.')

if __name__ == "__main__":
    main()