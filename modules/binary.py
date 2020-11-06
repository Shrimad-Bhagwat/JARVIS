
print("Loading Databases...")
print("All Systems ready...")
''' This file is used for Binary conversions..'''

def encode(a):

    
    x=(' '.join(format(ord(x), 'b') for x in a))
    return x

def decode(q):
    
    z=str(q)
    binary_values = z.split()
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    
    return ascii_string
