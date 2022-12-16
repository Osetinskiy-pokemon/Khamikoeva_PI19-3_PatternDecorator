class Animal(object):
    """Животное"""

    def __init__(self, name):
        self._name = name

    def say(self):
        print('Привет! Это животное по кличке %s!' % self._name)