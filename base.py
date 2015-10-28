from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivy.factory import Factory
import math


win_x = Window.size[0]
win_y = Window.size[1]

class Base(Widget):

	LEVELS = [16, 25, 36, 49, 64]
	current_level = LEVELS[0]
	divisions = int(math.sqrt(current_level))

Factory.register('Base', cls=Base)
