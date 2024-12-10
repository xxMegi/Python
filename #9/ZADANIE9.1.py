import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SNOWFLAKE_RADIUS = 20
SNOWFLAKE_SPEED = 2
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ZIMA!")

white = (255, 255, 255)
purple = (128, 0, 128)
pink = (255, 105, 180)

snowdrift_height = 0
SNOWDRIFT_INCREMENT = 10

def_font = pygame.font.Font(None, 72)
snowflakes = []

def draw_snow():
    for snowflake in snowflakes:
        pygame.draw.circle(screen, white, (snowflake[0], snowflake[1]), SNOWFLAKE_RADIUS)

def add_snow():
    x = random.randint(0, SCREEN_WIDTH - SNOWFLAKE_RADIUS * 2)
    y = 0 
    snowflakes.append([x, y])

def move_snow():
    global snowdrift_height
    for snowflake in snowflakes[:]:
        snowflake[1] += SNOWFLAKE_SPEED
        if snowflake[1] > SCREEN_HEIGHT:
            snowflakes.remove(snowflake)
            snowdrift_height += SNOWDRIFT_INCREMENT

def check_snow_click(pos):
    for snowflake in snowflakes[:]:
        if (snowflake[0] - pos[0])**2 + (snowflake[1] - pos[1])**2 <= SNOWFLAKE_RADIUS**2:
            snowflakes.remove(snowflake)
            return True
    return False



def main():
    global snowdrift_height
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(purple)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                check_snow_click(event.pos)

        if random.randint(1, 25) == 1:  
            add_snow()

        move_snow()
        draw_snow()

        if snowdrift_height > 0:
            pygame.draw.rect(screen, white, (0, SCREEN_HEIGHT - snowdrift_height, SCREEN_WIDTH, snowdrift_height))

        if snowdrift_height >= SCREEN_HEIGHT:
            game_over_text = def_font.render("GAME OVER!!!", True, pink)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    main()