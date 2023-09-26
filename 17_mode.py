def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # TODO: improve runtime by using regular freq counter
    counts = {num: nums.count(num) for num in nums}

    max = 0
    max_key = ""
    for key, val in counts.items():
        if val > max:
            max = val
            max_key = key
    return max_key
