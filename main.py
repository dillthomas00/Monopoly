import pygame
import sys
import random
import copy

pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen_width, screen_height = screen_width-5, screen_height-75
fpsControl = pygame.time.Clock()

# Image Asset
player_counter = pygame.image.load(".//Assets//player_counter.png")
player_counter = pygame.transform.scale(player_counter, (80, 75))
computer_counter = pygame.image.load(".//Assets//computer_counter.png")
computer_counter = pygame.transform.scale(computer_counter, (80, 75))


class app():
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.main()

    def main(self):
        grid = pygame.image.load(".//Assets//board.png")
        grid = pygame.transform.scale(grid, (1150, 950))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((255,255,255))
        self.background.blit(grid, (385, 25)) #(1920 - 1150) / 2
        
        #back_button  = pygame.image.load(".//Assets//back_button.png")
        #pygame.transform.scale(back_button, (400, 100))
        #self.background.blit(back_button, (790, 910))
        self.screen.blit(self.background, (0,0))

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button.
                        print (event.pos)
                        self.dice_roll()
                        
            pygame.display.flip()
            fpsControl.tick(60)
        pygame.quit()
        sys.exit()

    def dice_roll(self):
        self.dice_roll_animation()
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print (dice1, " : ", dice2)
        total = dice1 + dice2

    def dice_roll_animation(self):
        operators = ["-", "+"]
        chosen_x_direction = random.choice(operators)
        chosen_y_direction = random.choice(operators)
        displacement = random.randint(5, 10)

        x1 = 960
        y1 = 530
        x2 = 960
        y2 = 530
        counter = 0
        while counter < 30:
            x1 = x1 + int(chosen_x_direction + str(displacement))
            y1 = y1 + int(chosen_y_direction + str(displacement))

            x2 = x2 - int(chosen_x_direction + str(displacement))
            y2 = y2 - int(chosen_y_direction + str(displacement))

            dice_1 = pygame.image.load(".//Assets//Dice//dice_" + str(random.randint(1, 6)) + ".png")
            dice_1 = pygame.transform.scale(dice_1, (60, 60))

            dice_2 = pygame.image.load(".//Assets//Dice//dice_" + str(random.randint(1, 6)) + ".png")
            dice_2 = pygame.transform.scale(dice_2, (60, 60))

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(dice_1, (x1, y1))
            self.screen.blit(dice_2, (x2, y2))

            pygame.display.update()
            counter = counter + 1


app()
