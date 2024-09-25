from cs50 import get_int

def firstform(height):
    hash = ''
    for i in range(height):
        hash += '#'
        print(hash)

def spaceform(height):
    height = height - 1
    new = ''
    for i in range(height):
        new = '#' * height
        print(new)
        height -= 1

def centerspace(height):
    space = '&&'
    for i in range(height):
        print(space)

while True:
    get = get_int("Height: ")
    if get > 1:
        break

if get < 1 or get > 8:
    print("invalid number")
else:
    spaces_side = spaceform(get)
    hashes_side = firstform(get)
    center_space = centerspace(get)
    firstform(get)

