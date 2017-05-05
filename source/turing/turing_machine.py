from handler import MachineTapeException, NoStatesException, NoInitStateException, NoFinalStateException, TuringErrorException, TuringAcceptException, NoTransitionsException, NoInputException
from machine_tape import MachineTape
import sys

"""
Program Layout:
[state][char_in] --> (dest_state, char_out, movement)
"""

class TuringMachine:
    def __init__(self, states, finalStates=[], blank="_"):
        self.states = states
        self.blank = blank
        self.fstates = finalStates
        self.program = {}
        self.initState = 0
        self.step_count = 1
        self.state = self.initState
        self.inp_available = False

    def __init__(self, blank="_"):
        self.states = {}
        self.blank = blank
        self.fstates = []
        self.program = {}
        self.initState = None
        self.step_count = 1
        self.state = self.initState
        self.inp_available = False

    def add_states(self, states):
        self.states = states

    def set_final_state(self, states_list):
        self.fstates = states_list

    def set_init_state(self, initial):
        self.initState = initial
        self.state = self.initState

    def add_input(self, inp):
        self.lenStr = len(inp)
        self.tape = MachineTape(inp)
        self.inp_available = True

    def reinit(self):
        self.state = self.initState
        self.step_count = 1
        self.tape.reinit()

    def addTransition(self, state, char_in, dest_state, char_out, movement):
        try:
            if self.states == {}:
                raise NoStatesException
            if not self.program.has_key(state):
                self.program[state] = {}

            tup = (dest_state, char_out, movement)
            self.program[state][char_in] = tup
        except NoStatesException as s:
            print s
            return True

    def step(self):
        """
        Step 1. Check to see if the length of the string is zero and if we
        are in a final state
        Step 2. If the currentstate is in the final states then raise an Accept
        Step 3. If the currentstate is not in the program then raise an Error
        """
        if self.lenStr == 0 and self.state in self.fstates: raise TuringAcceptException(self.states[self.state])
        if self.state in self.fstates: raise TuringAcceptException(self.states[self.state])
        if self.state not in self.program: raise TuringErrorException

        """
        Step 4. Check the head character
        Step 5. If the head character is not in the program and in the current state then
        raise an Error
        """
        head = self.tape.read()
        if head not in self.program[self.state]: raise TuringErrorException

        """
        Step 6. Retrieve from the dictionary the dest_state, char_out, and movement
        Step 7. set the current state to the new state
        """
        # execute transition
        (dest_state, char_out, movement) = self.program[self.state][head]

        print '\nStep ', self.step_count, ':'
        print "Transition: " + u'\u03B4' + "("+ self.states[self.state]+", '" + head+"') => ("+self.states[dest_state] + ", '"+char_out+"', '" + movement + "')"
        self.state = dest_state
        self.step_count += 1
        try:
            """
            Step 8. write the tape, and move the head
            """
            self.tape.move(head, char_out, movement)
        except MachineTapeException, s:
            print s
            return True

    def execute(self):
        """ The TM will keep stepping forever until the TM accepts or rejects.
        This does allow for looping TM's """
        try:
            if self.initState == None:
                raise NoInitStateException
            if self.fstates == []:
                raise NoFinalStateException
            if self.program == {}:
                raise NoTransitionsException('run the machine')
            if not self.inp_available:
                raise NoInputException
            while 1:
                self.tape.show()
                self.step()
        except (NoInitStateException, NoFinalStateException, TuringErrorException, NoTransitionsException, TuringAcceptException, NoInputException), s:
            print s
            return True

    def disp_transition_fn(self):
        try:
            if self.program == {}:
                raise NoTransitionsException('display')
            print '\n======================\nTransition Table\n======================\n'
            for state in self.program:
                for inp in self.program[state]:
                    (res, out, direc) =self.program[state][inp]
                    print u'\u03B4' + "("+ self.states[state]+", '" + inp+"') => ("+self.states[res] + ", '"+out+"', '" + direc + "')"
            print '\n======================\n'
        except NoTransitionsException as s:
            print s
