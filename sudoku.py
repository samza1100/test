from Cell import Cell
import pygame
from Board import Board
from constants import *
medium_rectangle = None
hard_rectangle = None
easy_rectangle = None
exit_rectangle = None
# for difficulty whatever the user inputs put as removed cells when creating board
def draw_menu(screen):
    global easy_rectangle
    global medium_rectangle
    global hard_rectangle
    screen = pygame.display.set_mode((900, 900))
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)
    screen.fill(ORANGE)
    title_surface = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 250))
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

def click(rect, event):
    x, y = pygame.mouse.get_pos()  # get mouse position
    if event.type == pygame.MOUSEBUTTONDOWN:  # look for mouse click event
        if pygame.mouse.get_pressed()[0]:  # check that mouse 1 (left click) is pressed - this event is called for mouse click and mouse unclick
            if rect.collidepoint(x, y):  # check that mouse click is within this rectangle
                return True
    return False

def winning_screen(screen): #appear when you won the game
    global exit_rectangle
    screen = pygame.display.set_mode((900, 900))
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)
    screen.fill(ORANGE)
    title_surface = start_title_font.render("Game Won", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)
    exit_text = button_font.render("Exit", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(exit_surface, exit_rectangle)

def losing_screen(screen): # appear when lost the game
    global exit_rectangle
    screen = pygame.display.set_mode((900, 900))
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)
    screen.fill(ORANGE)
    title_surface = start_title_font.render("Game Over", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)
    exit_text = button_font.render("Exit", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(exit_surface, exit_rectangle)

def GetKeyNumber(event): # set each key to number1-9
    match event.key:
        case pygame.K_0:
            return 0
        case pygame.K_1:
            return 1
        case pygame.K_2:
            return 2
        case pygame.K_3:
            return 3
        case pygame.K_4:
            return 4
        case pygame.K_5:
            return 5
        case pygame.K_6:
            return 6
        case pygame.K_7:
            return 7
        case pygame.K_8:
            return 8
        case pygame.K_9:
            return 9
        case _:                # not a number key, return None
            return None

def main():
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((900, 900))
    screen.fill(ORANGE)
    draw_menu(screen)
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            else:
                if click(easy_rectangle, event): # Easy difficulty
                    var = Board(900, 900, screen, 30)
                    screen.fill(ORANGE)
                    finished = True
                    break
                elif click(medium_rectangle, event): # Medium difficulty
                    var = Board(900, 900, screen, 40)
                    screen.fill(ORANGE)
                    finished = True
                    break
                elif click(hard_rectangle, event): # Hard difficulty
                    var = Board(900, 900, screen, 50)
                    screen.fill(ORANGE)
                    finished = True
                    break
        pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()  # get mouse position
                    row,col = var.click(x,y)
                    var.select(row,col)
            elif event.type == pygame.KEYDOWN:
                num = GetKeyNumber(event)
                if num == None:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        var.place_skectchedvalue()
                    if event.key == pygame.K_UP:
                        new_row = var.selected_row-1
                        if new_row >= 0:
                            var.select(new_row, var.selected_col)
                    if event.key == pygame.K_DOWN:
                        new_row = var.selected_row+1
                        if new_row <= 8:
                            var.select(new_row, var.selected_col)
                    if event.key == pygame.K_RIGHT:
                        new_col = var.selected_col+1
                        if new_col <= 8:
                            var.select(var.selected_row, new_col)
                    if event.key == pygame.K_LEFT:
                        new_col = var.selected_col-1
                        if new_col >= 0:
                            var.select(var.selected_row, new_col)
                    if event.key == pygame.K_BACKSPACE:
                        var.clear()
                    else:
                        continue
                var.sketch(num)
        screen = pygame.display.set_mode((900, 900))
        screen.fill(ORANGE)
        var.draw()
        if var.is_full():
            if var.check_board():
                winning_screen(screen)
                pygame.display.update()
                break
            else:
                losing_screen(screen)
                pygame.display.update()
                break
        pygame.display.update()
    while True:
        for event in pygame.event.get(): #click to exit the game
            if event.type == pygame.QUIT:
                pygame.quit()
            else:
                if click(exit_rectangle, event):
                    main()
                    #pygame.quit()



if __name__ == "__main__":
    main()



