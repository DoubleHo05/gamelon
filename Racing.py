import pygame
from random import randint, choice
from operator import attrgetter
from Settings import *

pygame.init()
screen  = pygame.display.set_mode((1280, 720),pygame.RESIZABLE)
pygame.display.set_caption('US88')
font = pygame.font.SysFont('Consolas',20)
clock = pygame.time.Clock()
normal1_1 = ['cars/AS87/AS87_1.png', 'cars/NA4/NA4_1.png', 'cars/NA5/NA5_1.png', 'cars/NA6/NA6_1.png', 'cars/NA2/NA2_1.png']
normal1_2 = ['cars/AS87/AS87_2.png', 'cars/NA4/NA4_2.png', 'cars/NA5/NA5_2.png', 'cars/NA6/NA6_2.png', 'cars/NA2/NA2_2.png']
tangtoc1_1 = ['cars/AS87/AS87_tang_toc_1.png', 'cars/NA4/NA4_tang_toc_1.png', 'cars/NA5/NA5_tang_toc_1.png', 'cars/NA6/NA6_tang_toc_1.png', 'cars/NA2/NA2_tang_toc_1.png']
tangtoc1_2 = ['cars/AS87/AS87_tang_toc_2.png', 'cars/NA4/NA4_tang_toc_2.png', 'cars/NA5/NA5_tang_toc_2.png', 'cars/NA6/NA6_tang_toc_2.png', 'cars/NA2/NA2_tang_toc_2.png']
cham1_1 = ['cars/AS87/AS87_cham_1.png', 'cars/NA4/NA4_cham_1.png', 'cars/NA5/NA5_cham_1.png', 'cars/NA6/NA6_cham_1.png', 'cars/NA2/NA2_cham_1.png']
cham1_2 = ['cars/AS87/AS87_cham_2.png', 'cars/NA4/NA4_cham_2.png', 'cars/NA5/NA5_cham_2.png', 'cars/NA6/NA6_cham_2.png', 'cars/NA2/NA2_cham_2.png']
winner = ['cars/AS87/winner.png', 'cars/NA4/winner.png', 'cars/NA5/winner.png', 'cars/NA6/winner.png', 'cars/NA2/winner.png']
set2 = ['xe6.png', 'xe7.png', 'xe8.png', 'xe9.png', 'xe10.png']

class Car():
    def __init__(self, i, map, leaderboard, final_rank):
        self.order = i
        
        # buff 
        self.duration = 0
        self.start_time = 0
        self.buff = None

        # leaderboard setting up
        self.leaderboard = leaderboard
        self.final_rank1 = 0
        self.final_rank2 = final_rank
        self.pos = 1
        
        # assign image to the car
        if map == 1:
            
            surf1 = pygame.image.load(f'{normal1_1[i]}').convert_alpha()
            surf2 = pygame.image.load(f'{normal1_2[i]}').convert_alpha()
            self.surf = [surf1, surf2]
            self.index = 0
            self.image = pygame.transform.scale(self.surf[int(self.index)], (100, 65))

        self.rect = self.image.get_rect(midleft = (0, i * 100 + 245))
        
        # random speed for each car
        self.sta_speed = randint(1,5)
        self.mid_speed1 = randint(5,10)
        self.mid_speed2 = randint(5,10)
        self.mid_speed3 = randint(7,13)
        self.fin_speed = randint(8,15)

    # return speed with no buff for each car according to timer
    def speed(self):
        if current_time <= 1:
            return self.sta_speed
        elif current_time <= 5:
            return self.mid_speed1
        elif current_time <= 10:
            return self.mid_speed2
        elif current_time <= 15:
            return self.mid_speed3
        else: return self.fin_speed
    
    # return speed without assigning animation
    def return_speed(self):
        if (self.rect.right >= 1280):
            return 0
        if current_time <= self.start_time + self.duration:
            if self.buff == 'bua_tang_toc':
                return self.speed() + 5
            if self.buff == 'bua_cham':
                return self.speed() - 5
            if self.buff == 'bua_di_lui':
                return -5
        return self.speed()

    # return speed and playing animation
    def check_buff(self):
        if current_time <= self.start_time + self.duration:
            if self.buff == 'bua_tang_toc':
                surf1 = pygame.image.load(f'{tangtoc1_1[self.order]}').convert_alpha()
                surf2 = pygame.image.load(f'{tangtoc1_2[self.order]}').convert_alpha()
                self.surf = [surf1, surf2]
                self.image = pygame.transform.scale(self.surf[int(self.index)], (100, 65))
                if current_time == self.start_time + self.duration: self.buff = None
                return self.speed() + 5
            if self.buff == 'bua_cham':
                surf1 = pygame.image.load(f'{cham1_1[self.order]}').convert_alpha()
                surf2 = pygame.image.load(f'{cham1_2[self.order]}').convert_alpha()
                self.surf = [surf1, surf2]
                self.image = pygame.transform.scale(self.surf[int(self.index)], (100, 65))
                if current_time == self.start_time + self.duration: self.buff = None
                return self.speed() - 5
            if self.buff == 'bua_di_lui':
                surf1 = pygame.image.load(f'{normal1_1[self.order]}').convert_alpha()
                surf2 = pygame.image.load(f'{normal1_2[self.order]}').convert_alpha()
                self.surf = [surf1, surf2]
                self.image = pygame.transform.scale(self.surf[int(self.index)], (100, 65))
                if current_time == self.start_time + self.duration: self.buff = None
                return -5
        surf1 = pygame.image.load(f'{normal1_1[self.order]}').convert_alpha()
        surf2 = pygame.image.load(f'{normal1_2[self.order]}').convert_alpha()
        self.surf = [surf1, surf2]
        self.image = pygame.transform.scale(self.surf[int(self.index)], (100, 65))
        return self.speed()
    
    # car movement
    def movement(self):
        # playing winning animation if final rank is 1st
        if self.order == self.leaderboard.ranking[0].order and self.rect.right >= 1280:
                surf1 = pygame.image.load(f'{winner[self.order]}').convert_alpha()
                surf2 = pygame.transform.flip(surf1, True, False)
                self.surf = [surf1, surf2]
                self.image = pygame.transform.scale(self.surf[int(self.index)], (100, 65))

        # flip the image if buff == 'bua_di_lui'
        if self.buff == 'bua_di_lui': screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
        else: screen.blit(self.image,self.rect)

        # move car to the right
        self.rect.right += (self.check_buff())

        # check if touching the screen border
        if(self.rect.right >= 1280):
            self.rect.right = 1280
            # saving final_rank for sorting the leaderboard if multiple cars have self.rect.right = 1280
            if self.final_rank1 == 0:
                self.final_rank1 = self.final_rank2
                self.final_rank2 -= 1
        
        # saving pos for sorting the leaderboard
        self.pos = self.rect.right
    
    # playing animation
    def animation_state(self):
        self.index += 0.1
        if self.index  >= len(self.surf): self.index = 0
        self.image = pygame.transform.scale(self.surf[int(self.index)], (100, 65))

    # update function for car class
    def update(self):
        self.movement()
        self.animation_state()


class Mystery(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        mystery = [1, 2, 3]
        self.image = pygame.image.load(f'mystery/mystery{choice(mystery)}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (65, 65))
        self.rect = self.image.get_rect(midleft = (x_pos, y_pos))

    # assign buff attribute to the car
    def bua_tang_toc(self, car):
        car.buff = 'bua_tang_toc'
        car.duration = 3
        car.start_time = current_time

    def bua_cham(self, car):
        car.buff = 'bua_cham'
        car.duration = 3
        car.start_time = current_time

    def bua_di_lui(self, car):
        car.buff = 'bua_di_lui'
        car.duration = 3
        car.start_time = current_time
    
    # check collision between the car and mystery box
    # random the buff
    def collide(self, car):
        if self.rect.colliderect(car.rect):
            random = choice(['bua_cham', 'bua_di_lui', 'bua_tang_toc'])
            if random == 'bua_tang_toc':
                self.bua_tang_toc(car)
            elif random == 'bua_cham':
                self.bua_cham(car)
            elif random == 'bua_di_lui':
                self.bua_di_lui(car)
            self.kill()

    # update function for Mystery class
    def update(self, car):
        self.collide(car)

    
class Leaderboard():
    def __init__(self, cars_name):
        self.ranking = []
        self.cars_name = cars_name
        self.order = []
    
    # append all the car to the leaderboard
    def append(self, car, i):
        self.ranking.append(car)
        self.order.append(i)
    
    # sort the leaderboard
    def sort(self):
        self.ranking = sorted(self.ranking, key = attrgetter('final_rank1', 'pos'), reverse = True)
    

    def update(self):
        self.sort()
        # blit leaderboard stats to the screen
        if self.ranking:
            # blit unchanged stats
            maps_x = 50
            for i in range(5):
                text_surf = font.render(f'Làn {i + 1}: ',False,'White')
                text_rect = text_surf.get_rect(midleft = (maps_x, 25))
                profile_border = pygame.image.load('Profile Border.png').convert_alpha()
                profile_border = pygame.transform.scale(profile_border, (230, 150))
                profile_bg = pygame.image.load('Profile BackGround.png').convert_alpha()
                profile_bg = pygame.transform.scale(profile_bg, (230, 150))
                profile_bg.set_alpha(120)
                screen.blit(profile_border, (text_rect.x - 15 , text_rect.y - 15))
                screen.blit(profile_bg, (text_rect.x - 15 , text_rect.y - 15))
                screen.blit(text_surf, text_rect)

                text_surf = font.render(f'{self.cars_name[i]}',False,'White')
                text_rect = text_surf.get_rect(midleft = (maps_x, 50))
                screen.blit(text_surf, text_rect)

                car_surf = pygame.image.load(f'{normal1_1[self.order[i]]}').convert_alpha()
                car_surf = pygame.transform.scale(car_surf, (75, 50))
                car_rect = car_surf.get_rect(topright = (maps_x + 200, 25))
                screen.blit(car_surf, car_rect)
                maps_x += 250
            
            # blit changed stats
            for j in range(5):
                maps_x = 50 + self.ranking[j].order * 250
                s = f'Hạng: {j + 1}'
                if j + 1 == 1:
                    s = s + 'st'
                elif j + 1 == 2:
                    s = s + 'nd'
                elif j + 1 == 3:
                    s = s + 'rd'
                else: s = s + 'th'
                text_surf = font.render(s,False,'White')
                text_rect = text_surf.get_rect(midleft = (maps_x, 75))
                screen.blit(text_surf, text_rect)
                if self.ranking[j].buff == None:
                    text_surf = font.render(f'Hiệu ứng: không có',False,'White')
                    text_rect = text_surf.get_rect(midleft = (maps_x, 100))
                elif self.ranking[j].buff == 'bua_tang_toc':
                    text_surf = font.render(f'Hiệu ứng: tăng tốc',False,'White')
                    text_rect = text_surf.get_rect(midleft = (maps_x, 100))
                elif self.ranking[j].buff == 'bua_cham':
                    text_surf = font.render(f'Hiệu ứng: chậm',False,'White')
                    text_rect = text_surf.get_rect(midleft = (maps_x, 100))
                elif self.ranking[j].buff == 'bua_di_lui':
                    text_surf = font.render(f'Hiệu ứng: đi lùi',False,'White')
                    text_rect = text_surf.get_rect(midleft = (maps_x, 100))
                screen.blit(text_surf, text_rect)
                text_surf = font.render(f'Tốc độ: {self.ranking[j].return_speed()}',False,'White')
                text_rect = text_surf.get_rect(midleft = (maps_x, 125))
                screen.blit(text_surf, text_rect)



class Background():
    def __init__(self, map_number):

        self.sky_surf = pygame.image.load(f'maps/sky{map_number}.png').convert()
        self.sky_rect = self.sky_surf.get_rect(topleft = (0,0))

        self.racetrack_surf = pygame.image.load(f'maps/racetrack{map_number}.jpg').convert()
        self.racetrack_rect = self.racetrack_surf.get_rect(topleft = (0, 170))
    
        self.fin_surf = pygame.image.load('finish_line.jpg').convert()
        self.fin_rect = self.fin_surf.get_rect(bottomright = (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.max_pos = 0
        self.max_speed = 0
        self.count = 0
        self.amount = 0
    
    
    def update(self):
        screen.blit(self.sky_surf, self.sky_rect)

        screen.blit(self.racetrack_surf, self.racetrack_rect)

        screen.blit(self.fin_surf, self.fin_rect)


class Racing():
    def __init__(self, cars_name, map_number):
        # init the rank
        self.final_rank = 5 

        # init the timer for the buff
        self.start_time = 0
        self.current_time = 0

        # assign the names into the game
        self.cars_name = cars_name
        self.leaderboard = Leaderboard(self.cars_name)

        # init the background
        self.bg = Background(map_number)

        # init cars
        self.car1 = Car(0,1, self.leaderboard,self.final_rank)
        self.car2 = Car(1,1, self.leaderboard,self.final_rank)
        self.car3 = Car(2,1, self.leaderboard,self.final_rank)
        self.car4 = Car(3,1, self.leaderboard,self.final_rank)
        self.car5 = Car(4,1, self.leaderboard,self.final_rank)
        
        # push cars into leaderboard
        self.leaderboard.append(self.car1, 0)
        self.leaderboard.append(self.car2, 1)
        self.leaderboard.append(self.car3, 2)
        self.leaderboard.append(self.car4, 3)
        self.leaderboard.append(self.car5, 4)

        # blit mystery box randomly on the screen
        self.mystery_list = pygame.sprite.Group()
        for i in range(5):
            self.mystery_list.add(Mystery(randint(250, 350), i * 100 + 245))
        for i in range(5):
            self.mystery_list.add(Mystery(randint(700, 900), i * 100 + 245))

    # timer
    def display_time(self):
        global current_time
        current_time = int(pygame.time.get_ticks() / 1000) - self.start_time

    # blit map
    def display_map(self):
        self.bg.update()

    def run(self):        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # blit the background and timer   
            self.display_map()
            self.display_time()

            # draw mystery and update collision 
            self.mystery_list.draw(screen)
            self.mystery_list.update(self.car1)
            self.mystery_list.update(self.car2)
            self.mystery_list.update(self.car3)
            self.mystery_list.update(self.car4)
            self.mystery_list.update(self.car5)

            # update the leaderboard
            self.leaderboard.update()

            # update car movement
            self.car1.update()
            self.car2.update()
            self.car3.update()
            self.car4.update()
            self.car5.update()

            pygame.display.update()
            clock.tick(60)


        
        
