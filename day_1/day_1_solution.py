### goal: out of groups divided by new lines, sum each of the groups together. 
### Out of the all of the groups, which has the highest sum! But it's fun cuz it's with elves. 

test_text = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
### extract challenge text
with open('day_1_input.txt') as f: 
    challenge_text = f.read()


def day_1_solution(input):
    ### simply just sum the groups and then return the maximum value
    sum_list = sum_groups(input)

    return max(sum_list)

def sum_groups(input):
    cleaned_groups = chunk_groups(input)
    
    ### for all of the cleaned group, we are going to sum the value and then append that to another list
    sum_list = []

    for group in cleaned_groups: 
        sum_calories = sum(group)
        sum_list.append(sum_calories)

    return sum_list

def sort_sum_groups(input):
    ### this is needed for the part 2 answer
    sum_list = sum_groups(input)
    sum_list.sort(reverse=True)
    answer_list = sum_list[0:3]

    return sum(answer_list)


def chunk_groups(input):
    ### just group the ones that aren't split by a double line
    input_groups_double_lines = input.split('\n\n')

    ### let's set an empty list to append to
    input_groups = []

    ### now split each for the groups by the new line & append it to the empty list
    for raw_groups in input_groups_double_lines: 
        num_groups_raw = raw_groups.split('\n')
        input_groups.append(num_groups_raw)

    ### lastly I just need to remove the empty '' for the starts & ends. Plus convert all the strings to ints
    num_groups_cleaned = []

    for group in input_groups: 
        cleaned_inner_group = []
        for value in group: 
            if value == '':
                pass
            else: 
                cleaned_inner_group.append(int(value))
        
        ### lastly append the cleaned group to the bigger one
        num_groups_cleaned.append(cleaned_inner_group) 
    
    return num_groups_cleaned

### show solution
print(day_1_solution(challenge_text))

### for part two, I just have to return the top 3, which I should already have! 
print(sort_sum_groups(challenge_text))