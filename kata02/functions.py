def chop(number, array_of_numbers):

    if number not in array_of_numbers:
        return -1
    else:
        cropped_array = list(array_of_numbers)
        crop_point = 0

        while cropped_array:

            if len(cropped_array) == 1:
                return crop_point

            half_point = len(cropped_array)/2

            if number in cropped_array[:half_point]:
                cropped_array = cropped_array[:half_point]
            else:
                cropped_array = cropped_array[half_point:]
                crop_point += half_point
