# minor bug fixes
# runs faster

import pygame, time
import backend as bk

pygame.init()

white = (255, 255, 255)

scheme_count = 1

dW = 670
dH = 190

clear_icon = pygame.image.load('icon.png')

cDisplay = pygame.display.set_mode((dW, dH))
pygame.display.set_caption('Live Coronavirus Updates')
pygame.display.set_icon(clear_icon)

clock = pygame.time.Clock()


def text_objects(text, font, c):  # render the text
    text_surface = font.render(text, True, c)
    return text_surface, text_surface.get_rect()


def message_display(text, size, color=(0, 0, 0), coordinates=(dW // 2, dH//2)):
    large_text = pygame.font.Font('freesansbold.ttf', size)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = (coordinates[0], coordinates[1])
    cDisplay.blit(text_surf, text_rect)


def print_total():
    global cDisplay
    cases, deaths, recoveries = bk.data_return()
    message_display('Global Cases: ' + cases, 40, (0, 0, 0), (dW//2, dH//2 - 50))
    message_display('Global Deaths: ' + deaths, 40, (0, 0, 0))
    message_display('Global Recoveries: ' + recoveries, 40, (0, 0, 0), (dW//2, dH//2 + 50))


def wait(num=60):
    time_rn = time.time()
    while time.time() - time_rn <= num:
        for event_ in pygame.event.get():
            if event_.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event_.type == pygame.KEYDOWN:
                if event_.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


def update():
    global scheme_count
    global cDisplay
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        cDisplay.fill(white)
        print_total()

        pygame.display.flip()

        wait()

        clock.tick(60)


update()