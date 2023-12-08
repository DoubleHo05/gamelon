import pygame
from Settings import *
from sys import exit

#components
from Game import Game

class runGame():

    def __init__(self):

        # general
        pygame.init()
        pygame.display.set_caption('US88')
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        # components
        self.game = Game()
        self.state = False

        # Data for next feature
        self.cars_name = []
        
      

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    self.game.mouse_sound.play()

                    # Choose your map
                    if self.game.chose_map == False:
                        for i in range(MAPS):
                            if self.game.maps_rect_list[i].collidepoint(event.pos):
                                self.game.map = i + 1

                    # Choose your car
                    if self.game.chose_car == False:
                        for j in range(len(self.game.cars_rect_list)):
                            if self.game.cars_rect_list[j].collidepoint(event.pos):
                                self.game.car = j + 1

                    # Choose your bet money
                    if self.game.chose_coin == False:
                        for k in range(len(self.game.coins_rect_list)):
                            if self.game.coins_rect_list[k].collidepoint(event.pos):
                                self.game.coin = (k + 1) * 1000

                if event.type == pygame.KEYDOWN:

                    self.game.enter = True

                    # Input name for each car
                    if self.game.chose_car and self.game.changed_opponents == False:
                        
                        if event.key == pygame.K_BACKSPACE and len(self.game.cars_name_list[self.game.current_opponent]) >= 10:
                            self.game.cars_name_list[self.game.current_opponent] = self.game.cars_name_list[self.game.current_opponent][:-1]

                        elif event.key == pygame.K_RETURN and self.game.enter:
                            self.game.cars_name_list[self.game.current_opponent] = self.game.cars_name_list[self.game.current_opponent][9:]
                                                         
                            if len(self.game.cars_name_list[self.game.current_opponent]) == 0:
                                self.game.cars_name_list[self.game.current_opponent] = choice(self.game.Name)
                                self.game.Name.remove(self.game.cars_name_list[self.game.current_opponent])

                            self.game.name_x += (GAME_WIDTH - 280) / (CARS - 1)

                            self.game.current_opponent += 1

                            self.game.enter = False

                            if self.game.current_opponent == CARS:
                                self.game.changed_opponents = True

                        elif len(self.game.cars_name_list[self.game.current_opponent]) < 22:
                            self.game.cars_name_list[self.game.current_opponent] += event.unicode

                    if self.game.changed_opponents and self.game.changed_name == False:
                        if self.game.enter:
                            self.game.changed_name = True

            if self.game.chose_coin == False:
                self.game.run()
            else:
                self.state = True
                self.cars_name = self.game.cars_name_list
                self.map_number = self.game.map
                break

            

            # draw game cursor
            self.game.cursor_img_rect = pygame.mouse.get_pos()
            self.display_surface.blit(self.game.cursor_img, self.game.cursor_img_rect)

            pygame.display.update()
            self.clock.tick(60)
