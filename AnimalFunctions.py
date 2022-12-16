class AnimalFunctions(object):
    """Здесь описываются разные функции животного"""

    def __init__(self, animal):
        self._animal = animal

    def __getattr__(self, item):
        return getattr(self._animal, item)

    def fly(self):
        # расширяем функциональность объекта добавляя возможность летать
        print('%s умеет летать!' % self._animal._name)

    def swim(self):
        print('%s теперь умеет плавать!' % self._animal._name)