UP = [1,0,0,0,0,0,0,0,0]
DOWN = [0,1,0,0,0,0,0,0,0]
LEFT = [0,0,1,0,0,0,0,0,0]
RIGHT = [0,0,0,1,0,0,0,0,0]
UP_LEFT = [0,0,0,0,1,0,0,0,0]
UP_RIGHT = [0,0,0,0,0,1,0,0,0]
DOWN_LEFT = [0,0,0,0,0,0,1,0,0]
DOWN_RIGHT = [0,0,0,0,0,0,0,1,0]
NO_KEY = [0,0,0,0,0,0,0,0,1]

UP_HEX = 0x26
DOWN_HEX = 0x28
LEFT_HEX = 0x25
RIGHT_HEX = 0x27

def get_key_vector(keys):

    output = [0,0,0,0,0,0,0,0,0]
    
    if UP_HEX in keys and LEFT_HEX in keys:
        output = UP_LEFT
    elif UP_HEX in keys and RIGHT_HEX in keys:
        output = UP_RIGHT
    elif DOWN_HEX in keys and LEFT_HEX in keys:
        output = DOWN_LEFT
    elif DOWN_HEX in keys and RIGHT_HEX in keys:
        output = DOWN_RIGHT
    elif UP_HEX in keys:
        output = UP_HEX
    elif DOWN_HEX in keys:
        output = DOWN_HEX
    elif LEFT_HEX in keys:
        output = LEFT_HEX
    elif RIGHT_HEX in keys:
        output = RIGHT_HEX
    else:
        output = NO_KEY
    return output
