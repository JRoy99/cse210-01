# Name: James Roy
# Assignment: W01 Prove; Tic-Tac-Toe


def drawBoard(board_array):
    for i in range(0, 2):
        print(board_array[i])
        if i < 2:
            print("|")


def main():
    game_over = False
    board_array = [1, 2, 3,
                    4, 5, 6,
                    7, 8, 9]
    print(board_array)
    drawBoard(board_array)

if __name__ == "__main__":
    main()
