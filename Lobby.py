import pygame
import sys

from pygame.constants import MOUSEMOTION
import tetris_main
from Game import Game

class Menu:
    def __init__(self):
        pygame.init()
        
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Game Menu")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Consolas',75)
        self.current_screen = 'menu'
        self.backgrounds = {
            'menu': pygame.image.load('Graphic/menuchinh.png').convert(),
            'chonmap': pygame.image.load('Graphic/chonmap.png').convert(),
            'setting': pygame.image.load('Graphic/setting.png').convert(),
            'instruction': pygame.image.load('Graphic/huongdan.png').convert(),
            'menu_eng': pygame.image.load('Graphic/menuchinh_eng.png').convert(),
            'chonmap_eng': pygame.image.load('Graphic/chonmap_eng.png').convert(),
            'setting_eng': pygame.image.load('Graphic/setting_eng.png').convert(),
            'instruction_eng': pygame.image.load('Graphic/huongdan_eng.png').convert(),
            'shop_mo': pygame.image.load('Graphic/shopmo.png').convert(),
            'shop_mo_eng': pygame.image.load('Graphic/shopmo_eng.png').convert()
        }
        self.buttons = []
        self.money = 0
        
        
    def add_button(self, action, x, y, width, height):
        button_rect = pygame.Rect(x, y, width, height)
        self.buttons.append((button_rect, action))

    def check_button_click(self, mouse_pos):
        for button in self.buttons:
            if button[0].collidepoint(mouse_pos):
                return button[1]
        return None

    def menu_screen(self):
        self.buttons = []
        
        self.add_button('play', 873, 321, 272, 110)
        self.add_button('back', 24, 28, 85, 51)
        self.add_button('minigame', 831, 451, 355, 108)
        self.add_button('instruction', 838, 576, 341, 103)
        self.add_button('settings', 1188, 21, 68, 68)
        self.add_button('infor',1189,114,68,68)
        self.add_button('shop',153,185,365,240)
        pass

    def chonmap_screen(self):
        self.buttons = []  # Xóa danh sách các button cũ
    
        # Thêm các button mới
        self.add_button('map1', 63, 212, 240, 315)
        self.add_button('map2', 372, 212, 240, 315)
        self.add_button('map3', 673, 212, 240, 315)
        self.add_button('map4', 995, 212, 240, 315)
        self.add_button('back', 24, 28, 85, 51)
        pass

    def setting_screen(self):
         self.buttons = []  # Xóa danh sách các button cũ
    
        # Thêm các button mới
         self.add_button('sound', 471, 288, 69, 69)
         self.add_button('language', 471, 399, 68, 68)
         self.add_button('Ok',564,457,172,68)
         self.add_button('back', 24, 28, 85, 51)
         
         pass

    def instruction_screen(self):
        self.buttons = []
        
        self.add_button('back', 24, 28, 85, 51)
        pass

    def shop_screen(self):
        self.buttons = []
        
        self.add_button('shop', 153, 185, 365, 240)
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    motion_button = self.check_button_click(mouse_pos)
                    if self.current_screen == 'menu':
                       if motion_button == 'shop':
                          self.current_screen = 'shop_mo'
                    elif self.current_screen == 'shop_mo':
                       if motion_button != 'shop':
                           self.current_screen = 'menu'
                    elif self.current_screen == 'menu_eng':
                       if motion_button == 'shop':
                          self.current_screen = 'shop_mo_eng'
                    elif self.current_screen == 'shop_mo_eng':
                       if motion_button != 'shop':
                           self.current_screen = 'menu_eng'
                           
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_button = self.check_button_click(mouse_pos)  
                    
                    # màn hình menu TV
                    if self.current_screen == 'menu' :
                        if clicked_button == 'instruction': 
                            pygame.display.set_caption("Instruction")
                            self.current_screen = 'instruction'
                        elif clicked_button == 'minigame':
                            pygame.display.set_caption("Minigame")
                            print("Play minigame")
                            self.minigame = tetris_main.Main()
                            self.minigame.music.set_volume(0.05)
                            self.minigame.run()
                            # gọi minigame nếu k đủ tiền
                        elif clicked_button == 'play':
                            pygame.display.set_caption("Choose map")
                            print("Start Game")
                            self.current_screen = 'chonmap'
                        elif clicked_button == 'settings':
                            pygame.display.set_caption("Settings")
                            self.current_screen = 'setting'
                        elif clicked_button == 'back':
                            return
                        
                    # màn hình menu TA
                    elif self.current_screen == 'menu_eng' :
                        if clicked_button == 'instruction': 
                            pygame.display.set_caption("Instruction")
                            self.current_screen = 'instruction_eng'
                            print("Instruction in English")
                        elif clicked_button == 'minigame':
                            pygame.display.set_caption("Minigame")
                            print("Play minigame")
                            # gọi minigame nếu k đủ tiền
                        elif clicked_button == 'play':
                            pygame.display.set_caption("Choose map")
                            print("Start Game")
                            self.current_screen = 'chonmap_eng'
                        elif clicked_button == 'settings':
                            pygame.display.set_caption("Settings")
                            self.current_screen = 'setting_eng'
                        elif clicked_button == 'back':
                            return    
                            
                            
                    #màn hình chọn map chơi TV
                    elif self.current_screen == 'chonmap' :
                        if clicked_button == 'map1':
                            Game(1).run()
                            # dẫn gem zô
                        elif clicked_button == 'map2':
                           Game(2).run()
                            # dẫn gem zô
                        elif clicked_button == 'map3':
                            Game(3).run()
                            # dẫn gem zô
                        elif clicked_button == 'map4':
                            Game(4).run()
                            # dẫn gem zô
                        elif clicked_button == 'back':
                                pygame.display.set_caption("Game Menu")
                                self.current_screen = 'menu'
                    
                    #màn hình chọn map chơi TA
                    elif self.current_screen == 'chonmap_eng' :
                        if clicked_button == 'map1':
                            print("Map university")
                            # dẫn gem zô
                        elif clicked_button == 'map2':
                            print("Map grass field")
                            # dẫn gem zô
                        elif clicked_button == 'map3':
                            print("Map countryside")
                            # dẫn gem zô
                        elif clicked_button == 'map4':
                            print("Map city")
                            # dẫn gem zô
                        elif clicked_button == 'back':
                                pygame.display.set_caption("Game Menu")
                                self.current_screen = 'menu_eng'
                                
                    #màn hình hướng dẫn TV
                    elif self.current_screen == 'instruction':
                        if clicked_button == 'back':
                            pygame.display.set_caption("Game Menu")
                            self.current_screen = 'menu'
                            
                    #màn hình hướng dẫn TA
                    elif self.current_screen == 'instruction_eng':
                        if clicked_button == 'back':
                            pygame.display.set_caption("Game Menu")
                            self.current_screen = 'menu_eng'

                    #màn hình cài đặt TV sang TA
                    elif self.current_screen == 'setting' :
                        if clicked_button == 'sound':
                            print("Turn off/on music")
                            # lệnh tắt mở nhạc
                        elif clicked_button == 'language':
                            print("Change to English")
                            self.current_screen = 'setting_eng'
                        elif clicked_button == 'back':
                            pygame.display.set_caption("Game Menu")
                            self.current_screen = 'menu'
                            
                    #màn hình cài đặt TA sang TV
                    elif self.current_screen == 'setting_eng' :
                        if clicked_button == 'sound':
                            print("Turn off/on music")
                            # lệnh tắt mở nhạc
                        elif clicked_button == 'language':
                            print("Change to Vietnamese")
                            self.current_screen = 'setting'
                        elif clicked_button == 'back':
                            pygame.display.set_caption("Game Menu")
                            self.current_screen = 'menu_eng'
            
            # điều kiện chuyển màn hình                
            if self.current_screen == 'menu' or self.current_screen == 'menu_eng':
                self.menu_screen()
               
            if self.current_screen == 'chonmap' or self.current_screen == 'chonmap_eng': 
                self.chonmap_screen()
                
            if self.current_screen == 'instruction' or self.current_screen == 'instruction_eng': 
                self.instruction_screen()
                
            if self.current_screen == 'setting' or self.current_screen == 'setting_eng': 
                self.setting_screen()    
                
            if self.current_screen == 'shop_mo' or self.current_screen == 'shop_mo_eng' :
                self.shop_screen()
            
            
            # in ảnh ra màn hình    
            self.screen.blit(self.backgrounds[self.current_screen], (0, 0))
            # print(self.money)
            # in money
            money_surf = self.font.render(f'{self.money}', False, 'Red')
            money_rect = money_surf.get_rect(topleft = (1000, 250))
            self.screen.blit(money_surf, money_rect)

            # update screen
            pygame.display.flip()
            self.clock.tick(60)

Menu().run()

     