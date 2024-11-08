#Sistema Bancário

print("--- SISTEMA BANCÁRIO ---\n")
#variáveis

saldo = 2500
saque = 0
deposito = 0
extrato = 0


print("Saldo : R$", saldo, "\n")
print("Informe o valor que Deseja Depositar: ")
deposito = int(input())

#Operação Deposito

saldo = saldo + deposito

print("O novo saldo é: R$", saldo)

#Operação Saque

print("Informe o valor que deseja sacar")
saque = int(input())

saldo = saldo -saque

print("O novo saldo é R$", saldo)




