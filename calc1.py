print("---------Calculadora-------------")
n1 = float(input("Informe um número: "))
n2 = float(input("Informe um número: "))
operador = input("Digite o operador (+, -, *, /:  ")

if operador == '+':
    print(n1 + n2)
elif operador == '-':
    print(n1 - n2)
elif operador == '*':
    print(n1 * n2)
else:
    print(n1 / n2)