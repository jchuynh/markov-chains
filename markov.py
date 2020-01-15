"""Generate Markov text from text files."""

import sys
from random import choice
from collections import defaultdict


def open_and_read_file(*args):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    full_text = []

    for file_path in args[0]:
        # 'r' = read-only
        with open(file_path, 'r') as f:
            # read the open file then replace the new-line breaks with
            # whitespaces.
            text = f.read().replace("\n", " ")
        full_text.append(text)

    return full_text


def make_chains(all_text_strings, n):
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

    n = int(n)

    chains = defaultdict(lambda: [], {}) # with an empty dictionary, we take the list as the default
    # if the key is not in the dictionary, the default is an empty list

    for text_string in all_text_strings:
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


def make_text(chains, end_points=set(['.', '!', '?'])):
    """Return text from chains."""

    words = []
    n = len(list(chains.keys())[0])

    # your code goes here
    while True:
        if not words:
            while True:
                start_bigram = choice(list(chains.keys()))
                if start_bigram[0][0].isupper():
                    break
            words.extend(list(start_bigram))
        else:
            possible_next_words = chains[tuple(words[-n:])]
            if not possible_next_words:
                return " ".join(words)
            next_word = choice(possible_next_words)
            words.append(next_word)
            if next_word[-1] in end_points:
                return " ".join(words)


#input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1:-1])

# Get a Markov chain
chains = make_chains(input_text, sys.argv[-1]) # user enters n value

# Produce random text
random_text = make_text(chains)

print(random_text)
