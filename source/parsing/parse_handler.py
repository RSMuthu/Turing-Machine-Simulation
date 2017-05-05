class MachineInitException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value
    def __str__(self):
        if self.value == '':
            return 'MK --> The Machine should be initiated before use'
        return 'MK --> Line ' + str(self.value) + 'The Machine should be initiated before use'

class SyntaxRecogException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value
    def __str__(self):
        if self.value == '':
            return 'MK --> Syntax Error'
        return 'MK --> Line ' + str(self.value) + ': Syntax Error'

class NotInStateException(Exception):
    def __init__(self, count, value):
        Exception.__init__(self)
        self.count = count
        self.value = value
    def __str__(self):
        if self.count == '':
            return "MK --> " + self.value
        return "MK --> Line " + str(self.count) + ": " + self.value
