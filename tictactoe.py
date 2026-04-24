import time
import os

print(r"""                                                 
__      _____| | ___ ___  _ __ ___   ___  
\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
 \ V  V /  __/ | (_| (_) | | | | | |  __/ 
  \_/\_/ \___|_|\___\___/|_| |_| |_|\___|""")

time.sleep(1)
os.system('cls')

# game table
table = ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]']

# combinations for victory
combinations = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 5, 3],
    [1, 5, 9]
]

# defined the player and generated a value for the game variable
player = 'X'
game = True

# ensures the player switches after every turn
def change_player(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player

# receives player input, validates if position is free and places the player mark
def make_play(table, player):
    play = int(input('Make your move (1 to 9): '))
    if '[' in table[play - 1]:
        table[play - 1] = player
    else:
        print('Position filled!')
    return play

# checks if any winning combination is fully occupied by the same player
def check_winner(table, combinations, player):
    for combo in combinations:
        if table[combo[0] - 1] == player and table[combo[1] -1] == player and table[combo[2] - 1] == player:
            return True
    return False

# checks if all positions are occupied, meaning no winner and no free spaces
def check_draw(table):
    for position in table:
        if position != 'X' and position != 'O':
            return False
    return True

# outer loop that allows the game to be restarted
while True:
    # main game loop — runs until someone wins or draws
    while game:
        print(f'{table[0]} {table[1]} {table[2]} '
              f'\n{table[3]} {table[4]} {table[5]}'
              f'\n{table[6]} {table[7]} {table[8]}')
        make_play(table, player)
        time.sleep(0.5)
        os.system('cls')
        if check_winner(table, combinations, player):
            print(f'Player {player} Win!')
            game = False

        elif check_draw(table):
            print('DRAW!')
            game = False
        player = change_player(player)
    time.sleep(0.8)
    restart = input('Would you like to restart the game?(y/n)')
    if restart == 'y':
        table = ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]']
        player = 'X'
        game = True
    else:
        print('Thank you for playing!')
        break
