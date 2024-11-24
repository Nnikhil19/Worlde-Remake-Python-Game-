import random
words = [
    'acorn', 'acrid', 'adapt', 'addle', 'adage',
    'added', 'addle', 'adept', 'adult',
    'admit', 'adopt', 'adore', 'adorn',
    'adust', 'aegis', 'aider', 'aimed', 'alert',
    'alien', 'align', 'alive', 'allay', 'aloof',
    'alter', 'amber', 'amble', 'amuse', 'angel',
    'anger', 'angle', 'angry', 'anode', 'anvil',
    'apple', 'apply', 'argue', 'arise', 'armed',
    'armor', 'aroma', 'arose', 'array', 'arrow',
    'asset', 'aster', 'atone', 'audio', 'augur',
    'aunty', 'await', 'awash', 'bacon', 'badge',
    'baker', 'baldy', 'bambo', 'banjo', 'barge',
    'barky', 'baron', 'batch', 'beach', 'beard',
    'beast', 'beech', 'beefy', 'beige', 'belly',
    'berry', 'binge', 'blaze', 'bliss', 'block',
    'blood', 'boast', 'bloom', 'board', 'boast',
    'brave', 'break', 'broad', 'broom', 'broth',
    'brown', 'brush', 'buddy', 'cabin', 'cacao',
    'canal', 'candy', 'caper', 'charm', 'chase',
    'cheap', 'cheat', 'chill', 'chime', 'chuck',
    'cider', 'civil', 'clean', 'clear', 'climb',
    'clock', 'cloud', 'clown', 'clump', 'coach',
    'craft', 'crash', 'crave', 'creek', 'creep',
    'cross', 'crush', 'curve', 'daily', 'daisy',
    'dance', 'dared', 'debut', 'depth', 'depot',
    'deter', 'devil', 'diner', 'douse', 'draft',
    'dream', 'drill', 'drunk', 'dwell', 'eager',
    'early', 'earth', 'eased', 'easel', 'email',
    'enact', 'enter', 'equal', 'erase', 'event',
    'every', 'exile', 'exile', 'fable', 'feast',
    'fifth', 'flame', 'fleet', 'flint', 'float',
    'force', 'frank', 'fresh', 'fries', 'front',
    'fruit', 'funny', 'fuzzy', 'gavel',
    'gauge', 'gleam', 'glory', 'glove', 'grace',
    'grasp', 'grass', 'great', 'green', 'grief',
    'grind', 'grove', 'guard', 'guide', 'habit',
    'happy', 'harsh', 'heart', 'hence', 'hobby',
    'house', 'hover', 'hurry', 'ideal', 'image',
    'index', 'inbox', 'input', 'irony', 'ivory',
    'jewel', 'joint', 'jolly', 'judge', 'jumpy',
    'junta', 'knife', 'knock', 'label', 'latch',
    'laser', 'lemon', 'libra', 'light', 'liver',
    'lobby', 'loose', 'lucky', 'lunar', 'march',
    'media', 'merge', 'merit', 'model',
    'molar', 'money', 'moral', 'mouse', 'music',
    'nacho', 'noble', 'novel', 'north', 'ocean',
    'olive', 'orbit', 'order', 'other', 'pasta',
    'pearl', 'plant', 'plate', 'plaza', 'pound',
    'pride', 'pride', 'print', 'pulse', 'quail',
    'quark', 'quest', 'quiet', 'radar', 'raise',
    'range', 'ready', 'rebel', 'reign', 'relax',
    'reply', 'reset', 'rival', 'river', 'roast',
    'robot', 'round', 'salad', 'scale', 'scene',
    'score', 'sense', 'sheep', 'shiny', 'shirt',
    'shock', 'short', 'shout', 'sight', 'silly',
    'slope', 'smile', 'sneak', 'sound', 'space',
    'spice', 'scoop', 'screw', 'screw', 'serve',
    'shape', 'shear', 'sheep', 'shift', 'shiny',
    'shirt', 'slick', 'slope', 'slice', 'slope',
    'slush', 'smile', 'snare', 'snake', 'sooth',
    'space', 'spine', 'spoon', 'stage',
    'stand', 'steam', 'stone', 'storm', 'story',
    'stuck', 'style', 'sugar', 'sweet', 'table',
    'tiger', 'touch', 'train', 'trend', 'trick',
    'trust', 'twine', 'tweak', 'twirl', 'under',
    'urban', 'value', 'vapor', 'verse', 'video',
    'vocal', 'vowel', 'water', 'weary', 'wheel',
    'widen', 'wince', 'witty', 'yield', 'youth',
    'zebra', 'zesty', 'zippy', 'zoned', 'zonal'
]

guesses = 1

def print_instructions():
    print("Guess the Wordle in 6 tries.")
    print("Each guess must be a work in a given list.")
    print("A '!' is placed under the letter in the correct spot.")
    print("A '^' is placed under the letter in the wrong spot.")
    print("A 'X' is placed under the letter not in the word.")

print_instructions()

def get_hidden_word(word_list):
    return random.choice(word_list).lower()

# get_random_word(words) test cases - should print a different hidden_word each call
# uncomment to see what the function does, comment out after 
# hidden_word = get_hidden_word(words) 
# print(hidden_word)
# hidden_word = get_hidden_word(words) 
# print(hidden_word)
# hidden_word = get_hidden_word(words) 
# print(hidden_word)


def is_letter_in_word(letter, word):
    return (letter in word)

# is_letter_in_word(letter, word) - test case
# uncomment to see what the function does, comment out after 
# if is_letter_in_word('a', 'apple'):
#     print("The letter is in the word!")
# else:
#     print("The letter is not in the word.")


def check_length_word(user_word):
    user_word = input("Enter a 5 letter word ")
    while len(user_word)!= 5:
        user_word = input("Enter a 5 letter word ")

    return (user_word)

# check_length_word(user_word)
# uncomment to see what the function does, comment out after 
# valid_word = check_length_word(input("Enter a word: ").lower())
# print(valid_word)

def user_word_in_list(user_word, word_list):
    return user_word in word_list

# check_length_word(user_word)
# uncomment to see what the function does, comment out after 
# if user_word_in_list('apple', words):
#     print("The word is in the list!")
# else:
#     print("The word is not in the list.")

def compare_words(user_word, hidden_word):
    return user_word == hidden_word

# compare_words(user_word)
# uncomment to see what the function does, comment out after 
# hidden_word = get_random_word(words) # gets hidden_word
# if compare_words('apple', get_hidden_word(words)):
#     print("Congratulations! You've guessed the word!")
# else:
#     print("Try again.")

def display_spaces(hidden_word):
    final_str = ""
    for i in range(len(hidden_word)):
        final_str+="_ "
    print(final_str)


# uncomment to see what the function does, comment out after 
# hidden_word = get_hidden_word(words) # gets hidden_word
# display_spaces(hidden_word)

def print_word_spaces(user_word):
    for i in range(len(user_word)):
        print(f"{user_word[i]} ", end="")
    print()

# display_spaces(hidden_word)
# uncomment to see what the function does, comment out after 
# print_word_spaces('apple')
# print_word_spaces('house')
# print_word_spaces('print')

def letter_matching(user_word, hidden_word):
    index = 0
    out_str = ""

    for i in range(len(hidden_word)):
        if user_word[i] in hidden_word:
            if user_word[i] == hidden_word[i]:
                out_str+="! "
            else:
                out_str+="^ "
        else:
            out_str+="X "
    return out_str 
# display_spaces(hidden_word)
# uncomment to see what the function does, comment out after 
# result = letter_matching('apple', 'grape')
# print(result) 

def play_wordle(word_list):
    
    hidden_word = get_hidden_word(words)    
    display_spaces(hidden_word)
    
    for i in range(6):
        will_subtract = True
        guessed_word = check_length_word(user_word="").lower()

        print()
        print_word_spaces(guessed_word)

        if user_word_in_list(guessed_word,words)==False:
            will_subtract = False
            print("That word is not in the list!!")
            
        if will_subtract:
            matched_letters = letter_matching(hidden_word=hidden_word,user_word=guessed_word)
            print(matched_letters)
            print(f"{6-(i+1)} guesses left!")

    

play_wordle(words)