"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """

    print items[0]
    print items[1]
    print items[2]
    print items[3]
    print items[4]

print_list([1,2,6,3,9])


def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """

    return [word for word in words if len(word) > 4]

long_words(["hello", "a", "b", "hi", "bacon", "bacon"])


def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    return [word for word in words if len(word) > n]

n_long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"], 3)
n_long_words(["I", "like", "apples", "bananas", "you"], 5)


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """

    if not numbers:                 #test if list is empty
        return None
    else:
        test = 100                  #establish high ceiling
        for i in numbers:
            if i < test:
                test = i
        found_smallest_int = test   #test is complete
    return found_smallest_int   #returned variable is clearly named

smallest_int([-5, 2, -5, 7])
smallest_int([3, 7, 2, 8, 4])
smallest_int([]) is None


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """

    if not numbers:                 #test if list is empty
        return None
    else:
        test = 0                    #establish low floor
        for i in numbers:
            if i > test:
                test = i
        found_largest_int = test    #test is complete
    return found_largest_int        #returned variable is clearly named

largest_int([-5, 2, -5, 7])
largest_int([3, 7, 2, 8, 4])
largest_int([]) is None


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """

    return [float(num)/2 for num in numbers]

halvesies([2, 6, -2])
halvesies([1, 5])


def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """

    return [len(word) for word in words]

word_lengths(["hello", "hey", "hello", "spam"])


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """

    custom_sum = 0
    for num in numbers:
        custom_sum = custom_sum + num
    return custom_sum

sum_numbers([1, 2, 3, 10])
sum_numbers([])


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """

    custom_product = 1
    for num in numbers:
        custom_product = custom_product * num
    return custom_product

mult_numbers([1, 2, 3])
mult_numbers([10, 20, 0, 50])
mult_numbers([])


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """

    custom_join = ""
    for word in words:
        custom_join = custom_join + "{}".format(word)
    return custom_join

join_strings(["spam", "spam", "bacon", "balloonicorn"])
join_strings([])


def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    and feel free to provide a good solution here.)
    """

    custom_average_numerator = 0
    for num in numbers:
        custom_average_numerator = custom_average_numerator + num
        custom_average_denomenator = len(numbers)
    custom_average = float(custom_average_numerator) / custom_average_denomenator
    return custom_average

average([2, 4])
average([2, 12, 3])


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    custom_join_with_comma = "{}".format(words[0])
    for word in words:
        if words.index(word) > 0:
            custom_join_with_comma = custom_join_with_comma + ", {}".format(word)
    return custom_join_with_comma


join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
join_strings_with_comma(["Pretzel"])


def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """

    return items[-1::-1]

reverse_list([1, 2, 3])
reverse_list(["cookies", "love", "I"])


def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """
    #unsolved

    #doesn't mutate list in-place:
    #items = items[-1::-1]
    return

orig = [1, 2, 3]
reverse_list_in_place(orig)
orig

orig = ["cookies", "love", "I"]
reverse_list_in_place(orig)
orig


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """

    #unsolved

    return []

duplicates(["apple", "banana", "banana", "cherry", "apple"])
duplicates([1, 2, 2, 4, 4, 4, 7])

orig = ["apple", "apple", "berry"]
duplicates(orig)
orig


def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """

    #unsolved

    indices_containing_letter = []

    for word in words:
        if letter in word:
            indices_containing_letter.append(words.index(word))
            #need new method to find index^
        else:
            indices_containing_letter.append(None)

    return indices_containing_letter

find_letter_indices(['odd', 'dog', 'who'], 'o')
find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
