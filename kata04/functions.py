#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

current_directory = os.path.realpath(os.path.join(os.getcwd(),
                                     os.path.dirname(__file__)))


def checkFileIsReadable(filepath):
    try:
        open(filepath)
    except IOError, OSError:  # Note OSError is for later versions of python
        raise IOError("Unable to read the supplied file '{}'".format(filepath))
    return True


def checkFileHasValidSuffix(filepath):
    valid_extension = '.dat'
    filename, file_extension = os.path.splitext(filepath)
    if file_extension != valid_extension:
        raise ValueError("Only {} files are valid.")
    return True


def getFirstLineOfFile(filepath):
    with open(filepath, 'r') as f:
        return f.readline()


def convert_data_to_array(filepath):
    data = list()
    with open(filepath, 'r') as f:
        for line in f:
            line_as_array = line.split()
            try:
                int(line_as_array[0])
                data.append(line_as_array)
            except (IndexError, ValueError):
                pass
    return data


def make_safe(string):
    if string.endswith('*'):
        string = string[:-1]
    return float(int(string))


def create_temperature_range_array(data):
    return_list = list()
    for line in data:
        return_list.append([line[0],
                            make_safe(line[1]) - make_safe(line[2])])
    return return_list


def get_day_with_smallest_temp_spread(temperature_data):
    from operator import itemgetter
    return sorted(temperature_data, key=itemgetter(1))[0]


def processWeatherData(filepath):
    checkFileIsReadable(filepath)
    checkFileHasValidSuffix(filepath)
    data = convert_data_to_array(filepath)
    temperature_data = create_temperature_range_array(data)
    result = get_day_with_smallest_temp_spread(temperature_data)
    print ('# Weather\nThe day with the smallest temperature spread '
           'is day {}.\nThe spread is {}').format(result[0], result[1])


if __name__ == '__main__':
    processWeatherData(os.path.join(current_directory, 'weather.dat'))

