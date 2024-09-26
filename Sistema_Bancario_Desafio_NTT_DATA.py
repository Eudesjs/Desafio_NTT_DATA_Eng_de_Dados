# Função Menu()

import textwrap

def menu():
    menu = """\n
    ================================= MENU ================================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Conta
    [nu]\tNovo Usuário
    [q]\tSair
    === """

    return input(textwrap.dedent(menu))

# Função Depositar()

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n=== Deposito Realizado com Sucesso! ===")
    else:
        print("\n@@@ Operação Falhou! O valor Informado é Inválido. @@@")

    return saldo, extrato

# Função Sacar()

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação Falhou! Você nao Tem Saldo Suficiente. @@@") 
    elif excedeu_limite:
        print("\n@@@ Operação Falhou! O Valor do Saque Excede o Limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação Falhou! Número Máximo de Saques Excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\tR$: {valor:.2f}\n"
        numero_saques += 1
        print("\n@@@ === Saque Realizado Com Sucesso === @@@")
    else:
        print("\n === Operação Falhou! O Valor Informado é Inválido. ===")

    return saldo, extrato


# Função Extrato()

def exibir_extrato(saldo, /, *, extrato):
        if not extrato:
            print("\n======================= EXTRATO =============================")
            print("Nao Foram Realizado Movimentações.")
        else:
            print(f"Conta:\t\tR$ {extrato}")
            print(f"\nSaldo:\t\tR$ {saldo:.2f}")
            print("================================================================")

# Função Nova_Conta()

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do Usuário: ")
    usuario = nova_conta(cpf, usuarios)

    if usuario:
        print("\n=== Conta Criada com Sucesso! ===")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": {"nome": usuario["nome"], "cpf": usuario["cpf"], "data_nascimento": usuario["data_nascimento"], "endereco": usuario["endereco"]}}
    
    print("\n@@@ Usuário não Encontrado, Fluxo de Criação de Conta Encerrado! @@@")

# Função Filtrar_USuario()

def filtrar_usuario(cpf, usuarios):
    usuario_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None

# Função Criar_Conta()

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do Usuário: ")
    usuario = nova_conta(usuarios, agencia)
    if usuario:
        print("\n=== Conta Criada com Sucesso ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
       
    print("\n@@@ Usuario nao Encontrado, Fluxo de Criação de Conta Encerrado! @@@")
        
# Função Listar_Contas()

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


# Função Novo_Usuario()

def novo_usuario(usuarios):
    cpf = input("Informe o CPF (Apenas Números): ")
    usuario = nova_conta(cpf, usuarios)

    if usuario:
        print("\n@@@ Já Existe Usuário com esse CPF! @@@")
    else: 
        nome = input("Informe o Nome Completo: ")
        data_nascimento = input("Informe a Data de Nascimento (dd - mm - aaaa): ")
        endereco = input("Informe o Endereço (Logradouro, Nro - Bairro - Cidade - Estado/sigla): ")
        usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
        print("=== Usuario Criado com Sucesso! ===")

# Função main()

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
            valor = float(input("Informe o Valor do Depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o Valor do Saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )   

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(conta)

        elif opcao == "q":
            break
        else:
            print("Operação Inválida, por faovr Selecione Novamente a Operação Desejada.")

main()
