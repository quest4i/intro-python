def new_quiz(number):
    print('\n', number, '-'*40)


new_quiz(6.1)


class Thing:
    pass


print('Thing:', Thing)
example = Thing()
print('example: ', example)

new_quiz(6.2)


class Thing2:
    letters = 'abc'


print(Thing2.letters)

new_quiz(6.3)


class Thing3:
    def __init__(self, letters):
        self.letters = letters


print('Yes')

new_quiz(6.4)


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print('name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number))

    def __str__(self):
        return 'name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number)

    #def __repr__(self):
    #    return self.name + ' - ' + self.symbol + ' - ' + str(self.number)


example4 = Element('Hydrogen', 'H', 1)

new_quiz(6.5)
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
example5 = Element(**el_dict)
print(example5)

new_quiz(6.6)
example6 = Element(**el_dict)
example6.dump()

new_quiz(6.7)
print(example6)

new_quiz(6.8)


class Element8:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return 'name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number)


example8 = Element8(**el_dict)
print(example8)

new_quiz(6.9)


class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campus'


bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()
bear.eats()
rabbit.eats()
octothorpe.eats()

new_quiz(6.10)


class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        print('raser=%s, claw=%s, smartphone=%s' % (self.laser.does(), self.claw.does(), self.smartphone.does()))


robot = Robot()
robot.does()


