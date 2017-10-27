import time
from functools import wraps



# 4.1
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')



# 4.2
guess_me = 7
start = 1
while (start <= guess_me):
    if start ==  guess_me:
        print('found it!')
        break
    elif start > guess_me:
        print('oops')
    print('too low')

    start += 1


print('4.3 -------------')
list_a = [3, 2, 1, 0]
for i in list_a:
    print(i)


print('4.4 -------------')
list_4 = [number for number in range(10) if number % 2 == 0]
print(list_4)


print('\n\n4.5 ', '-' * 20)
squares = {index: index**2 for index in range(10)}
print(squares)


print('\n\n4.6 ', '-' * 20)
set_odd = {index for index in range(10) if index % 2 != 0}
print(set_odd)


print('\n\n4.7 ', '-' * 20)


gods = ('God ' + str(number) for number in range(10))
for i in gods:
    print(i)


print('\n\n4.8 ', '-' * 20)


def good():
    return ['Harry', 'Ron', 'Hermione']


print('\n\n4.9 ', '-' * 20)


def get_odds():
    for number in range(1, 10, 2):
        yield number;

for count, number in enumerate(get_odds(), start=1):
    if count == 3:
        print("The third odd number is", number)
        break


print('\n\n4.10 ', '-' * 20)


def test(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        start = time.time()
        print('start')
        result = func(*args, **kwargs)
        end = time.time()
        print('end', end-start)
        return result
    return new_func


@test
def greeting():
    print('Greetings, Earthling')


greeting()


print('\n\n4.11 ', '-' * 20)


class OopsException(Exception):
    print('OopsException class')


# raise OopsException()

try:
    raise OopsException()
except OopsException as ops:
    print('Caught an oops')


# 4.12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)
