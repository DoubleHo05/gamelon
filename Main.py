from Settings import *
from runGame import runGame
from runRacing import runRacing

class Main():

    def __init__(self):

        # general
        pygame.init()
        pygame.display.set_caption('US88')
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)

        self.game = runGame()
        

    def run(self):

        if self.game.state == False:
            self.game.run()
        
        if self.game.state:
            self.racing = runRacing(self.game.cars_name, self.game.map_number)
            self.racing.run()
        
        

Main().run()