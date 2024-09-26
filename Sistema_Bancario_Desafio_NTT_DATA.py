# Função Menu()

import textwrap

def menu():
    menu = """\n
    ================================= MENU ================================
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [Nc]\tNova Conta
    [Lc]\tListar Conta
    [Nu]\tNovo Usuário
    [Q]\tSair
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
    print("\n======================= EXTRATO =============================")
    print("\n Nao Foram Realizado Movimentações." if not extrato else extrato)
    print("\nSaldo:\t\tR$ {saldo:.2f}")
    print("================================================================")


# Função Criar Usuário()

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente Números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Já Existe Usuário com esse CPF! @@@")
        return
    nome = input("Informe o Nome Completo: ")
    data_nascimento = input("Informe a Data de Nascimento (dd, mm, aaaa): ")
    endereco = input("Informe o Endereço (Logradouro - Numero - Bairro - Cidade/Sigla - Estado): ")
    usuarios.append({"nome": nome, "Data_Nascimento": data_nascimento, "CPF": cpf, "Endereço": endereco})
    print("\n=== Usuário Criado com Sucesso! ===")

# Função Filtrar_USuario()

def filtrar_usuario(cpf, usuarios):
    usuario_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None

# Função Criar_Conta()

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do Usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta Criada com Sucesso ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        print("\n@@@ Usuario nao Encontrado, Fluxo de Criação de Conta Encerrado! @@@")
        