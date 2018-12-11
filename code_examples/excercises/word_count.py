from collections import Counter


def get_odd_squares_list(numbers):
    """
    Return list of tuples (value, square value) for odd values only)
    Use for loop to iterate over numbers, process only odd values (value % 2 == 0)

    :param numbers: collection of numbers (int)
    :return: list of tuples where tuple (value, square value)
    """
    return [(val, val**2) for val in numbers if val % 2 == 0]


def get_word_count_dict(words_str):
    """
    Split word sting with split()

    :param words_str: String with words
    :return: dictionary, which keys are words and values are word occurrence.
    """
    word_counter = Counter()
    for word in words_str.split():
        word_counter[word] += 1
    return dict(word_counter)
