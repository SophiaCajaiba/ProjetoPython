#Declarar variáveis
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

#Calcular o valor de delta
delta = (b ** 2) - (4 * a * c)

#Calcular as raízes da equação
X1 = (-b + (delta ** 0.5)) / (2 * a)
X2 = (-b - (delta ** 0.5)) / (2 * a)

#Mostrar o resultado
print("O valor de X1 é: ", X1)
print("O valor de X2 é: ", X2)