'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # 1. what is my base case?
    if len(str(word)) == 2:
        return word
    
    if len(str(word)) > 0:
        if 'th' in str(word.lower()):
            count_th(len(str(word)) - 1)

    # 2. I think I need to go through each char in the string
    # 3. find out how many times 'th' presents itself
    
