from handler import MachineTapeException
import sys

pr = sys.stdout.write

class MachineTape:
	def __init__(self, initialString=[], initialPos=0, blank="_"):
		""" The Tape uses a simple list.  It could easily be changed into a string if
		    need be """
		self.tape = []
		self.pos = initialPos
		self.blank = blank
		self.initialString = initialString
		if len(initialString) > 0:
		    for ch in initialString:
			    self.tape.append(ch)
		else:
		    self.tape.append(blank)

	def reinit(self):
		self.__init__(self.initialString)

	def move(self, check_char, changeto_char, direction):
		""" Only R, L directions are supported """
		# check to see if the character under the head is what we need
		if check_char != self.tape[self.pos]:
			raise MachineTapeException ("Tape head doesn't match head character")

		# at this point the head is over the same character we are looking for
		#  change the head character to the new character
		self.tape[self.pos] = changeto_char

		if direction == "L":
			self.move_left()
		elif direction == "R":
			self.move_right()
		#elif direction == 'N':
		#	self.no_move()
		else: raise MachineTapeException ("Direction is invalid")

	def no_move(self):
		self.pos = self.pos

	def read(self):
		""" return the character over the head """
		return self.tape[self.pos]

	def move_left(self):
		if self.pos == 0:
			self.tape.insert(0, self.blank)
			self.pos = 0
		else:
			self.pos += -1

	def move_right(self):
		self.pos += 1
		if self.pos >= len(self.tape): self.tape.append(self.blank)

	def show(self):
		""" print the tape """
		for ch in self.tape:
			pr(ch)
		pr("\n"); pr(" "*self.pos + "^"); pr("\n")
