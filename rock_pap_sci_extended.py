from random import choice

RATING = 0

move = []
# move = ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors',
#         'snake', 'human', 'tree', 'wolf', 'sponge', 'paper','air', ]

win = {
    'water': ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water']
}

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

options = input().split(',')
if options == ['']:
    move = ['rock', 'paper', 'scissors']
elif options != ['']:
    move = options
print("Okay, let's start")

while True:
    current_move = choice(move)
    user_input = input()

    if user_input == '!rating':
        print(f'Your rating: {RATING}')

    elif user_input == '!exit':
        break

    elif user_input in move:
        # print(current_move)
        if user_input == current_move:
            print(f"There is a draw ({current_move})")
            RATING += 50

        if user_input != current_move:
            for key, value in win.items():
                if user_input == key and current_move in value:
                    print(f"Well done. The computer chose {current_move} and failed")
                    RATING += 100
                if user_input == key and current_move not in value:
                    print(f"Sorry, but the computer chose {current_move}")
    else:
        print('Invalid input')

print('Bye!')

# player = f'{name} {RATING}'
# input_file.write(f'{player}\n')
# input_file.close()


