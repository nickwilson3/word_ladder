from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):

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
    dictionary.remove(start_word)
    queue = deque([])
    queue.append(stack)

    while len(queue) != 0:
        stack2 = queue.popleft()
        dictionary_copy = copy.deepcopy(dictionary)
        for word in dictionary_copy:
            if _adjacent(word, stack2[-1]):
                if word == end_word:
                    stack2.append(word)
                    return stack2
                new_stack = copy.deepcopy(stack2)
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
    if len(ladder) == 0:
        return False
    for i in range(len(ladder) - 1):
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
    if (len(word1) != len(word2)):
        return False
    differ = 0
    for i in range(0, min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            differ += 1
    return differ == 1
