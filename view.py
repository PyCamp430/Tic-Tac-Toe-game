def welcome_message():
    print('''
    Welcome to the 'Tic Tac Toe' game! 
    The game consisits of two players: Player1 and Player2.
    Player1 plays as "O" and Player2 plays as "X". The player who suceeds in placing three of their 
    marks in a diagonal, horizontal or vertical row, first, is the winner. Enjoy!''')

def ask_user():
    choice = input("Enter 'Yes' to start the game and 'Exit' to exit the game: ")
    return choice

def turn_player1_row():
    x1 = input("Player 1, enter row: ")
    return x1

def turn_player1_col():
    y1 = input("Player 1, enter column: ")
    return y1

def turn_player2_row():
    x2 = input("Player 2, enter row: ")
    return x2

def turn_player2_col():
    y2 = input("Player 2, enter column: ")
    return y2

def win_message(result):
    print("GAME OVER!")
    return f"CONGRATULATIONS!! WINNER IS PLAYER {result}"
    
def draw_message():
    return "**GAME DRAW! NO WINNER.**"
