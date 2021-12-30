from random import choice

RATING = 0
move = ['rock', 'paper', 'scissors']
win = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
players = {}

player_name = input('Enter your name: ')
print(f'Hello, {player_name}')

with open('rating.txt', 'r') as input_file:
    for line in input_file:
        name, score = line.strip().split(' ')
        players[name] = score

if player_name in players:
    RATING = int(players[player_name])
    print(f'Your rating: {RATING}')

while True:
    current_move = choice(move)
    user_input = input()

    if user_input == '!rating':
        print(f'Your rating: {RATING}')

    elif user_input == '!exit':
        break

    elif user_input == 'rock' or user_input == 'paper' or user_input == 'scissors':
        print(current_move)
        if user_input == current_move:
            print(f"There is a draw ({current_move})")
            RATING += 50

        elif user_input != current_move:
            for key, value in win.items():
                if key == user_input and value == current_move:
                    print(f"Well done. The computer chose {current_move} and failed")
                    RATING += 100
                if key == user_input and value != current_move:
                    print(f"Sorry, but the computer chose {current_move}")
    else:
        print('Invalid input')

print('Bye!')



