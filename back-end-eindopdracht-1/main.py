# Boter Kaas en Eieren eindopdracht back-end

# Het spelbord
board = [0,0,0,
         0,0,0,
         0,0,0]

# Het bord laten zien met een mooie stijl dat er 3 naast elkaar staan net als op papier
def show_board(list):
    bord = ""
    count = 0
    for place in list:
        if count == 3:
            count = 0
            bord += f"\n{str(place)} " # Moet een f-string zijn om de spatie ertussen te krijgen
        else:
            bord += str(f"{place} ") # zelfde hier

        count += 1

    print('-' * len(bord)) # mooie decoratie
    print(bord)

player0 = 'X'
player1 = 'O'

turn = 0

# player_1 heeft de beurt
def player_1():
    available = [] # nieuw lijste voor de beschikbare plaatsen
    for i, place in enumerate(board):
        if place == 0:
            available.append(i + 1)
        else:
            available.append('-')

    show_board(available) # dan kan je de beschikbare plaatsen weer mooi laten zien

    print("Turn: player_1")
    choice = input("Select a position: ")

    # de try zorgt ervoor dat er wel een input is gegeven, het een int is en tussen de 1 en 9 zit
    try:
        if choice:
            choice = int(choice)
            if choice > len(board) or choice < 1:
                raise ValueError
            choice -= 1 # for the index
        else: 
            raise ValueError
    except(ValueError):
        print("Not a valid choice! Skipping turn...")
        return

    # Hier kijkt 'ie of de plaats wel leeg is en zo niet dan slaat die de beurt over
    if board[choice] == 0:
        if board[choice] != player0 and board[choice] != player1:
            board[choice] = player0 # type: ignore

    else:
        print("Invalid choice, skipping turn...")

# zelfde hier kijk bij player_1()
def player_2():
    available = []
    for i, place in enumerate(board):
        if place == 0:
            available.append(i + 1)
        else:
            available.append('-')

    show_board(available)

    print("Turn: player_2")
    choice = input("Select a position: ")
    try:
        if choice:
            choice = int(choice)
            if choice > len(board) or choice < 1:
                raise ValueError
            choice -= 1 # for the index
        else: 
            raise ValueError

    except(ValueError):
        print("Not a valid choice! Skipping turn...")
        return

    if board[choice] == 0:
        if board[choice] != player0 and board[choice] != player1:
            board[choice] = player1 # type: ignore

    else:
        print("Invalid choice, skipping turn...")

# Kijken of er een winnaar is elke beurt
def check_winner():
    # alle mogelijke win posities (door chatgpt laten maken)
    winning_lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    # hier doet die dus per lijst in de winning_lines de 0,1,2 in a,b,c en dan kijkt die of a niet leeg is anders is alles leeg en dan is dat allemaal gelijk dus dan telt die dat als een win. Dan returned die de winnaar.
    for a,b,c in winning_lines:
        if board[a] != 0 and board[a] == board[b] == board[c]:
            return board[a]

    return None

# best wel simpel gewoon kijken of er geen nullen meer in board zit en zo ja een True returnen die in de main while loop word gechecked
def check_tie(board):
    return 0 not in board

# de main loop
running = True
while running:
    # elke beurt het spelbord laten zien
    show_board(board)

    # kijken wie de beurt heeft en dan ook de beurt wisselen en de functies aanroepen
    if turn == 0:
        player_1()
        turn = 1
    elif turn == 1:
        player_2()
        turn = 0

    # winner is gelijk aan of 'X' of 'O' en dus kan die checken wie de winnaar is en als je running = False doet dan stopt het spel
    winner = check_winner()
    if winner == player0:
        print("player_1 HAS WON!")
        running = False
        
    elif winner == player1:
        print("player_2 HAS WON!")
        running = False

    elif check_tie(board): # hier kijkt die of het gelijk spel is of niet en zet dan ook weer running naar False wat het spel stopt
        print("IT'S A TIE!")
        running = False