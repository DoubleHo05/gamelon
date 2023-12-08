from Settings import *
from Racing import Racing

class runRacing():
    def __init__(self, cars_name, map_number):

        # general
        pygame.init()

        self.clock = pygame.time.Clock()
        self.racing = Racing(cars_name, map_number)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.racing.run()
        
            pygame.display.update()
            self.clock.tick(60)
