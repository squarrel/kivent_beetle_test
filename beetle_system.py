from kivy.core.window import Window
from kivent_core.systems.gamesystem import GameSystem
from kivent_core.gameworld import GameWorld
from kivy.factory import Factory
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from random import randint, choice
from base import Base


win_x = Window.size[0]
win_y = Window.size[1]

class BeetleSystem(GameSystem):
	
	system_id = StringProperty('beetle_system')
	beetles = {}

	def __init__(self, *args, **kwargs):
		super(BeetleSystem, self).__init__(*args, **kwargs)

	def start(self):
		Clock.schedule_interval(self.draw_stuff, 1.0 / 147.0)

	def draw_stuff(self, dt):
		pos = (randint(0, win_x), randint(0, win_y))
		self.create_beetle(pos)

	def create_beetle(self, pos):
		vert_mesh_key = choice(['beetle_up', 'beetle_down'])
		create_dict = {
			'position': pos,
			'renderer': {'texture': vert_mesh_key,
				'vert_mesh_key': vert_mesh_key},
			'beetle_system': {},
			}
		return self.gameworld.init_entity(create_dict, ['position',
			'renderer', 'beetle_system'])

	def remove_beetle(self, ent_id):
		self.gameworld.remove_entity(ent_id)

	def update(self, dt):
		entities = self.gameworld.entities
		
		for component in self.components:
			if component is not None:
				entity_id = component.entity_id
				pos = entities[entity_id].position
				pos.x += 5.75
				pos.y -= 5.75
				if pos.y < win_y / 10:
					self.remove_beetle(entity_id)


Factory.register('BeetleSystem', cls=BeetleSystem)
