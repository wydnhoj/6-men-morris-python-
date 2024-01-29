from FERRANCULLO_BOARD_BSCS3A import *

def pve(heuristic):
    board = []
    for i in range(16):
        board.append("*")
        
    evaluation = evaluate()
    
    print("Placing Phase")
    
    for i in range(6):
        printBoard(board)
        finished = False
        
        while not finished:
            try:
                pos = int(input("\nPlace a piece: "))
                if board[pos] == '*':
                    board[pos] = 'O'
                    
                    if isMill(pos, board):
                        itemPlaced = False
                        while not itemPlaced:
                            try:
                                pos = int(input("\n Remove a 'X' piece: "))
                                if board[pos] ==  'X' and not isMill(pos, board) or (isMill(pos, board) and numOfPieces(board, 'O') == 3):
                                    board[pos] = '*'
                                    itemPlaced = True
                                else:
                                    print("Invalid Position. Try again.")
                                    
                            except Exception as e:
                                print(str(e))
                                print("Invalid input! Try again.")
                    finished = True
                else:
                    print("A piece have been already placed in the position! Try again.")
            except Exception as e:
                print(str(e))
                print("Invalid input! Try again.")
                
        printBoard(board)
        evalBoard = minimax(board, depth, False, alpha, beta, True, heuristic)
        
        if evalBoard.evaluate == float('-inf'):
            print("You Lost!")
            sys.exit()
        else:
            board = evalBoard.board
            
    print("Moving Phase")
    while True:
        printBoard(board)
        userMoved = False
        while not userMoved:
            try:
                pos = int(input("\nMove a 'O' piece: "))
                
                while board[pos] != 'O':
                    print("Invalid. Try again.")
                    pos = int(input("\nMove a 'O' piece: "))
                    
                userPlaced = False
                
                while not userPlaced:
                    newpos = int(input("'O' New Location: "))
                    
                    if board[newpos] == '*':
                        board[pos] = '*'
                        board[newpos] = 'O'
                        
                        if isMill(newpos, board):
                            userRemoved = False
                            while not userRemoved:
                                try:
                                    pos = int(input("\nMill Formed. Remove a 'X' piece: "))
                                    
                                    if board[pos] == "X" and not isMill(pos, board) or (isMill(pos, board) and numOfPieces(board, "O") == 3):
                                        board[pos] = "*"
                                        userRemoved = True
                                    else:
                                        print("Invalid position")
                                except Exception:
                                    print("Error while accepting input")
                        userPlaced = True
                        userMoved = True
                    else:
                        print("Invalid Position. Try Again.")
                        
            except Exception as e:
                print(str(e))
                print("Invalid entry. Try again.")
                
        # if evaluateStage23(board) == float('inf'):
        #     print("You Win!")
        #     exit(0)
        
        
        # if evaluation.evaluate == float('inf'):
        #     print("You Win!")
        #     exit(0)
        
        if numOfPieces(board, 'X') < 3:
            print("You Win!")
            exit(0)
        
        printBoard(board)
        
        evaluation = minimax(board, depth, False, alpha, beta, False, heuristic)
        
        if evaluation.evaluate == float('-inf'):
            print("You Lost!")
            exit(0)
        else:
            board = evaluation.board
            
if __name__== "__main__":
    print("Player Vs AI 6 Men Morris")
    print()
    pve(potentialMillsHeuristic)