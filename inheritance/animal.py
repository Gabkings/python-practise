class Animal:
    def __init__(self,name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f'{self.name} is a {self.species} species'

class Cat(Animal):
    def __init__(self,name,breed,age):
        super().__init__(name,species = 'Cat')
        self._breed = breed
        self._age = age
    @property
    def age(self):
        return self._age
    @property
    def breed(self):
        return self._breed
    

blue = Cat('Meow','black and white',3)
print(blue.age)
print(blue.breed)
