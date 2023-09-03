class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print ('My name is', self.name)
    def walk(self, x):
        self.position[0] = self.position[0] + x
        print ('New position is', self.position)
    def eat(self):
        print ('I am hungry!')        
class Robot_Dog(Robot):
    def make_noise(self):
        print ('Woof! Woof!')
    def eat(self):
        super().eat()
        print ('I like bacon!')         

#Main program
my_robot_dog = Robot_Dog('Rover')
my_robot_dog.eat()
my_robot_dog.walk(5)
my_robot_dog.make_noise()
