import textwrap

# Função Menu()

def menu():
    menu = """\n
    --------------------- MENU -------------------
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar conta
    [nu]\tNovo usuario
    [q]\tSair
    ==> """
    return input(textwrap.dedent(menu))

# Função Depositar()

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n=== Deposito Realizado com Sucesso! ===")
    else:
        print("\n=== Operação Falhou! O Valor Informado é Inválido. ===")

    return saldo, extrato

# Função Sacar()

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n=== Operação Falhou! Você nao tem saldo suficiente. ===")

    elif excedeu_limite:
        print("\n=== Operação Falhou! O valor do saque excede o limite. ===")

    elif excedeu_saques:
        print("\n=== Operação Falhou! Numero maximo de saques excedido. ===")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque Realizado com Sucesso! ===")

    else:
        print("\n=== Operação Falhou! O valor Informado é Inválido. ===")

    return saldo, extrato

# Função Extrato()

def exibir_extrato(saldo, /, *, extrato):
    print("\n -------------------- EXTRATO --------------")
    print("Nao Foram Realizadas Movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("----------------------------------------------")

# Função Criar_Usuario()

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente Numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Já existe usuario com esse CPF! ===")
        return
    
    nome = input("Informe o Nome Completo: ")
    data_nascimento = input("Informe a Data de Nascimento (dd-mm-aaa): ")
    endereco = input("Informe o Endereço (Logradouro, Nro - Bairro - Cidade/Sigla Estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário Criado com Sucesso! ===")

# Função Filtrar_Usuario()

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


# Função Criar_Conta()

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do Usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta Criada com Sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n=== Usuário nao Encontrado, O Fluxo de Criação de Conta Encerrado! ===")

# Função Listar_Contas()

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


# Função Main()

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o Valor do Deposito: "))
            saldo, extrato = depositar(saldo,valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o Valor de Saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação Inválida, Por favor selecione novamente a operação desejada.")

main()