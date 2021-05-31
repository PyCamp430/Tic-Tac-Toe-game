# create a 3 by 3 array for the game, using datatype "list"
def draw_game():
    return  [[0, 0, 0] for i in range(3)]

# create the board to display to the user
def display_board(game):
    dict = {0: "___", 1: "_X_", 2: "_O_"}
    print("     1   2   3 ")
    print("    ___ ___ ___ ")
    for rows in range(3):
        new_row = []
        new_row.append(f" {str(rows+1)} ")
        for columns in range(3):
            new_row.append(dict[game[rows][columns]])
        print("|".join(new_row) + "|")

# add the move entered by the player in the game array and display the updated game board
def add_value(game, row, column, value):
    game[row][column] = value
    display_board(game) 

# check whether the move is valid or not
def check_move(game, x, y):
    try:
        if int(x) < 1 or int(x) > 3:
            return False
        elif int(y) < 1 or int(y) > 3:
            return False
        elif game[int(x)-1][int(y)-1] != 0:
            return False
        else:
            return True
    except:
        return False

# check the condition for the win
def check_win(game):
    if ((game[0][0] == 1 and game[1][1] == 1 and game[2][2] == 1) or (game[0][2] == 1 and game[1][1] == 1 and game[2][0] == 1)):
        return 1
        
    if((game[0][0] == 2 and game[1][1] == 2 and game[2][2] == 2) or (game[0][2] == 2 and game[1][1] == 2 and game[2][0] == 2)):
        return 2
        
    for i in range(3):
        if ((game[i][0] == 1 and game[i][1] == 1 and game[i][2] == 1) or (game[0][i] == 1 and game[1][i] == 1 and game[2][i] == 1)):
            return 1
                    
    for i in range(3):
        if ((game[i][0] == 2 and game[i][1] == 2 and game[i][2] == 2) or (game[0][i] == 2 and game[1][i] == 2 and game[2][i] == 2)):
            return 2
    else:
        return 3

# check if the game is a draw between the two players
def game_draw(game):
    count = 0
    for i in range(3):
        for j in range(3):
            if game[i][j] != 0:
                    count += 1
    return count


