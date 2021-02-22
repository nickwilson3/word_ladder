#!/bin/python3
from collections import deque
import copy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    with open(dictionary_file) as f:
        new_dictionary = f.readlines()
    
    dictionary = []
    for element in new_dictionary:
        dictionary.append(element.strip())
    
    if start_word == end_word:
        return [start_word]
    if len(start_word) != len(end_word):
        return None
    if _adjacent(start_word, end_word):
        return [start_word, end_word]

    stack = []
    stack.append(start_word)
    queue = deque([])
    queue.append(stack)

    while len(queue) != 0:
        stack2 = queue.popleft()
        for word in list(dictionary):
            if _adjacent(stack[0], word):
                if word == end_word:
                    stack2.append(word)
                    return stack2
                new_stack = copy.copy(stack2)
                new_stack.append(word)
                queue.append(new_stack)
                dictionary.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder is None or len(ladder) < 1:
        return False
    elif len(ladder) == 1:
        return True
    else:
        for i in range(0, len(ladder) -1):
            if not _adjacent(ladder[i], ladder[i + 1]):
                return False
        return True



def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    else:
        differ = 0
        for i in range(0, min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                differ += 1
        return (differ == 1)
