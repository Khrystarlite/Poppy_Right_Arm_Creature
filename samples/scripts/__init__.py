from .config import *
from .primitives import *
from .record import *

import pypot.robot


class Poppy_Right_Arm(object):
	"""docstring for Poppy_Right_Arm"""
	def __init__(self, arg):
		super(Poppy_Right_Arm, self).__init__()
		self.right_arm = pypot.robot.config.my_config(config())
