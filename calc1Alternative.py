print("---------Calculadora-------------")
n1 = float(input("Informe um número: "))
n2 = float(input("Informe um número: "))
operador = input("Digite o operador (+, -, *, /:  ")

if operador == '+':
    resultado = n1 + n2
elif operador == '-':
    resultado = n1 - n2
elif operador == '*':
    resultado = n1 * n2
else:
    resultado = n1 / n2
    
print(f" O resultado é:{resultado}")
