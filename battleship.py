from random import randint

#pre-set
board = []



for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)



print "Let's play Battleship!"
print_board(board)


#generating shpis
ship_row = random_row(board)
ship_col = random_col(board)



#cheat
print "Cheat:"
print ship_row+1
print ship_col+1
print


#Loop for guessing and conditional checks
turn = 0
for turn in range(4):

    print "Turn %s" % (turn+1)
    guess_row = int(raw_input("Guess Row:"))-1
    guess_col = int(raw_input("Guess Col:"))-1

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        
    turn +=1
    if turn == 3:
        print
        print "Game Over"
        break
    print
    print_board(board)







#add-ons: multiple ships, two player, bigger board?