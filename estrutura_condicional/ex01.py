#CRIANDO FUNÇÃO
def cadastrar(nome, idade):
    print('Bom dia ', nome, 
          '\n Sua idade é: ', idade)
    
cadastrar('Rafael', 20)
cadastrar('Fabia', 30)

#FUNÇÃO SOMAR NUMEROS
def somar(n1, n2):
    return n1 + n2

print('\n\nA soma dos números = ', somar(56, 4))

#FUNÇÃO CALCULAR SALARIO
def calcular_salario(qtd_horas, valor_horas):
    horas = float(qtd_horas)
    taxa = float(valor_horas)
    if horas <= 40:
        salario = horas * taxa
    else:
        horas_excd= horas - 40
        salario = 40 * taxa +(horas_excd*(1.5*taxa))
    return salario

str_horas = input('Digite a quantidadede horas: ')
str_taxa = input('Digite o valor da hora: ')
total_salario = calcular_salario(str_horas, str_taxa)
print('O valor total do salário a receber é: ', total_salario)