print("--- SISTEMA BANCÁRIO ---\n")

# Variáveis
saldo = 2500
saque = 0
deposito = 0
extrato = []

# Loop principal
while True:
    print("\n--- Menu ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Operação de Depósito
        deposito = float(input("Informe o valor que deseja depositar: R$ "))
        saldo += deposito
        extrato.append(f"Depósito: +R$ {deposito:.2f}")
        print("Depósito realizado com sucesso!")

    elif opcao == "2":
        # Operação de Saque
        saque = float(input("Informe o valor que deseja sacar: R$ "))
        if saque <= saldo:
            saldo -= saque
            extrato.append(f"Saque: -R$ {saque:.2f}")
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque.")

    elif opcao == "3":
        # Exibir Extrato
        print("\n--- Extrato ---")
        if extrato:
            for operacao in extrato:
                print(operacao)
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Nenhuma operação realizada.")
    
    elif opcao == "4":
        # Sair do sistema
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")

    print(f"\nSaldo atual: R$ {saldo:.2f}")
