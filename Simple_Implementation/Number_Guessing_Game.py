import random

def play_game():
    rand_number = random.randint(1,101)
    guesses_left = 0
    numbers_guessed = []
    print("Guess a number between 1 - 100 \n ")
    print("If you guess wrong, you get a hint whether it's too high or too low \n")
    print("Select difficulty: \n 0 = 10 guesses (easy) \n 1 = 7 guesses (medium) \n 2 = 5 guess (hard)")
    difficulty = int(input("You selected:"))
    
    if difficulty == 0 :
        guesses_left = 10
    elif difficulty == 1 :
        guesses_left = 7
    else : 
        guesses_left = 5
    
    while guesses_left > 0:
        player_guess = int(input("Select a number: "))
        
        if player_guess == rand_number :
            print("You Win! The random number was", rand_number)
            break
        else : 
            if rand_number > player_guess :
                print("Too low!")
            else :
                print("Too High!")
                
        numbers_guessed.append(player_guess)

        for i in range(len(numbers_guessed)) :
            print(numbers_guessed[i])
        
        guesses_left = guesses_left - 1
        print("Guesses Left:", guesses_left)
    
play_game();