def chop(number, array_of_numbers):

    if number not in array_of_numbers:
        return -1
    else:
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
