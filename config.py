# dictionary should be a list with one word per element - no spaces!
# by default this reads OS dictionary on *nix, on other operating systems, get dictionary from the web.

max_wordlen = 6

def filterwords(word):
    if "\'s" not in word and len(word) <= max_wordlen:
        return True
    else:
        return False

rawdict = open("/usr/share/dict/words", "r").read().splitlines()
dict = list(filter(filterwords, rawdict))

# number of words to use in a sprint, type: int
# I reccomend 50-100 words for the best balance between time and accuracy

sprintLen = 50

# whether you see what you're typing or not. type: bool
# It is *highly* reccomended that you set this to True, as being able to see what you type means you tend to go back and correct your errors, which is not what we want.

textInvisible = True
