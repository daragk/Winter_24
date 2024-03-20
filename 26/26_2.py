def dis(self):
    for i in self.__dict__:
        print(i, self.__dict__.get(i))

Pet = type('Pet', (), {'dis':dis})
my_pet = Pet()
my_pet.name = 'Vaska'
my_pet.age = 10
my_pet.dis()
