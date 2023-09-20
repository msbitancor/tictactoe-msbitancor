import pygame

# Check if cell is occupied
def occupied(board, row, col):
    if board[row][col] == '':
        return True
    else:
        return False

# For making a move
def move(board, letter, row, col):

    # Check if not occupied, then insert move to cell
    if occupied(board, row, col):
        board[row][col] = letter


# Check winning condition
def winning_condition(board):

    # Horizontal
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != '':
        return True
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != '':
        return True
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != '':
        return True

    # Vertical
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != '':
        return True
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != '':
        return True
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != '':
        return True
    
    # Diagonal
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '':
        return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != '':
        return True
    
    return False

# Check which piece will get the win
def check_piece_win(board, piece):
    # Horizontal
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] == piece:
        return True
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] == piece:
        return True
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] == piece:
        return True

    # Vertical
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == piece:
        return True
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == piece:
        return True
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == piece:
        return True
    
    # Diagonal
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == piece:
        return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == piece:
        return True
    
    return False

# Check if draw
def draw(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == ''):
                return False
    return True

# Player move
def player_move(board, ai, player, row, col, turn):

    # Insert piece to cell if not yet occupied and increment turn counter
    if occupied(board, row, col):
        move(board, player, row, col)
        turn +=1

        # AI moves if game is not yet draw
        if draw(board) != True:
            ai_move(board, ai, player, turn)

# AI move
def ai_move(board, ai, player, turn):

    best_score = -1000
    best_move = 0

    # Do minmax
    for r in range(len(board)):
        for c in range(len(board[r])):
            if (board[r][c] == ''):

                # Do the move in the board if unoccupied
                board[r][c] = ai

                # Check the score
                score = minmax(board, 0, ai, player, False)

                # Turn it back into unoccupied
                board[r][c] = ''

                # Check if score is better and if it is, get the row and column and pass value to best_score
                if (score > best_score):
                    best_score = score
                    best_move = [r, c]
    
    # Insert piece to best cell and increment turn counter
    move(board, ai, best_move[0], best_move[1])
    turn += 1

# Minmax Algorithm
def minmax(board, depth, ai, player, max):

    # AI wins
    if check_piece_win(board, ai):
        return 1

    # Player wins
    elif check_piece_win(board, player):
        return -1
    
    # Draw 
    elif (draw(board)):
        return 0

    # Maximizer statement
    if max:
        best_score = -1000
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == ''):
                    board[i][j] = ai
                    score = minmax(board, depth + 1, ai, player, False)
                    board[i][j] = ''
                    if (score > best_score):
                        best_score = score
        return best_score

    # Minimizer statement
    else:
        best_score = 1000
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == ''):
                    board[i][j] = player
                    score = minmax(board, depth + 1, ai, player, True)
                    board[i][j] = ''
                    if (score < best_score):
                        best_score = score
        return best_score

# For creating new board
def new_board():
    board = [['','',''],['','',''],['','','']]
    return board

pygame.init()

#Window, Name, Screen Size, Font Style, and Initialization of board, respectively
pygame.display.set_caption("TicTacToe")
screen = pygame.display.set_mode((420, 800))
myFont = pygame.font.SysFont("Arial", 20)

# Initial state of board
board = [['','',''],['','',''],['','','']]

running = True

#Grid Dimensions
w = 120
h = 120
m = 5

#Grid Location
gridpos_x = 20
gridpos_y = 75

# Initialize Player and AI
player = ''
ai = ''

# Initialize state of buttons and ai_first to false
X_button_show = True
O_button_show = True
exit_button_show = True
yes_button_show = False
no_button_show = False
ai_first = False

# Main game
while running == True:
    screen.fill((255,255,255))

    # For showing options (X, O, and Exit, respectively)
    if X_button_show == True:
        select = myFont.render("Select your piece", 1, (0,0,0))
        X_button = myFont.render("X", 1, (0,0,0))
        X_rect = pygame.draw.rect(screen, (135,206,250), pygame.Rect(50, 500, 60, 40))
        screen.blit(select, (150, 465))
        screen.blit(X_button, (73, 510))
    if O_button_show == True:
        O_button = myFont.render("O", 1, (0,0,0))
        O_rect = pygame.draw.rect(screen, (135,206,250), pygame.Rect(180, 500, 60, 40))
        screen.blit(O_button, (203, 510))
    if exit_button_show == True:
        e_button = myFont.render("Exit", 1, (0,0,0))
        e_rect = pygame.draw.rect(screen, (135,206,250), pygame.Rect(310, 500, 60, 40))
        screen.blit(e_button, (325, 510))

    # Option to choose whether player wants to go first or not
    if yes_button_show == True:
        play = myFont.render("Do you want to play first?", 1, (0,0,0))
        yes_button = myFont.render("Yes", 1, (0,0,0))
        yes_rect = pygame.draw.rect(screen, (135,206,250), pygame.Rect(50, 500, 60, 40))
        screen.blit(play, (120, 465))
        screen.blit(yes_button, (65, 510))
    if no_button_show == True:
        no_button = myFont.render("No", 1, (0,0,0))
        no_rect = pygame.draw.rect(screen, (135,206,250), pygame.Rect(180, 500, 60, 40))
        screen.blit(no_button, (200, 510))
    
    #Number positioning of tiles for y-axis
    y = 50 + gridpos_y

    for row in range(3):
        
        #Number positioning of tiles for x-axis
        x = 55 + gridpos_x

        for col in range(3):
            num_value = board[row][col]

            #For placing tiles in the screen using rectangle object
            rect = ((m + w) * col+gridpos_x + m, (m + h) * row+gridpos_y + m, w, h)
  
            num_view = myFont.render(str(num_value), 1, (0,0,0))
            pygame.draw.rect(screen, (135,206,250), rect)
            
            #View number inside tile with positioning
            screen.blit(num_view, (x+10,y+10))
            x += w
        y += h
    
    # If AI is X, ai moves first and turn ai_first to False
    if ai_first:
        ai_move(board, ai, player, turn)
        ai_first = False

    # If winning condition, print winner based on what turn it is
    if winning_condition(board):

        # Player wins if turn is odd
        if turn %2 == 1:
            alert = myFont.render("Player wins!", 1, (0,0,0))
            screen.blit(alert, (160, 50))
        
        # AI wins if turn is even
        else:
            alert = myFont.render("AI wins!", 1, (0,0,0))
            screen.blit(alert, (180, 50))

        # Show options again afterwards
        X_button_show = True
        O_button_show = True
        exit_button_show = True

    # Print this if draw game
    if draw(board):
        alert = myFont.render("Draw game!", 1, (0,0,0))
        screen.blit(alert, (160, 50))

        # Show options again afterwards
        X_button_show = True
        O_button_show = True
        exit_button_show = True
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Get mouse click position
            pos = pygame.mouse.get_pos()
            
            # Player chooses X
            if X_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and X_button_show == True:
                board = [['','',''],['','',''],['','','']]
                player = 'X'
                ai = 'O'
                X_button_show = False
                O_button_show = False
                exit_button_show = False
                yes_button_show = True
                no_button_show = True

            # Player chooses O
            elif O_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and O_button_show == True:
                board = [['','',''],['','',''],['','','']]
                player = 'O'
                ai = 'X'
                X_button_show = False
                O_button_show = False
                exit_button_show = False
                yes_button_show = True
                no_button_show = True
            
            # Player chooses Exit
            elif e_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and exit_button_show == True:
                running = False

            # Player wants to go first
            elif yes_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and yes_button_show == True:
                turn = 0
                yes_button_show = False
                no_button_show = False

            # Player wants to go second
            elif no_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and no_button_show == True:
                turn = 0
                ai_first = True
                yes_button_show = False
                no_button_show = False

            # Player clicks on cell
            else:

                # Can only click if player has chosen a piece
                if X_button_show == False:

                    # Convert coordinates to index
                    column = pos[0] // (w + m + gridpos_x - 20)              
                    row = pos[1] // (h + m + gridpos_y - 50)

                    # Player can move if row and column is valid
                    if row < 3 and row > -1 and column < 3 and column > -1:
                        player_move(board, ai, player, row, column, turn)
                 
    
    pygame.display.update()

pygame.quit()