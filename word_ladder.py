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
    ['stone', 'shone', 'phone', 'phony',
    'peony', 'penny', 'benny', 'bonny',
    'boney', 'money']
    ```
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots',
    'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    dictionary_file = open(dictionary_file)
    word_list = dictionary_file.read().split('\n')
    if start_word == end_word:
        return [start_word]
    word_stack = []
    word_stack.append(start_word)
    word_queue = deque()
    word_queue.append(word_stack)
    while(len(word_queue) != 0):
        word_temp_stack = word_queue.popleft()
        for word in list(word_list):
            if _adjacent(word_temp_stack[-1], word):
                if word == end_word:
                    word_temp_stack.append(word)
                    return word_temp_stack
                word_perm_stack = copy.copy(word_temp_stack)
                word_perm_stack.append(word)
                word_queue.append(word_perm_stack)
                word_list.remove(word)
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
    if ladder is None or ladder == []:
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
    if len(word1) != len(word2):
        return False
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count == 1
