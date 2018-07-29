#!/user/bin/env python
'''Retrieve and print words from a URL.

Usage:
    python words.py <URL>
'''

from urllib.request import urlopen
import sys


def fetchwords(url):
    '''Fetch a list of words from a URL

    Args:
        url: The URL of a UTF-8 test document.

    Returns:
        A list of strings containing the words from the document
    '''
    with urlopen(url) as story:
        story_words = []
        for line in story:
            # adding words from our fetch into the story_words array
            # line by line, while decoding them from bytes to strings
            story_words.extend(line.decode('utf-8').split())
    return story_words


def print_items(items):
    '''Prints items one per Line.

    Args:
        An iterable containing items to be printed.
    '''
    for item in items:
        print(item)


def main(url):
    '''Print each word form a text document from an URL.

    Args:
        url: the URL of a UTF-8 encoded text document
    '''
    words = fetchwords(url)
    print_items(words)


if __name__ == '__main__':
    # this check is important to see, if our script is being executed
    # directly or imported into another script

    main(sys.argv[1])  # this accesses the first parameter given by the user,
    # as [0] represents the script filename
