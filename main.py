from Animal import Animal
from AnimalFunctions import AnimalFunctions


def main():
    animal = Animal("Боня")
    animal_f = AnimalFunctions(animal)
    animal_f.say()  # Привет! Это животное по кличке Боня!
    animal_f.fly()  # Боня умеет летать!
    animal_f.swim()  # Боня теперь умеет плавать!


if __name__ == '__main__':
    main()
