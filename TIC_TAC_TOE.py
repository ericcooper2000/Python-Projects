import time as tm


def get_valid_choice(prompt, choices):
    while True:
        choice = input(prompt)
        if choice.upper() in choices:
            return choice.upper()
        else:
            print(f"Please enter one of {choices}")


def game_board(position_in):
    board = "  ---  ---   --- \n" \
            f"| {position_in["R1C1"]}  |  {position_in["R1C2"]}  |  {position_in["R1C3"]}  |\n" \
            "  ---  ---   --- \n" \
            f"| {position_in["R2C1"]}  |  {position_in["R2C2"]}  |  {position_in["R2C3"]}  |\n" \
            "  ---  ---   --- \n" \
            f"| {position_in["R3C1"]}  |  {position_in["R3C2"]}  |  {position_in["R3C3"]}  |\n" \
            "  ---  ---   --- "
    return board


def intro():
    print("Welcome to tic tac toe!")
    tm.sleep(2)
    print("You will input answers in a 'rowcolumn (R1C2)' format")
    tm.sleep(2)
    print("Player1 will be 'X' and Player 2 will be 'O'")
    tm.sleep(2)
    input("Press any button to start....")


def tictac():
    positions = {"R1C1": 0, "R1C2": 0, "R1C3": 0,
                 "R2C1": 0, "R2C2": 0, "R2C3": 0,
                 "R3C1": 0, "R3C2": 0, "R3C3": 0}
    positions_list = ["R1C1", "R1C2", "R1C3", "R2C1", "R2C2",
                      "R2C3", "R3C1", "R3C2", "R3C3"]

    while True:
        # Player one chooses row and column
        while True:
            player1 = get_valid_choice("Player 1, choose your row and column:  ",
                                       positions_list)
            if 0 != positions[player1]:
                print("Spot is taken choose another location")
            if 0 == positions[player1]:
                positions[player1] = "x"
                # prints board to terminal after P1 input position
                print(game_board(positions))
                break
        if game_checker(positions) == "Player One Wins":
            print(game_checker(positions))
            break
        # Checks to see if there is any more moves left
        game_conclusion = 0
        for value in positions.values():
            if 0 != value:
                game_conclusion += 1
                if game_conclusion == 9:
                    return print("No more moves, Tie!")
            if 0 == value:
                pass

        # Player two chooses row and column
        while True:
            player2 = get_valid_choice("Player 2, choose your row and column:  ",
                                       positions_list)
            if 0 != positions[player2]:
                print("Spot is taken choose another location")
            if 0 == positions[player2]:
                positions[player2] = "o"
                print(game_board(positions))
                break
        if game_checker(positions) == "Player Two Wins":
            print(game_checker(positions))
            break


def game_checker(game_results):
    # Player one
    list_number = [1, 2, 3]
    for n in list_number:
        # Horizontal
        if game_results[f"R{n}C1"] == "x" \
            and game_results[f"R{n}C2"] == "x" \
                and game_results[f"R{n}C3"] == "x":
            return "Player One Wins"
        # Vertical
        if game_results[f"R1C{n}"] == "x" \
            and game_results[f"R2C{n}"] == "x" \
                and game_results[f"R3C{n}"] == "x":
            return "Player One Wins"
    # Angled
    if game_results["R1C1"] == "x" \
        and game_results["R2C2"] == "x" \
            and game_results["R3C3"] == "x":
        return "Player One Wins"
    if game_results["R3C1"] == "x" \
        and game_results["R2C2"] == "x" \
            and game_results["R1C3"] == "x":
        return "Player One Wins"

    # Player Two
    for n in list_number:
        # Horizontal
        if game_results[f"R{n}C1"] == "o" \
            and game_results[f"R{n}C2"] == "o" \
                and game_results[f"R{n}C3"] == "o":
            return "Player Two Wins"
        # Vertical
        if game_results[f"R1C{n}"] == "o" \
            and game_results[f"R2C{n}"] == "o" \
                and game_results[f"R3C{n}"] == "o":
            return "Player Two Wins"
    # Angled
    if game_results["R1C1"] == "o" \
        and game_results["R2C2"] == "o" \
            and game_results["R3C3"] == "o":
        return "Player Two Wins"
    if game_results["R3C1"] == "o" \
        and game_results["R2C2"] == "o" \
            and game_results["R1C3"] == "o":
        return "Player Two Wins"


def final():
    intro()
    tictac()


if __name__ == '__main__':
    final()
