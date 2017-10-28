import unicodedata
import re
import binascii
import struct


# 7.1
mystery = '\U0001f4a9'
print(mystery)
name = unicodedata.name(mystery)
print(name)


# 7.2
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)


# 7.3
pop_string = pop_bytes.decode('utf-8')
print(pop_string)
print(pop_string == mystery)


# 7.4
poem ='''
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s,
And now thinks he's a %s.
'''
args = ('roast beef', 'ham', 'head', 'clam')
print(poem % args)


# 7.5
letter = '''
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send your another {product} that, in our tests, is {percent}% less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}
'''


# 7.6
response = {
    'salutation': 'Colonel',
    'name': 'Hackenbush',
    'product': 'duck blind',
    'verbed': 'imploded',
    'room': 'conservatory',
    'animals': 'emus',
    'amount': '$1.38',
    'percent': '1',
    'spokesman': 'Edgar Schmeltz',
    'job_title': 'Licensed Podiatrist'
}
print(letter.format(**response))


# 7.7
mammoth = '''
we have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees, 
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a sahde even at noon,
folks would think it was the moon
About to fall and crush them soon.
'''


# 7.8
pat = r'\bc\w*'
result = re.findall(pat, mammoth)
print(result)


# 7.9
pat = r'\bc\w{3}\b'
result = re.findall(pat, mammoth)
print(result)


# 7.10
pat = r"\b\w*r\b"
result = re.findall(pat, mammoth)
print(result)

pat = r"\b[\w']*l\b"


# 7.11
pat = r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b'
result = re.findall(pat, mammoth)
print(result)


# 7.12
hex_str = '47494638396101000100080000000000ffffff21f9' + '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(hex_str)
print(len(gif))


# 7.13
print(gif[:6] == b'GIF89a')
print(b'GIF89a')


# 7.14
width, height = struct.unpack('<HH', gif[6:10])
print(width, height)
