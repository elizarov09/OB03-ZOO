import configparser

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Some generic sound")

    def eat(self):
        print(f"{self.name} is eating")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says tweet")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} says woof")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} says hiss")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def show_animals(self):
        for animal in self.animals:
            print(f"Animal: {animal.name}, Age: {animal.age}")

    def save_to_file(self, filename):
        config = configparser.ConfigParser()
        for index, animal in enumerate(self.animals, start=1):
            section = f"Animal{index}"
            config[section] = {}
            config[section]['Name'] = animal.name
            config[section]['Age'] = str(animal.age)
            config[section]['Type'] = animal.__class__.__name__
        with open(filename, 'w') as configfile:
            config.write(configfile)
        print("Data saved to file.")

    def load_from_file(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)
        for section in config.sections():
            animal_type = config[section]['Type']
            name = config[section]['Name']
            age = int(config[section]['Age'])
            if animal_type == "Bird":
                self.animals.append(Bird(name, age))
            elif animal_type == "Mammal":
                self.animals.append(Mammal(name, age))
            elif animal_type == "Reptile":
                self.animals.append(Reptile(name, age))
        print("Data loaded from file.")

# Пример использования
zoo = Zoo()
bird = Bird("Tweety", 2)
dog = Mammal("Rex", 5)
snake = Reptile("Sly", 4)
zoo.add_animal(bird)
zoo.add_animal(dog)
zoo.add_animal(snake)
keeper = ZooKeeper("John")
vet = Veterinarian("Dr. Smith")
zoo.add_staff(keeper)
zoo.add_staff(vet)

# Сохраняем данные в файл
zoo.save_to_file("zoo_data.ini")

# Предполагается, что для загрузки данных будет использоваться новый экземпляр Zoo
new_zoo = Zoo()
new_zoo.load_from_file("zoo_data.ini")
new_zoo.show_animals()
