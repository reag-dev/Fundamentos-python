print("Calculadora de IMC com base na classificação da OMS")

while True:
    try:
        weight = float(input("Informe seu peso (KG): "))
        height = float(input("Informe sua altura (M): "))
    except ValueError:
        print("Por favor, forneça um numero de formato válido!")
        continue
        
    if (weight <= 0 or height <= 0):
        print("Peso e altura deve ser maiores que zero.")
        continue

    imc =  weight / height ** 2

    print(f"Seu IMC é {imc:.2f}")
    if imc < 18.5:
        print("Magreza")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    elif imc < 35:
        print("Obesidade grau I")
    elif imc < 40:
        print("Obesidade grau II")
    else:
        print("Obesidade grau III")
    
    user_command = input("\n Digite [x] para encerrar o programa ou outra tecla para repetir: ")
    if user_command.lower() == "x":
        break
