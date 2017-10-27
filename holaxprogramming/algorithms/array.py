class Array(object):

    def __init__(self, array_string):
        self.array_string = array_string

    def sum(self, size):
        numbers = [int(number) for number in self.array_string.split(' ')]

        if size != len(numbers):
            print('error')
            raise Exception('array size is not matched')
            print('raise')

        return sum(numbers)
