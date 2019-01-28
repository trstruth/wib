from st2actions.runners.pythonrunner import Action

class IsEven(Action):
    def __init___(self, config):
        super(self.__class, self).__init__(config)

    def run(self, num):
        remainder = num % 2
        is_even = remainder == 0
        return (is_even, 'num is even' if is_even else 'num is odd')

