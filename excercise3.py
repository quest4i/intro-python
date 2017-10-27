# 3.1
year_lists = [1980, 1981, 1982, 1983, 1984]


# 3.2
print('세 번째 생일의 년도: ', year_lists[2])


# 3.3
print('가장 나이가 많을 때의 년도: ', year_lists[-1])


# 3.4
things = ['mozzarella', 'cinderella', 'salmonella']


print(things[1].capitalize())
print(things)

print(things[0].upper())
things.pop()
print(things)


# 3.8
surprise = ['Groucho', 'Chico', 'Harpo']

print(surprise[-1].lower()[::-1].capitalize())


# 3.10
f2e = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(f2e)

for k, v in f2e.items():
    if v == 'chien':
        print(k)

print(list(f2e.keys()))


# 3.15
life = {'animal': {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'}, 'plants': {}, 'other': {}}
print(life)
print('3.17')
print(life['animal']['cats'])
