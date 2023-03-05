

class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('dog was created')

    def sit(self):
        print(self.name.title() + ' - dog is sit down')

    def jump(self):
        print(self.name.title() + ' dog was jumped')

myDog = Dog('Topik','4')
secondDog = Dog('loh','7')
print(myDog.age)
print(secondDog.age)

myDog.sit()
