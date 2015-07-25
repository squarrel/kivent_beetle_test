from kivy.core.window import Window
from kivent_core.systems.gamesystem import GameSystem
from kivent_core.managers.resource_managers import (
	texture_manager, model_manager)
from kivy.factory import Factory
from kivy.clock import Clock
from random import randint, choice
from functools import partial

texture_manager.load_atlas('assets/background_objects.atlas')
model_manager.load_textured_rectangle(4, 7., 7., 'star1', 'star1-4')
model_manager.load_textured_rectangle(4, 10., 10., 'star1', 'star1-4-2')

win_x = Window.size[0]
win_y = Window.size[1]

class BeetleSystem(GameSystem):
	
	count = 0
	beetles = {}

	def __init__(self, *args, **kwargs):
		super(BeetleSystem, self).__init__(*args, **kwargs)

	def start(self):
		#self.draw_stuff()
		#Clock.schedule_once(self.draw_stuff)
		Clock.schedule_interval(self.draw_stuff, 1.0 / 1.0)
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	def draw_stuff(self, dt):
		print("|draw stuff")
		pos = (randint(0, win_x), randint(0, win_y))
		self.create_beetle(pos)
		self.beetles[self.count] = True
		self.count += 1

	def create_beetle(self, pos):
		vert_mesh_key = choice(['star1-4', 'star1-4-2'])
		create_dict = {
			'position': pos,
			'renderer': {'texture': 'star1',
				'vert_mesh_key': vert_mesh_key},
			}
		return self.gameworld.init_entity(create_dict, ['position',
			'renderer'])

	def remove_beetle(self, ent_id):
		self.gameworld.remove_entity(ent_id)
		self.beetles[ent_id] = False
		print("removed a beetle")

	def update(self, dt):
		entities = self.gameworld.entities
		for b in xrange(len(self.beetles)):
			print("b, beetles[b]", b, self.beetles[b])
			if self.beetles[b] == True:
				pos = entities[b].position
				pos.x += .45
				pos.y -= .45

				if pos.y < win_y / 10:
					self.remove_beetle(b)


Factory.register('BeetleSystem', cls=BeetleSystem)
