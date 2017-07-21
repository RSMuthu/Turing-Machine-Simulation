from turing.turing_machine import TuringMachine
from parse_handler import MachineInitException, SyntaxRecogException
import re

class parser:
    def __init__(self):
        self.machine = {}
        self.states = {}
        self.state_rev_index = {}
        self.line_count = ''

    def set_line_count(self, count):
        self.line_count = count

    def to_list(self, inp):
        inp = re.sub(r'\s', '', inp)
        split_list = inp.split(',')
        return split_list

    def process_state(self, mac, stat):
        if mac not in self.machine:
            raise MachineInitException(self.line_count)
        state_list = self.to_list(stat)
        for i, x in enumerate(state_list):
            self.states[i] = x
            self.state_rev_index[x] = i
        self.machine[mac].add_states(self.states)
        print "MK --> State List added to the Machine '" + mac + "'"

    def process_init_state(self, mac, init_state):
        if mac not in self.machine:
            raise MachineInitException(self.line_count)
        if init_state not in self.state_rev_index:
            raise NotInStateException(self.line_count, 'Initial State \'' + init_state + '\' not available in the States List')
        self.machine[mac].set_init_state(self.state_rev_index[init_state])
        print "MK --> Initial State added to the Machine '" + mac + "'"

    def process_final_state(self, mac, stat):
        if mac not in self.machine:
            raise MachineInitException(self.line_count)
        state_list = self.to_list(stat)
        final = list()
        for x in state_list:
            if x not in self.state_rev_index:
                raise NotInStateException(self.line_count, 'Final State \'' + x + '\' not available in the States List')
            final.append(self.state_rev_index[x])
        self.machine[mac].set_final_state(final)
        print "MK --> Final States added to the Machine '" + mac + "'"

    def trans_fn(self, mac, fro, to):
        if mac not in self.machine:
            raise MachineInitException(self.line_count)
        from_state = self.to_list(fro)
        to_state =  self.to_list(to)
        if from_state[0] not in self.state_rev_index:
            raise NotInStateException(self.line_count, 'Transition State \'' + from_state[0] + '\' not available in the States List')
        if to_state[0] not in self.state_rev_index:
            raise NotInStateException(self.line_count, 'Transition State \'' + to_state[0] + '\' not available in the States List')
        self.machine[mac].addTransition(self.state_rev_index[from_state[0]], from_state[1], self.state_rev_index[to_state[0]], to_state[1], to_state[2])
        print 'MK --> Transition function Added'

    def inp_reader(self, mac, inp, get):
        try:
            if mac not in self.machine:
                raise MachineInitException(self.line_count)
            if get:
                inp = raw_input('Enter The Input String: ')
            self.machine[mac].add_input(inp)
            print "\nMK --> Input added to the machine tape\n"
        except KeyboardInterrupt:
            print "\nTuring Machine Simulator Terminates ....\n"

    def parse(self, inp):
        inp = re.sub(r'\s+', " ", inp)
        try:
            m = re.match(r'[Ii]nitiate\sTM\sas\s([a-zA-Z_][a-zA-Z0-9_]*)', inp)
            if m:
                self.machine[m.group(1)] = TuringMachine()
                print "MK --> Machine '" + m.group(1) + "' instantiated"
                #print self.machine.keys()
                return None
            m = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)\.states\s?=\s?\(\s?((\w+(\s?,\s?)?)+)\s?\)',inp)
            if m:
                self.process_state(m.group(1), m.group(2))
                return None
            m = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)\.initial_state\s?=\s?(\w+)',inp)
            if m:
                self.process_init_state(m.group(1), m.group(2))
                return None
            m = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)\.final_states\s?=\s?\(\s?((\w+(\s?,\s?)?)+)\s?\)',inp)
            if m:
                self.process_final_state(m.group(1), m.group(2))
                return None
            m = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)\.read_input',inp)
            if m:
                self.inp_reader(m.group(1), '', True)
                return None
            m = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)\.display_transition_function',inp)
            if m:
                if m.group(1) not in self.machine:
                    raise MachineInitException(self.line_count)
                self.machine[m.group(1)].disp_transition_fn()
                return None
            m = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)\.run_TM_in_step',inp)
            if m:
                if m.group(1) not in self.machine:
                    raise MachineInitException(self.line_count)
                self.machine[m.group(1)].execute(True)
                return None
            m = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)\.run_TM',inp)
            if m:
                if m.group(1) not in self.machine:
                    raise MachineInitException(self.line_count)
                self.machine[m.group(1)].execute(False)
                return None
            m = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)\.input\s?=\s?(\w+)',inp)
            if m:
                self.inp_reader(m.group(1), m.group(2), False)
                return None
            m = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)\.T\s?\((\s?\w+\s?,\s?\w\s?)\)\s?=>\s?\(\s?(\w+\s?,\s?\w\s?,\s?[RL])\s?\)',inp)
            if m:
                self.trans_fn(m.group(1), m.group(2), m.group(3))
                return None
            m = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)\.initiate_again', inp)
            if m:
                if m.group(1) not in self.machine:
                    raise MachineInitException(self.line_count)
                self.machine[m.group(1)].reinit()
            else:
                raise SyntaxRecogException(self.line_count)
        except (MachineInitException) as s:
            print s
