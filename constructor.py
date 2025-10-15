
class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def displayInfo(self):
        print('Your name is: ', self.name)
        print('your roll is: ', self.roll)

    def __del__(self):
        print('Object deleted')

n = input('Enter name: ')
roll = int(input('Enter your roll: '))

s = Student(n, roll)
s.displayInfo()
del s
