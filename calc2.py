def soma(n1, n2):
    return n1 + n2
    
    
def subtracao(n1, n2):
    return n1 - n2
    
    
def multiplicacao(n1, n2):
    return n1 * n2
    
    
def divisao(n1, n2):
    return n1 / n2
    




print("---------Calculadora-------------")
n1 = float(input("Informe um número: "))
n2 = float(input("Informe um número: "))
operador = input("Digite o operador (+, -, *, /):  ")

if operador == '+':
    resultado = soma(n1, n2)
    
    
elif operador == '-':
    resultado = subtracao(n1, n2)
    
    
elif operador == '*':
    resultado = multiplicacao(n1, n2)
    
    
else:
    resultado = divisao(n1, n2)
    
    
print(f" O resultado é:  {resultado}")
