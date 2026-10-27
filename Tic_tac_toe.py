board = [" "]*9
def show():
    print(board[0],"|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
player="X"
for i in range(9):
    show()
    pos=int(input("Enter position for" + player + ", enter position (1-9); ")) -1

    if board[pos] == " ":
        board[pos] = player
    else:
        print("Position is already taken!")
        continue
    win = False
    for a,b,c, in [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]:
        if board[a] == board[b] == board[c] == player:
            win = True
    
    if win:
        show()
        print(player, "Wins!")
        break

    player="0" if player=="X"else"X"
else:
    show()
    print("It's a draw!")
