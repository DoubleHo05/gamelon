from tetris_settings import *
from sys import exit
from os.path import join

# components
from tetris_game import Game
from tetris_score import Score
from tetris_preview import Preview

from random import choice

class Main:
	def __init__(self):

		# general 
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()
		pygame.display.set_caption('Tetris')

		# shapes
		self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]

		# audio 
		self.music = pygame.mixer.Sound('tetris_theme.mp3')

		# components
		self.game = Game(self.get_next_shape, self.update_score, self.music)
		self.score = Score()
		self.preview = Preview()

		
		

	def update_score(self, lines, score, level):
		self.score.lines = lines
		self.score.score = score
		self.score.level = level

	def get_next_shape(self):
		next_shape = self.next_shapes.pop(0)
		self.next_shapes.append(choice(list(TETROMINOS.keys())))
		return next_shape

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit() 
			
			# play music
			self.music.play(-1)
			# self.music.set_volume(0.05)
			# display 
			self.display_surface.fill(GRAY)
			
			# components
			self.game.run()
			self.score.run()
			self.preview.run(self.next_shapes)

			# updating the game
			pygame.display.update()
			self.clock.tick()

# if __name__ == '__main__':
# 	main = Main()
# 	main.run()
