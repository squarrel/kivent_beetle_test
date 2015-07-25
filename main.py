from kivy.app import App
print('imported kivy')
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from random import randint, choice
import math
from math import radians, pi, sin, cos
import kivent_core
import kivent_cymunk
from kivent_core.gameworld import GameWorld
from kivent_core.rendering.vertmesh import VertMesh
from kivent_core.systems.renderers import RotateRenderer
from kivent_core.systems.position_systems import PositionSystem2D
from kivent_core.systems.rotate_systems import RotateSystem2D
from kivent_core.systems.gamesystem import GameSystem
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.factory import Factory
from functools import partial
from beetle_system import BeetleSystem
print("|finished all imports")


class TestGame(Widget):
	
	def __init__(self, **kwargs):
		print("|self init")
		super(TestGame, self).__init__(**kwargs)
		self.gameworld.init_gameworld(
			['position', 'renderer'],
			callback=self.init_game)

	def init_game(self):
		print("|init game")
		state = 'main'
		self.setup_states()
		self.set_state(state)
		self.beetle_system.start()

	def setup_states(self):
		print("|setup states")
		self.gameworld.add_state(state_name='main',
			systems_added=['renderer'],
			systems_removed=[], systems_paused=[],
			systems_unpaused=['renderer'],
			screenmanager_screen='main')

	def set_state(self, *args):
		print("|set state")
		self.gameworld.state = args[0]

class TestApp(App):
	pass

if __name__ == '__main__':
	TestApp().run()
