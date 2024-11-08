print("---SISTEMA BANCÁRIO--\n")

#Criando Váriaveis
saldo = 2500
saque = 0
deposito = 0
extrato = [] #criando um vetor

#FOR / WHILE
#ESTUTURA DE REPETIÇÃO - MENU

while True:
    print("\n---MENU---")
    print("1 - Deposito")
    print("2 - Sacar")
    print("3 - Ver Extrato")
    print("4 Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        #Deposito
        deposito = float(input("Informe o valor que deseja depositar: "))
        saldo += deposito
        extrato.append(f"Depósito: +R$ {deposito:.2f}")
        print("Deposito realizado com sucesso!!")
        
    elif opcao == "2":
        #Saque
        saque = float(input("Informe o valor que deseja sacar: R$ "))
        if saque <= saldo:
            saldo -= saque
            extrato.append(f"Saque: -R$ {saque:.2f}")
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente ... para realizar saque")
    
    elif opcao == "3":
        #Extrato
        print("\n---EXTRATO---")
        if extrato:
            for operacao in extrato:
                print(operacao)
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Nenhuma operação realizada") 
            
            
    elif opcao == "4":
        #sair
        print("Saindo do sistema bancario ....")
        break
    
    else: 
        print("Opção Invalida, tente novamente")

    #print(f"\nSaldo atual: R$ {saldo: .2f}")     
        