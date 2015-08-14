def chop(number, array_of_numbers):

    try:
        int(number) + 1
    except ValueError:
        raise ValueError('number must be an integer')

    try:
        [int(x) for x in array_of_numbers]
    except ValueError:
        raise ValueError('array_of_numbers must contain a list of integers')

    if number not in array_of_numbers:
        return -1

    crop_point = 0
    while array_of_numbers:
        if len(array_of_numbers) == 1:
            return crop_point
        half_point = len(array_of_numbers)/2
        if number in array_of_numbers[:half_point]:
            array_of_numbers = array_of_numbers[:half_point]
        else:
            array_of_numbers = array_of_numbers[half_point:]
            crop_point += half_point
