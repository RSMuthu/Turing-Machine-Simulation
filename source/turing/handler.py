class MachineTapeException(Exception):
	""" Turing Exception Exception """
	def __init__(self, value):
		Exception.__init__(self)
		self.value = value
	def __str__(self):
		return "MK --> " + self.value

class TuringErrorException(Exception):
	""" Turing Exception Exception """
	def __str__(self):
		return "MK --> Crash due to Transision failure. Input Not Accepted"

class TuringAcceptException(Exception):
	""" Turing Accept Exception """
	def __init__(self, value):
		Exception.__init__(self)
		self.value = value
	def __str__(self):
		return "MK --> Tansition completed in state '" + self.value + "'. Input is Accepted"

class NoInputException(Exception):
	def __str__(self):
		return "MK_Error --> Input data not provided. Machine Terminates"

class NoTransitionsException(Exception):
	def __init__(self, value):
		Exception.__init__(self)
		self.value = value
	def __str__(self):
		return "MK_Error --> Transition Funtions are not added to " + self.value

class NoInitStateException(Exception):
	def __str__(self):
		return "MK_Error --> Mention Initial State before running the Machine"

class NoFinalStateException(Exception):
	def __str__(self):
		return "MK_Error --> Mention Final States for the Machine to terminate"

class NoStatesException(Exception):
	def __str__(self):
		return "MK_Error --> The Machine states are not defined"
