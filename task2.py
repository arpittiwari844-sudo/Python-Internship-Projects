import random
number = random.randint(1,100)

attempt = 0
print("Welcome to the Number Guessing Game")


while True :

    guess = int(input("Enter Your Guess(1-100) :"))
    if(guess<1 or guess>100):
        print("Invalid Input,enter number between 1 and 100")
        continue
    
    attempt +=1
    if(guess == number):
        print("Congratulations,you guessed the number!")
        print(f"Attempt :{attempt}")
        break
    elif(guess < number):
        print("Too Low!")
    else:
        print("Too High!")