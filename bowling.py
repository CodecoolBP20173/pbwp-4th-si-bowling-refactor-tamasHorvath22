def score(game):
    result = 0
    frame = 1
    in_first_try = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        
        if frame < 10  and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
                    
        last = get_value(game[i])
        #if in_first_try == False:
        #    frame += 1

        if in_first_try == True:
            in_first_try = False
        else:
            in_first_try = True
            frame +=1
        if game[i] == 'X' or game[i] == 'x':
            in_first_try = True
            frame += 1
    return result

def get_value(char):
    if char in [str(num) for num in range(1, 10)]:
        return int(char)
    elif char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    
        
game = "5/11------------3/11"
print(score(game))