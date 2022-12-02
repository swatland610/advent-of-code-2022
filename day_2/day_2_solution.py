### goal: calculate win loss scores based on pattern in input

### dict for win or losses based on input
### win losses are based on YOUR win (so XYZ) - not the opponent 'ABC'
win_loss_dict = {
    'A':
        {'X':'draw',
         'Y':'win',
         'Z':'loss'},
    'B':
        {'X':'loss',
         'Y':'draw',
         'Z':'win'},
    'C':
        {'X':'win',
         'Y':'loss',
         'Z':'draw'}
}

### for part two, I need to change the approach - since XYZ becomes loss, draw, win
win_loss_dict_part_2 = {
    'A':
        {'X':'loss',
         'Y':'draw',
         'Z':'win'},
    'B':
        {'X':'loss',
         'Y':'draw',
         'Z':'win'},
    'C':
        {'X':'loss',
         'Y':'draw',
         'Z':'win'}
}

### store values of your score based on your play
your_select_score_dict = {
    'X':1,
    'Y':2,
    'Z':3
}

your_select_score_dict_part_2 = {
    'A':
        {'X':3,
         'Y':1,
         'Z':2},
    'B':
        {'X':1,
         'Y':2,
         'Z':3},
    'C':
        {'X':2,
         'Y':3,
         'Z':1}
}

### set test input
test_input = """A Y
B X
C Z
"""

with open('input.txt') as f:
    challenge_text = f.read()

# part 1 solution
def sum_total_match_score(input):
    match_list = split_input(input)

    ### extract two unique scores
    score_by_play = determine_score_by_play(match_list)
    score_by_win_loss_draw = determine_win_loss_draw_score(match_list, win_loss_dict)

    return score_by_play + score_by_win_loss_draw

# part 2 solution
def sum_total_match_score_part_2(input):
    match_list = split_input(input)

    ### extract two unique scores
    score_by_play = determine_score_by_play_part_2(match_list)
    score_by_win_loss_draw = determine_win_loss_draw_score(match_list, win_loss_dict_part_2)

    return score_by_play + score_by_win_loss_draw


def determine_score_by_play(match_list):
    ### initiate score
    score = 0

    for match in match_list:
        play_result = your_select_score_dict[match[1]]

        score = score + play_result

    return score

def determine_score_by_play_part_2(match_list):
    score = 0

    for match in match_list:
        play_result = your_select_score_dict_part_2[match[0]][match[1]]

        score = score + play_result
    
    return score

def determine_win_loss_draw_score(match_list, win_loss_map):
    ### initiate score
    score = 0

    for match in match_list: 
        match_result = win_loss_map[match[0]][match[1]]

        if match_result == 'win':
            score = score + 6

        elif match_result == 'draw':
            score = score + 3
        
        else: # for loss
            score = score

    return score

### get input into list of grouped lists
def split_input(input):
    split_list = input.split('\n')
    # iterate to split inner list
    result_list = []
    for value in split_list:
        if value == '':
            pass
        else: 
            inner_group = value.split(' ')
            result_list.append(inner_group)

    return result_list

### this is for the part 1 solution
print(sum_total_match_score(challenge_text))

### this is for the part 2 solution
print(sum_total_match_score_part_2(challenge_text))