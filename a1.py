class Dog:
    species = "Bulldog"

    def_init_(self,name,breed):
       self.name = name
       self.breed = breed
    
    def display(self):
        print("Name:",self.name)
        print("Breed:",self.breed)
        print("Species:", Dog.species)

dog1 = Dog("tom","american bulldog")
dog2 = Dog("max","English bulldog")
print("Details of Dog 1:")
dog1.display()
print("\nDeltails of dog 2:")
dog2.display()