from abc import ABC, abstractmethod


class Animal(ABC):

  def __init__(self, name, habitat):
    self.name = name
    self.habitat = habitat

  def display(self):
    print(f"Name: {self.name}, Habitat: {self.habitat}")

  @abstractmethod
  def speak(self):
    pass


class Dog(Animal):  # Fixed capitalization to match instantiation

  def __init__(self, name, habitat, breed):
    super().__init__(name, habitat)
    self.breed = breed

  def display(self):
    super().display()
    print(f"Breed: {self.breed}")

  def speak(self):
    print(f"{self.name} the {self.breed} barks: Woof!")


class Parrot(Animal):

  def __init__(self, name, habitat, phrase):
    super().__init__(name, habitat)
    self.phrase = phrase

  def display(self):
    super().display()
    print(f"Phrase: {self.phrase}")

  def speak(self):
    print(f"{self.name} the Parrot says: {self.phrase}")


class Lion(Animal):

  def __init__(self, name, habitat, pride):
    super().__init__(name, habitat)
    self.pride = pride

  # Added display method for consistency across all child classes
  def display(self):
    super().display()
    print(f"Pride: {self.pride}")

  def speak(self):
    print(f"{self.name} the Lion growls: Roar!")


# Fixed variable capitalization (Dog with a capital D)
dog = Dog("Bruno", "home", "labrador")
parrot = Parrot("Polly", "trees", "Hello, how are you?")
lion = Lion("Simba", "savannah", "Circle")

print("===Animal sound show===")
for animal in [dog, parrot, lion]:
  animal.display()
  animal.speak()
  print()