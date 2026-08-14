import random

print("Jogo de advinhação de número (1 a 100) \n")
match_state = "new_match" # playing | new_match

while True:
    
    if match_state == 'new_match':
        rand_number = random.randint(1, 100)
        match_state = 'playing'
    
    try: 
        user_number = int(input("Tente adivinhar o número de 1 a 100: "))
    except ValueError:
        print("Forneça um numero válido!")
        continue
    
    if 1 > user_number or user_number > 100:
        print("Numero fornecido está fora do intervalo de 1 a 100")
        continue
      
    if user_number > rand_number:
        print("Mais pra baixo!")
        continue
    elif user_number < rand_number:
        print("Mais pra cima!")
        continue
    else: 
        print("Você venceu!")
       
    print(f"\n O número sorteado era: {rand_number}")    
    
    user_input = input("Se deseja jogar novamente digite [S]")
    if(user_input.lower() == "s"):
        match_state = 'new_match'
        continue
    break