"""Generate Markov text from text files."""

import sys
from random import choice
from collections import defaultdict


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path, 'r') as f: # 'r' = read-only
        text = f.read().replace("\n", " ") # read the open file then replace the new-line breaks with whitespaces. 

    return text


def make_chains(text_string, n=2):
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

    # for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
    #     bi_gram = (w1, w2)
    #     chains[bi_gram].append(w3) # if the bigram doesn't exit in the keys, append w3
        # if bi_gram in chains:
        #   chains[bi_gram].append(w3)
        # else:
        #   chains[bi_gram] = [w3]

    for i in range(len(words)-n):
        n_gram = tuple(words[i:(i+n)])
        value_for_n_gram = words[i+n]
        chains[n_gram].append(value_for_n_gram)

    return chains


def make_text(chains, n=2):
    """Return text from chains."""

    words = []

    # your code goes here
    while True:
        if not words:
            start_bigram = choice(list(chains.keys()))
            words.extend(list(start_bigram))
        else:
            possible_next_words = chains[tuple(words[-n:])]
            if not possible_next_words:
                return " ".join(words)
            next_word = choice(possible_next_words)
            words.append(next_word)


#input_path = "green-eggs.txt"

n = 6

# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1])

# Get a Markov chain
chains = make_chains(input_text, n=n)

# Produce random text
random_text = make_text(chains, n=n)

print(random_text)
