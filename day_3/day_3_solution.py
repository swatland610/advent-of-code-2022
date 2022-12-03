# Part 1 Goal: 
### 1. split each line into two equal groups
### 2. find the case-sensitve match that exists in both
### 3. take the match, and then assign a value. (lowercase 1 - 26, and upper case 27 - 52)
### 4. sum all the of the matched letter scores and return the value

### imports
import string

### read in text file & cleanly set it in a list
with open('input.txt') as f: 
    raw_lines = f.readlines()
    lines = [line.replace('\n', '') for line in raw_lines]

# this chunker is for part 2
def group_every_three_lines(lines):
    every_three = []

    for i in range(0, len(lines), 3):
        every_three.append(lines[i:i+3])

    return every_three

# this chunker is for part 1
def split_lines_into_chunks_of_two(lines):
    chunked_lines = []
    for string in lines: 
        chunked_lines.append(split_string_into_chunks(string))

    return chunked_lines

def split_string_into_chunks(string, chunk=2):
    '''
    Input > takes in a string, and splits it into whatever number is set as chunks
    Returns > list of string split in chunks
    '''
    string_length = len(string)
    return [string[i:i+int((string_length/chunk))] for i in range(0, string_length, int(string_length/chunk))]

def find_case_sens_match(string_chunks):
    '''
    Input > takes in a list of strings (designed for two at the start), find any matching characters between the strings
    Return > a list of any matched characters - so that find unique matches
    '''
    if len(string_chunks) == 3:
        unique_matches = list(set([letter for letter in string_chunks[0] if letter in string_chunks[1]])) # using the set() function to reduce unique characters

        ### now run it again, but against the last chunk since we have one more list to check for part 2
        unique_matches = list(set([letter for letter in unique_matches if letter in string_chunks[2]]))

    else: 
        # we just need to check for 2 strings, since this should be for part 1
        unique_matches = list(set([letter for letter in string_chunks[0] if letter in string_chunks[1]])) # using the set() function to reduce unique characters 

    return unique_matches

def assemble_unique_matches_list(input_lines, chunking_function):
    '''
    Input > take in the full set of lines, divide it into chunks, and then run the case sens match
    Return > a list of all of the unique matches found within the lines
    '''

    string_chunks = chunking_function(input_lines)
    unique_matches = [find_case_sens_match(string) for string in string_chunks]

    ### since this returns a list of lists, let's go through every value and set it in one list
    result_list = []
    for match in unique_matches:
        for value in match:
            result_list.append(value)

    return result_list

def sum_priority_score(lines):
    alpha_list = string.ascii_lowercase + string.ascii_uppercase
    # bring in match list
    match_list = assemble_unique_matches_list(lines, group_every_three_lines)

    #set score
    score = 0

    for match in match_list: 
        score = score + (alpha_list.index(match) + 1)

    return score

### used for both solutions
print(sum_priority_score(lines))

# Goal Part 2: 
### 1. Create Chunks where every set of 3 lines is a chunk
### 2. Find the unique matches from those chunks
### 3. Sum those unique matches together

### I can tweak existing code by just creating a new grouping function and plugging that into a function. 