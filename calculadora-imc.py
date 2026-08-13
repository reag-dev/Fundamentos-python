import math

print("Calculadora de IMC com base na classificação da OMS")
weight = float(input("Informe seu peso (KG): "))
height = float(input("Informe sua altura (M): "))
imc = (height* height) / weight

if(40 >= imc):
    print("Obesidade grau III (grave)")
elif(35.0 >= imc and imc <= 39.9):
    print("Obesidade grau II (risco grave)")
elif(30.0 >= imc and imc <= 34.9):
    print("Obesidade grau I (risco aumentado)")
elif(25.0 >= imc and imc <= 29.9):
    print("Sobrepeso (risco moderado)")
elif(18.5 >= imc and imc <= 24.9):
    print("Peso normal (adequado)")
else:
    print("Magreza (baixo peso)")

