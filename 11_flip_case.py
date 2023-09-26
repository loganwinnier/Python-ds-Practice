def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # TODO: consolidate if statement and variable reassignment
    new_str = ""
    for letter in phrase:
        if letter == to_swap.lower() or letter == to_swap.upper():
            new_str += letter.swapcase()
        else:
            new_str += letter
    return new_str
