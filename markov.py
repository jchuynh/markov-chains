"""Generate Markov text from text files."""

from random import choice
from collections import defaultdict


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path, 'r') as f:
        text = f.read().replace("\n", " ").rstrip()
    
    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = defaultdict(lambda: [], {}) # with an empty dictionary, we take the list as the default
    # if the key is not in the dictionary, the default is an empty list

    # your code goes here
    words = text_string.split() # split by whitespace 

    for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
        bi_gram = (w1, w2)
        chains[bi_gram].append(w3) # if the bigram doesn't exit in the keys, append w3

    print(chains)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    while True:
        if not words:
            start_bigram = choice(list(chains.keys()))
            words.extend(list(start_bigram))
        else:
            possible_next_words = chains[(words[-2], words[-1])]
            if not possible_next_words:
                return " ".join(words)
            next_word = choice(possible_next_words)
            words.append(next_word)



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
