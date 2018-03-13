from os import system

# this Dictionary creates the initial game board, Keys are easy to update moves, and values draw the board
# Note Keys with whole numbers represent the numerical key pad pattern when drawn 
board = {'7L':' ','7':' ','7R':' ','TL':'|','8L':' ','8':' ','8R':' ','TR':'|','9L':' ','9':' ','9R':' ',
         'TL1':'-','TL2':'-','TL3':'-','TL4':'|','TL5':'-','TL6':'-','TL7':'-','TL8':'|','TL9':'-','TL10':'-','TL11':'-',
         '4L':' ','4':' ','4R':' ','ML':'|','5L':' ','5':' ','5R':' ','MR':'|','6L':' ','6':' ','6R':' ',
         'BL1':'-','BL2':'-','BL3':'-','BL4':'|','BL5':'-','BL6':'-','BL7':'-','BL8':'|','BL9':'-','BL10':'-','BL11':'-',
         '1L':' ','1':' ','1R':' ','BL':'|','2L':' ','2':' ','2R':' ','BR':'|','3L':' ','3':' ','3R':' '}

# List used to track the current user positions
pos = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def check_win():
    '''
            Winning Numpad Combinations are 
            1) 789 
            2) 741
            3) 753
            4) 159
            5) 456
            6) 258
            7) 963
            8) 123
            
            KEY: How it Maps
                pos.index = ['0','1','2','3','4','5','6','7','8']
                pos.value = ['7','8','9','4','5','6','1','2','3']
    '''
    
    # 789 - TOP ROW WIN
    if pos[0] == "X" and pos[1] == "X" and pos[2] == "X":
        game_won("X","TOP ROW WIN")

    # 741 - LEFT SIDE WIN
    elif pos[0] == "X" and pos[3] == "X" and pos[6] == "X":
        game_won("X","LEFT SIDE WIN")        

    # 753 - DIAGNAL TOP LEFT to BOTTOM RIGHT WIN
    elif pos[0] == "X" and pos[4] == "X" and pos[8] == "X":
        game_won("X","DIAGNAL TOP LEFT to BOTTOM RIGHT WIN")

    # 159 - DIAGNAL BOTTOM LEFT to TOP RIGHT WIN
    elif pos[6] == "X" and pos[4] == "X" and pos[2] == "X":
        game_won("X","DIAGNAL BOTTOM LEFT to TOP RIGHT WIN")
    
    # 456 - MIDDLE ROW WIN
    elif pos[3] == "X" and pos[4] == "X" and pos[5] == "X":
        game_won("X","MIDDLE ROW WIN")
    
    # 258 - MIDDLE VERTTICAL WIN
    elif pos[7] == "X" and pos[4] == "X" and pos[1] == "X":
        game_won("X","MIDDLE VERTTICAL WIN")
    
    # 963 - RIGHT SIDE WIN 
    elif pos[2] == "X" and pos[5] == "X" and pos[8] == "X":
        game_won("X","RIGHT SIDE WIN")
    
    # 123 - BOTTOM ROW WIN
    elif pos[6] == "X" and pos[7] == "X" and pos[8] == "X":
        game_won("X","BOTTOM ROW WIN")
    
    # 789 - TOP ROW WIN
    elif pos[0] == "O" and pos[1] == "O" and pos[2] == "O":
        game_won("O","TOP ROW WIN")

    # 741 - LEFT SIDE WIN
    elif pos[0] == "O" and pos[3] == "O" and pos[6] == "O":
        game_won("O","LEFT SIDE WIN")        

    # 753 - DIAGNAL TOP LEFT to BOTTOM RIGHT WIN
    elif pos[0] == "O" and pos[4] == "O" and pos[8] == "O":
        game_won("O","DIAGNAL TOP LEFT to BOTTOM RIGHT WIN")

    # 159 - DIAGNAL BOTTOM LEFT to TOP RIGHT WIN
    elif pos[6] == "O" and pos[4] == "O" and pos[2] == "O":
        game_won("O","DIAGNAL BOTTOM LEFT to TOP RIGHT WIN")
    
    # 456 - MIDDLE ROW WIN
    elif pos[3] == "O" and pos[4] == "O" and pos[5] == "O":
        game_won("O","MIDDLE ROW WIN")
    
    # 258 - MIDDLE VERTTICAL WIN
    elif pos[7] == "O" and pos[4] == "O" and pos[1] == "O":
        game_won("O","MIDDLE VERTTICAL WIN")
    
    # 963 - RIGHT SIDE WIN 
    elif pos[2] == "O" and pos[5] == "O" and pos[8] == "O":
        game_won("O","RIGHT SIDE WIN")
    
    # 123 - BOTTOM ROW WIN
    elif pos[6] == "O" and pos[7] == "O" and pos[8] == "O":
        game_won("O","BOTTOM ROW WIN")

    elif "".join(pos).find(" ") == -1:
        game_won("N","SORRY - NO WINNERS TODAY!")
    else:
        run_game(move_num)


def game_won(game_piece,win_text):
    if game_piece == "N":
        system('cls')
        print_board()
        print("\n" + win_text +"\n\n" )
        print("Do you want to play again?")
        play_again = input(" 1 for Yes - 2 for No: ")
        if int(play_again) == 2:
            system('exit')
        elif int(play_again) == 1:
            reset_board()
            system('cls')
            pos = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            move_num = 0
            run_game(move_num)
    else:
        system('cls')
        print_board()
        print("\nCONGRADULATIONS \"" + game_piece + "\" WON AT " + win_text +"\n\n" )
        print("Do you want to play again?")
        play_again = input(" 1 for Yes - 2 for No: ")
        if int(play_again) == 2:
            system('exit')
        elif int(play_again) == 1:
            reset_board()
            system('cls')
            pos = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            move_num = 0
            run_game(move_num)
        else:
            print("******** LN ~131 fired so aparently I need some code here ********")

# Lets set some game variables
move_num = 1
Player1 = ""
Player2 = ""

# Used to print the board current state or initial state. 
def print_board():
    system('cls')
    print(board['7L'],board['7'],board['7R'],board['TL'],
          board['8L'],board['8'],board['8R'],board['TR'],
          board['9L'],board['9'],board['9R'])
    print(board['TL1'],board['TL2'],board['TL3'],board['TL4'],
          board['TL5'],board['TL6'],board['TL7'],board['TL8'],
          board['TL9'],board['TL10'],board['TL11'])
    print(board['4L'],board['4'],board['4R'],board['ML'],
          board['5L'],board['5'],board['5R'],board['MR'],
          board['6L'],board['6'],board['6R'])
    print(board['BL1'],board['BL2'],board['BL3'],board['BL4'],
          board['BL5'],board['BL6'],board['BL7'],board['BL8'],
          board['BL9'],board['BL10'],board['BL11'])
    print(board['1L'],board['1'],board['1R'],board['BL'],
          board['2L'],board['2'],board['2R'],board['BR'],
          board['3L'],board['3'],board['3R'])


# Used to reset the board at the end of the game
def reset_board():
    board['7'] = ' '
    board['8'] = ' '
    board['9'] = ' '
    board['4'] = ' '
    board['5'] = ' '
    board['6'] = ' '
    board['1'] = ' '
    board['2'] = ' '
    board['3'] = ' '
    pos[0] = ' '
    pos[1] = ' '
    pos[2] = ' '
    pos[3] = ' '
    pos[4] = ' '
    pos[5] = ' '
    pos[6] = ' '
    pos[7] = ' '
    pos[8] = ' '
    print_board()

# Takes in a list of current moves and updates the board
def board_moves(moves):
    for x,y in enumerate(moves):
        if x == 0:
            board['7'] = y
        if x == 1:
            board['8'] = y
        if x == 2:
            board['9'] = y
        if x == 3:
            board['4'] = y
        if x == 4:
            board['5'] = y
        if x == 5:
            board['6'] = y
        if x == 6:
            board['1'] = y
        if x == 7:
            board['2'] = y
        if x == 8:
            board['3'] = y
    print_board()
    # Check do we have a winner? 
    check_win()

# up date the positions List from user input
def user_moves(x,y):
    # TOP numpad 7,8,9 
    if  x == 7 and y=='X':
        if pos[0] == ' ':
            pos[0] = 'X'
        else:
            run_game(move_num,1,7)
    elif  x == 7 and y=='O':
        if pos[0] == ' ':
            pos[0] = 'O'
        else:
            run_game(move_num,1,7)
    elif  x == 8 and y=='X':
        if pos[1] == ' ':
            pos[1] = 'X'
        else:
            run_game(move_num,1,8)        
    elif  x == 8 and y=='O':
        if pos[1] == ' ':
            pos[1] = 'O'
        else:
            run_game(move_num,1,8)
    elif  x == 9 and y=='X':
        if pos[2] == ' ':
            pos[2] = 'X'
        else:
            run_game(move_num,1,9)
    elif  x == 9 and y=='O':
        if pos[2] == ' ':
            pos[2] = 'O'
        else:
            run_game(move_num,1,9)

    # MIDDLE numpad 4,5,6 
    elif  x == 4 and y=='X':
        if pos[3] == ' ':
            pos[3] = 'X'
        else:
            run_game(move_num,1,4)        
    elif  x == 4 and y=='O':
        if pos[3] == ' ':
            pos[3] = 'O'
        else:
            run_game(move_num,1,4)
    elif  x == 5 and y=='X':
        if pos[4] == ' ':
            pos[4] = 'X'
        else:
            run_game(move_num,1,5)
    elif  x == 5 and y=='O':
        if pos[4] == ' ':
            pos[4] = 'O'
        else:
            run_game(move_num,1,5)
    elif  x == 6 and y=='X':
        if pos[5] == ' ':
            pos[5] = 'X'
        else:
            run_game(move_num,1,6)
    elif  x == 6 and y=='O':
        if pos[5] == ' ':
            pos[5] = 'O'
        else:
            run_game(move_num,1,6)

    # Bottom numpad 1,2,3 
    elif  x == 1 and y=='X':
        if pos[6] == ' ':
            pos[6] = 'X'
        else:
            run_game(move_num,1,1)
    elif  x == 1 and y=='O':
        if pos[6] == ' ':
            pos[6] = 'O'
        else:
            run_game(move_num,1,1)
    elif  x == 2 and y=='X':
        if pos[7] == ' ':
            pos[7] = 'X'
        else:
            run_game(move_num,1,2)
    elif  x == 2 and y=='O':
        if pos[7] == ' ':
            pos[7] = 'O'
        else:
            run_game(move_num,1,2)
    elif  x == 3 and y=='X':
        if pos[8] == ' ':
            pos[8] = 'X'
        else:
            run_game(move_num,1,3)
    elif  x == 3 and y=='O':
        if pos[8] == ' ':
            pos[8] = 'O'
        else:
            run_game(move_num,1,3)
        pos[8] = 'O'
    else:
        return "Please pick a number 1-9"
    board_moves(pos)

# alternate players
# start game sequence
def run_game(turn,taken=0,square=0):
        global move_num
        if taken==1:
            system('cls')
            print('DAMN! - you picked square '+str(square) +' and it''s already taken ')
        if turn%2==0:
            print_board()
            #print(pos)
            print("\nX moves \n ")
            x = input(Player2 + ", please pick a number 1-9:  ")
            while True:
                try:
                    if int(x) in range(1,10):
                        move_num += 1
                        user_moves(int(x),"X")
                        break
                except:
                    system('cls')
                    print_board()
                    print("You did not type a number, try again\n\n")
                    x = input(Player2 + ", please pick a number 1-9:  ")
                else:
                    system('cls')
                    print_board()
                    print("Your NOT picking a single number between 1 and 9. Please try again...\n\n")
                    x = input(Player2 + ", please pick a number 1-9:  ")
        else:
            print_board()
            #print(pos)
            print("\nO moves \n ")
            x = input(Player1 + ", please pick a number 1-9:  ")
            while True:
                try:
                    if int(x) in range(1,10):
                        move_num += 1
                        user_moves(int(x),"O")
                        break
                except:
                    system('cls')
                    print_board()                    
                    print("You did not type a number, try again\n\n")
                    x = input(Player1 + ", please pick a number 1-9:  ")
                else:
                    system('cls')
                    print_board()
                    print("Your NOT picking a single number between 1 and 9. Please try again...\n\n")
                    x = input(Player1 + ", please pick a number 1-9:  ")

# Get the players names
def get_players():
    global Player1
    global Player2
    Player1 = input('Player 1 what\'s your name?  ')
    system('cls')
    Player2 = input('Player 2 What\'s your name?  ')
    system('cls')
    run_game(move_num)

# Start the game
if __name__ == "__main__":
    system('cls')
    get_players()