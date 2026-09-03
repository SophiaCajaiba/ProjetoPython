#Declarar variáveis
Depósito = float(input("Digite o valor do depósito na poupança: "))
Meses = int(input("Digite o número de meses que deseja calcular o rendimento: "))

#Calcular o rendimento mensal do depósito
Rendimento = Depósito * (1.013 * Meses)

#Mostrar o resultado
print("O rendimento do depósito em ", Meses, " meses na poupança é: ", Rendimento)

