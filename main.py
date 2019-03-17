import pygame
import sys
import random
import copy

pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen_width = screen_width-5
fpsControl = pygame.time.Clock()

pygame.font.init() 
font = pygame.font.SysFont('Comic Sans MS', 24)


# Image Asset
player_counter = pygame.transform.scale(pygame.image.load(".//Assets//player_counter.png"), (30, 25))
computer_counter = pygame.transform.scale(pygame.image.load(".//Assets//computer_counter.png"), (30, 25))


class app():
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        self.player_positions = [0, 0, 0, 0]

        #jail position is going to be awkward to just deal with 1 player for now
        #from go to (visiting jail - 1)
        # visiting jail to (free parking - 1)
        # from free parking to (goto jail - 1)
        # from goto jail to (go -1)
        self.board_positions = [(1390, 1000), #Go
                                               (1297, 1000), (1204, 1000), (1111, 1000), (1018, 1000), (925, 1000), (832, 1000), (739, 1000), (646, 1000), (553, 1000),
                                               (395, 950), #jail (visiting)
                                               (430, 850), (430, 764), (430, 678), (430, 592), (430, 506), (430, 420), (430, 334), (430, 248), (430, 162),
                                               (480, 76), #Free Parking
                                               (595, 70), (688, 70), (781, 70), (874, 70), (967, 70), (1060, 70), (1153, 70), (1246, 70), (1339, 70),
                                               (1432, 70), #Goto Jail
                                               (1450, 200), (1450, 286), (1450, 372), (1450, 458), (1450, 544), (1450, 630), (1450, 716), (1450, 802), (1450, 888)]
    # 115 === 93
    # 105 === 86?
        self.main()

    def main(self):
        grid = pygame.image.load(".//Assets//board.png")
        grid = pygame.transform.scale(grid, (1150, 1050))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((255,255,255))
        self.background.blit(grid, (385, 15)) #(1920 - 1150) / 2
        self.screen.blit(self.background, (0,0))


        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    if event.key == pygame.K_ESCAPE or (event.key == pygame.K_F4 and (key[pygame.K_LALT] or key[pygame.K_LALT])):
                        done = True    
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button.
                        print (event.pos)
                        #self.dice_roll(0) ### Done for now
                        self.card_animation(0,0, "community_card")
                        self.card_animation(0,0, "chance_card")
                        
            pygame.display.flip()
            fpsControl.tick(60)
        pygame.quit()
        sys.exit()

    def dice_roll(self, player):
        roll_1, roll_2 = random.randint(1, 6), random.randint(1, 6)
        total = roll_1 + roll_2
        print ("total was ", total)
        self.dice_roll_animation(roll_1, roll_2)

        self.player_animation(player, total)
        self.player_positions[player] = self.player_positions[player] + total
        

    def dice_roll_animation(self, roll_1, roll_2):
        operators = ["-", "+"]
        chosen_x_direction, chosen_y_direction  = random.choice(operators), random.choice(operators)
        displacement = random.randint(3, 10)
        x1, y1 = 960, 530
        x2, y2 = 960, 530
        counter = 0
        while counter < 30:
            x1, y1 =  x1 + int(chosen_x_direction + str(displacement)), y1 + int(chosen_y_direction + str(displacement))
            x2, y2 =  x2 - int(chosen_x_direction + str(displacement)), y2 - int(chosen_y_direction + str(displacement))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(pygame.transform.scale(pygame.image.load(".//Assets//Dice//dice_" + str(random.randint(1, 6)) + ".png"), (65, 65)), (x1, y1))
            self.screen.blit(pygame.transform.scale(pygame.image.load(".//Assets//Dice//dice_" + str(random.randint(1, 6)) + ".png"), (65, 65)), (x2, y2))
            pygame.display.update()
            counter = counter + 1
        self.screen.blit(pygame.transform.scale(pygame.image.load(".//Assets//Dice//dice_" + str(roll_1) + ".png"), (65, 65)), (x1, y1))
        self.screen.blit(pygame.transform.scale(pygame.image.load(".//Assets//Dice//dice_" + str(roll_2) + ".png"), (65, 65)), (x2, y2))
        pygame.time.wait(500) #millerseconds

    def player_animation(self, player, total):
        for x in range(self.player_positions[player], (self.player_positions[player] + total) + 1):
            pos_x, pos_y = self.board_positions[x]
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(player_counter, (pos_x, pos_y))
            pygame.display.update()
            pygame.time.wait(250)
            

    def card_animation(self, starter_x, starter_y, card):
        starter_x, starter_y = 575, 185
        displacement_x, displacement_y = (1150 - starter_x) / 50,  (740 - starter_y) / 50
        x, y = starter_x, starter_y
        counter = 0
        while counter != 22: #need a for loop to blit all player positions after background blit
            card_pic = pygame.transform.scale(pygame.image.load(".//Assets//" + card.title() + "//" + str(int(23-counter)) + ".png"), (265, 240))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(card_pic, (x, y))
            pygame.display.update()
            x = x + displacement_x
            y = y + displacement_y
            counter = counter + 1

        empty_card = pygame.transform.scale(pygame.image.load(".//Assets//" + card.title() + "//" + card + "_blank.png"), (365, 240))
        self.screen.blit(self.background, (0,0))
        self.screen.blit(empty_card, (x-50, y))

        with open(".//Assets//" + card.title() + "//" + card + " Text.txt", "r", encoding='utf8') as f:
            possible_texts = []
            for line in f:
                possible_texts.append(line.strip())
        #print (possible_texts)
        
        chosen_index = random.randint(0, 15)
        chosen_text = possible_texts[chosen_index]
        counter = 0
        splits = 0
        chosen_text_rewritten = [[], []]
        print (chosen_text)
        for char in chosen_text:
            if counter > 15:
                if char == ' ':
                    counter = 0
                    splits = splits + 1
            chosen_text_rewritten[splits].append(char)
            counter = counter + 1
        str1, str2 = "", ""
        for char in chosen_text_rewritten[0]:
            str1 = str1 + str(char)
        for char in chosen_text_rewritten[1]:
            str2 = str2 + str(char)
        self.screen.blit(font.render(str1, False, (0, 0, 0)), (x + 30, y + 50))
        self.screen.blit(font.render(str2, False, (0, 0, 0)), (x + 30, y + 100))

    
                



                             


app()
