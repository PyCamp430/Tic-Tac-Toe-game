# Tic Tac Toe game

import time
import view, model

def play_loop():
    while(True):     
        # Enter the row number and column number where the player wants the move
        x1 = view.turn_player1_row()
        if x1 == "Exit" or x1 == "exit":
            return "GAME exited"
        y1 = view.turn_player1_col()
        if y1 == "Exit" or y1 == "exit":
            return "GAME exited" 
        # check for the winner, display the winner and end the game
        result = model.check_win(game)
        if result != 3:
            return view.win_message(result)
        # check if the game is a draw
        count = model.game_draw(game)
        if count == 9:
            return view.draw_message()
        while (model.check_move(game, x1, y1) == False):
            print("Not a valid move")
            x1 = view.turn_player1_row()
            if x1 == "Exit" or x1 == "exit":
                return "GAME exited"
            y1 = view.turn_player1_col()
            if y1 == "Exit" or y1 == "exit":
                return "GAME exited" 
        value = 1
        # place the move entered by the player in the game array
        model.add_value(game, int(x1)-1, int(y1)-1, value)
        result = model.check_win(game)
        if result != 3:
            return view.win_message(result)
        count = model.game_draw(game)
        if count == 9:
            return view.draw_message()
        x2 = view.turn_player2_row()
        if x2 == "Exit" or x2 == "exit":
            return "GAME exited"
        y2 = view.turn_player2_col()
        if y2 == "Exit" or y2 == "exit":
            return "GAME exited"
        result = model.check_win(game)
        if result != 3:
            return view.win_message(result)
        count = model.game_draw(game)
        if count == 9:
            return view.draw_message()
        while (model.check_move(game, x2, y2) == False):
            print("Not a valid move")
            x2 = view.turn_player2_row()
            if x2 == "Exit" or x2 == "exit":
                return "GAME exited"
            y2 = view.turn_player2_col()
            if y2 == "Exit" or y2 == "exit":
                return "GAME exited"
        value = 2
        model.add_value(game, int(x2)-1, int(y2)-1, value)
        result = model.check_win(game)
        if result != 3:
            return view.win_message(result)
        count = model.game_draw(game)
        if count == 9:
            return view.draw_message()
        
        
if __name__ == "__main__":
    view.welcome_message()
    time.sleep(8)
    choice = view.ask_user()
    if choice == "Yes" or choice == "yes":
        game = model.draw_game()
        model.display_board(game)
        print(play_loop())
    else:
        pass




