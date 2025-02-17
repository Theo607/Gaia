import pygame

# Initialize pygame
pygame.init()

# Set up display
(screenWidth, screenHeight) = (900, 900)
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
Grid = [[0 for _ in range(3)] for _ in range(3)]  # 3x3 grid initialized with 0
current_player = 1  # 1 for X, -1 for O

# Draw the grid lines


def drawGrid():
    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (300 * i, 0), (300 * i, 900), 3)
        pygame.draw.line(screen, WHITE, (0, 300 * i), (900, 300 * i), 3)

# Draw X at the given grid position


def drawX(gridPosX, gridPosY):
    pygame.draw.line(screen, WHITE, (gridPosX * 300 + 50, gridPosY * 300 + 50),
                     (gridPosX * 300 + 250, gridPosY * 300 + 250), 5)
    pygame.draw.line(screen, WHITE, (gridPosX * 300 + 250, gridPosY * 300 + 50),
                     (gridPosX * 300 + 50, gridPosY * 300 + 250), 5)

# Draw O at the given grid position


def drawO(gridPosX, gridPosY):
    pygame.draw.circle(screen, WHITE, (gridPosX * 300 +
                       150, gridPosY * 300 + 150), 100, 5)


def checkRow(position):
    val = Grid[position][0]
    if val == 0:
        return 0
    if val == Grid[position][1] and val == Grid[position][2] and val:
        return val
    return 0


def checkCol(position):
    val = Grid[0][position]
    if val == 0:
        return 0
    if val == Grid[1][position] and val == Grid[2][position]:
        return val
    return 0


def checkDiag():
    val = Grid[0][0]
    if val == Grid[1][1] and val == Grid[2][2] and val != 0:
        return val
    val = Grid[2][0]
    if val == Grid[1][1] and val == Grid[0][2] and val != 0:
        return val
    return 0


def checkZero():
    for y in range(0, 3):
        for x in range(0, 3):
            if Grid[y][x] == 0:
                return 1
    return 0


def checkWin():
    for i in range(0, 3):
        if checkRow(i) == 1 or checkRow(i) == -1:
            return checkRow(i)
        if checkCol(i) == 1 or checkCol(i) == -1:
            return checkCol(i)
    if checkDiag() == 1 or checkDiag() == -1:
        return checkDiag()
    if checkZero() == 1:
        return 0
    return -2


def writeWin(playerWon):
    screen.fill(BLACK)
    font = pygame.font.Font(None, 80)

    if playerWon == 1:
        message = "Player X Wins!"
    elif playerWon == -1:
        message = "Player O Wins!"
    else:
        message = "It's a Tie!"

    text_surface = font.render(message, True, WHITE)
    text_rect = text_surface.get_rect(
        center=(screenWidth // 2, screenHeight // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()


# Main loop
running = True
while running:
    screen.fill(BLACK)
    drawGrid()

    # Draw existing Xs and Os based on grid
    for row in range(3):
        for col in range(3):
            if Grid[row][col] == 1:
                drawX(col, row)
            elif Grid[row][col] == -1:
                drawO(col, row)
    if checkWin() != 0:
        writeWin(checkWin())
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:  # Any key press
                    waiting = False  # Exit loop
        for y in range(0, 3):
            for x in range(0, 3):
                Grid[y][x] = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
            x, y = pygame.mouse.get_pos()
            grid_x = x // 300
            grid_y = y // 300
            # Check if the spot is empty
            if Grid[grid_y][grid_x] == 0:
                Grid[grid_y][grid_x] = current_player
                current_player *= -1  # Switch turns

    pygame.display.flip()

pygame.quit()
