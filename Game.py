from Settings import *
from Racing import Racing
class Game:
    def __init__(self, map_number):
        pygame.init()
        pygame.display.set_caption('US88')
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("CSFONT-TwistyPixel.ttf", 50)
        # Name for random choices
        self.Name = NAMES

        # List of maps' images, list of cars' images and cars' rect
        self.maps_rect_list = []
        self.cars_image_list = []
        self.cars_rect_list = []

        self.cars_name_list = ['Bí danh: ', 'Bí danh: ', 'Bí danh: ', 'Bí danh: ', 'Bí danh: ']
        self.current_opponent = 0
        self.name_x = 140

        self.coins_rect_list = []
        self.coins_list = ['1000$', '2000$', '3000$', '4000$']

        # cursor attributes
        self.mouse_pos = (0, 0)
        self.mouse_sound = pygame.mixer.Sound('mouseclick1.mp3')
        # pygame.mouse.set_visible(False)
        self.cursor_img = pygame.image.load('normal.png')
        self.cursor_img_rect = self.cursor_img.get_rect()

        # the number of map, car and coin that user choose
        self.map = map_number
        self.car = 0
        self.coin = 0

        # the state of each def
        self.chose_car = False
        self.changed_name = False
        self.changed_opponents = False
        self.displayed_information = False
        self.chose_coin = False

        # the image of map and coin
        self.map_image = 0
        self.coin_image = 0
 
        self.enter = False

        # background
        self.bg = pygame.image.load('ChoosingCarBackground.png').convert_alpha()
        self.bg.set_alpha(120)
    def display_cursor(self):
        self.cursor_img_rect = pygame.mouse.get_pos()
        self.display_surface.blit(self.cursor_img, self.cursor_img_rect)


    def list_cars(self):

        if self.chose_car == False:
            self.display_surface.fill((0, 0, 0))
            self.display_surface.blit(self.bg, (0, 0))
            cars_x = 140

            text = self.font.render('HÃY CHỌN CHIẾN MÃ CỦA BẠN', False, 'Red')
            text_rect = text.get_rect(center = (640, 100))
            self.display_surface.blit(text, text_rect)
           
            for i in range(1, CARS + 1):                
                cars_image = pygame.transform.scale(pygame.image.load(f'xe{i}.png').convert_alpha(), (100, 65))
                cars_rect = cars_image.get_rect(center = (cars_x, 360))
                if len(self.cars_rect_list) != CARS:
                    self.cars_image_list.append(cars_image)
                    self.cars_rect_list.append(cars_rect)
                self.display_surface.blit(cars_image, cars_rect)

                cars_x += (GAME_WIDTH - 280) / (CARS - 1)

        if self.car > 0 and self.chose_car == False:
            self.cars_image_list[self.car - 1] = pygame.transform.scale(pygame.image.load(f'xe{self.car}.png').convert_alpha(), (100, 65))
            self.chose_car = True


    def change_name(self):

        if self.chose_car and self.changed_name == False:
            self.display_surface.fill((0, 0, 0))
            self.display_surface.blit(self.bg, (0, 0))
            cars_x = 140

            text = self.font.render('HÃY CHỌN BÍ DANH CHO BẢN THÂN VÀ CÁC ĐỐI THỦ', False, 'Red')
            text_rect = text.get_rect(center = (640, 100))
            self.display_surface.blit(text, text_rect)
             
            for i in range(CARS):
            
                cars_image = self.cars_image_list[i]
                name_surface = self.font.render(self.cars_name_list[i], True, (255, 255, 255))

                cars_rect = cars_image.get_rect(center = (cars_x, 360))
                name_rect = name_surface.get_rect(center = (cars_x, 500))
                                
                self.display_surface.blit(cars_image, cars_rect)
                self.display_surface.blit(name_surface, name_rect)

                if i == self.car - 1:
                    pygame.draw.rect(self.display_surface, COLOR, cars_rect, 2)
                
                cars_x += (GAME_WIDTH - 280) / (CARS - 1)

            for i in range(CARS):

                if i == self.current_opponent:

                    name_surface = self.font.render(self.cars_name_list[self.current_opponent], True, (255, 255, 255))

                    name_rect = name_surface.get_rect(center = (self.name_x, 500))

                    pygame.draw.rect(self.display_surface, COLOR, name_rect, 2)
                                
                    self.display_surface.blit(name_surface, name_rect)


    def bet_money(self):
        
        if self.changed_name and self.chose_coin == False:

            self.display_surface.fill((0, 0, 0))
            self.display_surface.blit(self.bg, (0, 0))
            coins_x = 140

            text = self.font.render('HÃY CHỌN MỨC CƯỢC THÔI NÀO', False, 'Red')
            text_rect = text.get_rect(center = (640, 100))
            self.display_surface.blit(text, text_rect)
           
            for i in range(1, COINS + 1):                
                coins_image = pygame.transform.scale(pygame.image.load(f'coins/coin{i}.png').convert_alpha(), (100, 80))
                coins_rect = coins_image.get_rect(center = (coins_x, 360))

                price_surface = self.font.render(self.coins_list[i - 1], True, (255, 255, 255))
                price_rect = price_surface.get_rect(center = (coins_x, 500))

                if len(self.coins_rect_list) != COINS:
                    self.coins_rect_list.append(coins_rect)

                self.display_surface.blit(coins_image, coins_rect)
                self.display_surface.blit(price_surface, price_rect)

                coins_x += (GAME_WIDTH - 280) / (COINS - 1)

        if self.coin > 0 and self.chose_coin == False:
            self.chose_coin = True
            

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    self.mouse_sound.play()

                    # Choose your car
                    if self.chose_car == False:
                        for j in range(len(self.cars_rect_list)):
                            if self.cars_rect_list[j].collidepoint(event.pos):
                                self.car = j + 1

                    # Choose your bet money
                    if self.chose_coin == False:
                        for k in range(len(self.coins_rect_list)):
                            if self.coins_rect_list[k].collidepoint(event.pos):
                                self.coin = (k + 1) * 1000

                if event.type == pygame.KEYDOWN:

                    self.enter = True

                    # Input name for each car
                    if self.chose_car and self.changed_opponents == False:
                        
                        if event.key == pygame.K_BACKSPACE and len(self.cars_name_list[self.current_opponent]) >= 10:
                            self.cars_name_list[self.current_opponent] = self.cars_name_list[self.current_opponent][:-1]

                        elif event.key == pygame.K_RETURN and self.enter:
                            self.cars_name_list[self.current_opponent] = self.cars_name_list[self.current_opponent][9:]
                                                         
                            if len(self.cars_name_list[self.current_opponent]) == 0:
                                self.cars_name_list[self.current_opponent] = choice(self.Name)
                                self.Name.remove(self.cars_name_list[self.current_opponent])

                            self.name_x += (GAME_WIDTH - 280) / (CARS - 1)

                            self.current_opponent += 1

                            self.enter = False

                            if self.current_opponent == CARS:
                                self.changed_opponents = True

                        elif len(self.cars_name_list[self.current_opponent]) < 22:
                            self.cars_name_list[self.current_opponent] += event.unicode

                    if self.changed_opponents and self.changed_name == False:
                        if self.enter:
                            self.changed_name = True

            if self.chose_coin == False:
                self.list_cars()
                self.change_name()
                self.bet_money()
            else:
                Racing(self.cars_name_list, self.map).run()
                break
                
            # draw game cursor
            self.cursor_img_rect = pygame.mouse.get_pos()
            self.display_surface.blit(self.cursor_img, self.cursor_img_rect)

            pygame.display.update()
            self.clock.tick(60) 



