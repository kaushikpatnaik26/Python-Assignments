class Dog:
    def speak(self):
        return "Woof!"

class Robot:
    def speak(self):
        return "Beep Boop!"

def describe(entity):
    print(entity.speak())
dog = Dog()
robot = Robot()
describe(dog)
describe(robot)
