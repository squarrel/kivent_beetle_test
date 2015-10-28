from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.uix.screenmanager import Screen

import kivent_core
import kivent_cymunk
from kivent_core.gameworld import GameWorld
from kivent_core.systems.renderers import RotateRenderer
from kivent_core.systems.position_systems import PositionSystem2D
from kivent_core.systems.rotate_systems import RotateSystem2D
from kivent_core.systems.gamesystem import GameSystem
from kivent_core.managers.resource_managers import texture_manager

from beetle_system import BeetleSystem
from base import Base


texture_manager.load_atlas('assets/beetles.atlas')

class TestGame(Widget):

	def __init__(self, **kwargs):
		super(TestGame, self).__init__(**kwargs)
		self.gameworld.init_gameworld(
			['position', 'renderer'],
			callback=self.init_game)

	def init_game(self):
		state = 'main'
		self.setup_states()
		self.set_state(state)
		self.beetle_system.start()

	def setup_states(self):
		self.gameworld.add_state(state_name='main',
			systems_added=['renderer'],
			systems_removed=[], systems_paused=[],
			systems_unpaused=['renderer'],
			screenmanager_screen='main')

	def set_state(self, *args):
		self.gameworld.state = args[0]
		
	def messages(self, message):
		print message

class MainScreen(Screen):
	def show_message(self):
		message = "message"
		print "calling the other function"
		TestGame().messages(message)

class TestApp(App):
	pass

if __name__ == '__main__':
	TestApp().run()
