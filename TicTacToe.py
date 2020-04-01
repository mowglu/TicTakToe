def firstvisual():
    '''
    DOCSTRING: A function to print out the initial visual of X & 0 map, and to get that map as a list
    input: N/A
    output: A list of a visual representation of map, and printing that list to get the map
    '''
    # a dictionary of types of characters used to build the map. b = blank, h = horizontal, v = vertical
    dict1 = {'b': ' ', 'h':'_', 'v': '|'}
    # defining strings of the different sort of lines
    my_line1 = dict1['b'] * 3 + dict1['v'] + dict1['b'] * 3 + dict1['v'] + dict1['b'] * 3
    my_line2 = dict1['h'] * 3 + dict1['v'] + dict1['h'] * 3 + dict1['v'] + dict1['h'] * 3
    # defining a list that holds this map
    my_list = []
    # printing lines repeatedly in a pattern
    for line in range(1, 4):
        if line == 3:
            my_list.append(my_line1)
            my_list.append(my_line1)
            my_list.append(my_line1)
        else:
            for num in range(1, 4):
                if num < 3:
                    my_list.append(my_line1)
                else:
                    my_list.append(my_line2)
    for index in range(0, 9):
        print(my_list[index])
    return my_list


def game_visual(new_list):
    '''
    DOCSTRING: This is to return updated visuals for the game
    input: a list with current x's and o's
    output: a print visual
    '''
    for index in range(0, 9):
        print(new_list[index])


def user_introinput():
    '''
    DOCSTRING: A function to take in user inputs, and allows user to interact with game. Also 'clears' the board for clean reading
    input: N/A
    output: Prompts for the user
    '''
    # Introducing to the game and giving first choice of X or O.
    print('\nHello, and welcome to this 2v2 Tic Tac Toe game. This is my first project so I hope you enjoy it.\n')
    print("Player 1, please enter if you would like 'X' or 'O'.")
    check = 1
    while check == 1:
        xochoice = input().upper()
        if xochoice == 'O' or xochoice == 'X':
            check = 0
        else:
            print("Please try again")
            check = 1
    print('The map is divided into 9 grids. The top-left corner is 1, and the bottom right is 9.')
    firstvisual()
    return xochoice


def checkend(choice1, choice2, list1, player_count):
    '''
    DOCSTRING: It checks if the game should end, depending on the current game list
    input: Player count
    output: A number - 0 if game should continue, or 1 if p1 wins, 2 if p2 wins, 3 if draw
    '''
    # horizontal wins
    for i in [1, 4, 7]:
        if choice1 == list1[i][1] and choice1 == list1[i][5] and choice1 == list1[i][-2]:
            return 1
    # vertical wins
    for j in [1, 5, -2]:
        if choice1 == list1[1][j] and choice1 == list1[4][j] and choice1 == list1[7][j]:
            return 1
    # diagonal wins
    if choice1 == list1[1][1] and choice1 == list1[4][5] and choice1 == list1[7][-2]:
        return 1
    if choice1 == list1[1][-2] and choice1 == list1[4][5] and choice1 == list1[7][1]:
        return 1
    # same stuff for p2 wins
    # horizontal wins
    for i in [1, 4, 7]:
        if choice2 == list1[i][1] and choice2 == list1[i][5] and choice2 == list1[i][-2]:
            return 2
    # vertical wins
    for j in [1, 5, -2]:
        if choice2 == list1[1][j] and choice2 == list1[4][j] and choice2 == list1[7][j]:
            return 2
    # diagonal wins
    if choice2 == list1[1][1] and choice2 == list1[4][5] and choice2 == list1[7][-2]:
        return 2
    if choice2 == list1[1][-2] and choice2 == list1[4][5] and choice2 == list1[7][1]:
        return 2
    # ended game as draw or continue
    if player_count == 10:
        return 3
    else:
        return 0


def ending(end):
    '''
    DOCSTRING: Printed statements to close the game up
    input: ending number that indicates who won, or if draw
    output: printed statements
    '''
    if end == 1:
        print("Congratulations Player 1. You have won!")
    elif end == 2:
        print("Congratulations Player 2. You have won!")
    elif end == 3:
        print("Wow. Tough fight, but well-earned draw!")


def choice_input(xochoice1):
    '''
    DOCSTRING: Simply makes clear the two choices for the two players
    input: The first chosen X/O
    output: The remaining X/O
    '''
    if xochoice1 == 'O':
        xochoice2 = 'X'
    else:
        xochoice2 = 'O'
    return xochoice2


pos_list = []


def user_input(choice1, choice2, player_count):
    '''
    DOCSTRING: a function to iterate through all turns in the game, till it's over
    input: the player one x/o choice, and a counter to check the player's turns
    output: user input of where they would like to place x/o on the map
    '''
    cheat = 0
    dict1 = {1: 'Player 1', 2: 'Player 2'}
    while cheat == 0:
        if player_count % 2 != 0:
            print(f'{dict1[1]}, Enter where (on the 1-9 map) you would like to place the {choice1}.')
            pos = int(input())
            pos_list.append(pos)
            cheat = 1
        else:
            print(f'{dict1[2]}, Enter where (on the 1-9 map) you would like to place the {choice2}.')
            pos = int(input())
            pos_list.append(pos)
            cheat = 1
        if pos in pos_list[:-1]:
            print("Tut tut. You thought you could cheat? Select another spot.")
            cheat = 0
    return pos


def play_game(choice1, choice2, player, pos, previous_list):
    '''
    DOCSTRING: A function that plays the main game by repeatedly updating the list.
    input: the x/o choice, the position of where to put x/o, and a previous list of positions
    output: horrible new list
    '''
    new_list = previous_list
    if player % 2 == 1:
        choice = choice1
    else:
        choice = choice2

    if pos in [1, 2, 3]:
        if pos == 1:
            new_list[1] = new_list[1][0] + choice + new_list[1][2:]
        elif pos == 2:
            new_list[1] = new_list[1][:5] + choice + new_list[1][6:]
        else:
            new_list[1] = new_list[1][:-2] + choice + new_list[1][-1]
    elif pos in [4, 5, 6]:
        if pos == 4:
            new_list[4] = new_list[4][0] + choice + new_list[4][2:]
        elif pos == 5:
            new_list[4] = new_list[4][:5] + choice + new_list[4][6:]
        else:
            new_list[4] = new_list[4][:-2] + choice + new_list[4][-1]
    elif pos in [7, 8, 9]:
        if pos == 7:
            new_list[7] = new_list[7][0] + choice + new_list[7][2:]
        elif pos == 8:
            new_list[7] = new_list[7][:5] + choice + new_list[7][6:]
        else:
            new_list[7] = new_list[7][:-2] + choice + new_list[7][-1]

    return new_list


# Main function positioned at the end of all code
if __name__ == "__main__":

    again = 'Y'
    while again == 'Y':
        list_visual = firstvisual()
        # defining who has X and who has O
        xochoice1 = user_introinput()
        xochoice2 = choice_input(xochoice1)
        # When player count is odd, it's Player 1's turn, else it's Player 2's turn
        player_count = 1
        # A variable that keeps track of when the game ends
        end = 0
        # Main looping code to get the game playing
        while player_count <= 10:
            pos = user_input(xochoice1, xochoice2, player_count)
            new_list = play_game(xochoice1, xochoice2, player_count, pos, list_visual)
            game_visual(new_list)
            list_visual = new_list
            player_count += 1
            end = checkend(xochoice1, xochoice2, list_visual, player_count)
            if end != 0:
                ending(end)
                break
        print("Would you like to play again? Y/N")
        again = input().upper()