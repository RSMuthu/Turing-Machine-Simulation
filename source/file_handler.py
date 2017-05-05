class TypeException(Exception):
	def __str__(self):
		return "MK_Error --> File must be of type '.tur'"

class IOException(Exception):
	def __str__(self):
		return "MK_Error --> File doesnt exist/Permision denied"
