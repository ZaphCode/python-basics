import random

secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 3

print('---- Guess the secret number ----')

def gameStart(attempts):
    while attempts < max_attempts:

        #* Handleling error

            #? Try - Except statement
        try:
            guess = int(input(f'Attempt {attempts + 1} >>> '))
        except ValueError:
            print('You must to type numeric values')
            continue

            #? Using isnumeric function
        #guess = input(f'Attempt {attempts + 1} >>> ')
        # if(not guess.isnumeric()):
        #     print('You must to type numeric values')
        #     continue
        # guess = int(guess)

        if guess == secret_number:
            print(f'Congratulations, you won! the number is {secret_number}')
            break
        attempts += 1
    else:
        print(f'You losed, the secret number is {secret_number}')

gameStart(attempts)

while True:
    startAgain = input('Try again? (y / n) >>> ')
    if startAgain.lower() == 'y':
        print('Restart game')
        gameStart(attempts)
    elif startAgain.lower() == 'n':
        print('Game end')
        break
    else:
        print('Invalid value')
