'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # 1. what is my base case?
    # count = 0

    if len(word) < 2:
        return 0
    elif word[0:2] == "th":
        # count += 1
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])


    # 2. I think I need to go through each char in the string
    # 3. find out how many times 'th' presents itself
    
