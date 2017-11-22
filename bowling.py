def score(game):
    result = 0
    frame = 1
    is_first_try = True
    last_score = 0
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last_score
        else:
            result += get_value(game[i])
        
        if frame < 10  and (game[i].lower() == 'x' or game[i] == '/'):
            result += get_value(game[i+1])
            if game[i].lower() == 'x':
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
                    
        last_score = get_value(game[i])

        if game[i].lower() == 'x' or is_first_try == False:
            is_first_try = True
            frame += 1
        elif is_first_try == True:
            is_first_try = False
    return result

def get_value(char):
    if char in [str(num) for num in range(1, 10)]:
        return int(char)
    elif char.lower() == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
        

