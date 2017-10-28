poem = '''There was young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

try:
    fout = open('relativity', 'xt')
    size= len(poem)
    offset = 0
    chunk = 100
    while True:
        if offset > size:
            break
        fout.write(poem[offset:offset+chunk])
        offset += chunk
    fout.close()
except FileExistsError:
    print('relativity already exists!. That was a close one.')


fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print(len(poem))



poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
print(len(poem))


poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line

fin.close()
print(len(poem))


poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line
fin.close()
print(len(poem))


fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
print(type(lines))
for line in lines:
    print(line, end='')


