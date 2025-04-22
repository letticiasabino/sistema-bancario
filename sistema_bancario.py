#Sistema Bancário com Depósito, Saque e Extrato

#Variáveis para armazenar os dados

saldo = 0
limite_saque = 500.00
saques_diarios = 0
LIMITE_SAQUES_DIARIOS = 3
transacoes = []
extrato = ""

#Definindo funções

def formatar_valor(valor):
    """Formatar valor no formato R$ xxx,xx"""
    return f"R$ {valor:,.2f}".replace(',', 'X') .replace(".", ",") .replace("X", ".")

def depositar(valor):
    """Realiza um depósito e atualiza o saldo e transações."""
    global saldo
    if valor > 0:
        saldo += valor
        transacoes.append(("Depósito", valor))
        print(f"Depósito de {formatar_valor(valor)} realizado com sucesso!")
    else:
        print("Erro: Valor de depósito deve ser positivo.")

def sacar(valor):
    """Realiza um saque , respeitando os limites e saldos."""
    global saldo, saques_diarios
    if saques_diarios >= LIMITE_SAQUES_DIARIOS:
        print("Erro: Limite de saques diários atingido.")
        return
    if valor > limite_saque:
        print(f"Erro: Valor de saque excede o limite de R$ {formatar_valor(limite_saque)}.")
        return
    if valor > saldo:
        print(f"Erro: Saldo insuficiente. Saldo atual: {formatar_valor(saldo)}.")
        return
    if valor <= 0:
        print("Erro: O valor de saque deve ser positivo.")
        return
    
    saldo -= valor
    saques_diarios += 1
    transacoes.append(("Saque", valor))
    print(f"Saque de {formatar_valor(valor)} realizado com sucesso!")

def exibir_extrato():
    """Exibe o extrato com todas as transações e o saldo atual."""
    if not transacoes:
        print("Nenhuma trasação realizada.")
    else:
        print("\n=== Extrato Bancário ===")
        for tipo, valor in transacoes:
            print(f"{tipo}: {formatar_valor(valor)}")
        print(f"\nSaldo atual: {formatar_valor(saldo)}")
        print("========================\n")

#Menu interativo
while True:
    print("\n=== Sistema Bancário ===")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1 - 4): ")
    
    if opcao == "1":
        try:
            valor = float(input("Digite o valor do depósito: R$ "))
            depositar(valor)
        except ValueError:
            print("Erro: Digite um valor número válido. Tente novamente.")
        
    elif opcao == "2":
        try:
            valor = float(input("Digite o valor do saque: R$ "))
            sacar(valor)
        except ValueError:
            print("Erro: Digite um valor número válido. Tente novamente.")

    elif opcao == "3":
        exibir_extrato()

    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")