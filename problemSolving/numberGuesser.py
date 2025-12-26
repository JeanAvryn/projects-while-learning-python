import random

secret = random.randint(1, 20)
lives = 5
rounds = 0
while True:
    guess = int(input('Guess a number: '))
    rounds += 1
    if guess > secret:
        print('Lower!')
    elif guess < secret:
        print('Higher!')
    elif guess == secret:
        print('Correct!')
        break
    if rounds == lives:
        print(f'You lose! The number was {secret}.')
        break
