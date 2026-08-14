while True:
    print("Tabuada interativa")
    
    try: 
        user_number = int(input("Digite um número: "))
    except ValueError:
        print("Valor inválido!")
        continue
    
    for i in range(1, 11):
        print(f"{user_number} x {i} = {user_number * (i)}")
    
    user_input = input("Digite [S] para realizar outra tabuada: ")
    if(user_input.lower() == 's'):
        continue
    
    break
    