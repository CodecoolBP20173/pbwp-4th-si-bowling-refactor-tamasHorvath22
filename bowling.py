def score(game):
    """ Gets a parameter 'game', which is a string.
    This contains the scores of a player. This function
    turns the string into score. Returns an integer"""
    result = 0
    frame = 1
    is_first_try = True
    last_score = 0
    for i in range(len(game)):
        result += if_spare(game[i], last_score)
        
        if frame < 10  and (game[i].lower() == 'x' or game[i] == '/'):
            result += get_value(game[i+1])
            if game[i].lower() == 'x':
                result += if_spare(game[i+2], get_value(game[i+1]))
                    
        last_score = get_value(game[i])

        if game[i].lower() == 'x' or is_first_try == False:
            is_first_try = True
            frame += 1
        elif is_first_try == True:
            is_first_try = False
    return result

def if_spare(char, last_score):
    """This function decides if a try was a spare or not.
    Returns the points of the try as an integer."""
    if char == '/':
        points = 10 - last_score
    else:
        points = get_value(char)
    return points

def get_value(char):
    """This function returns the points
    of a try as an integer."""
    if char in [str(num) for num in range(1, 10)]:
        return int(char)
    elif char.lower() == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
        

