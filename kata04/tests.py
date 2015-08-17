import unittest
import os

from functions import checkFileIsReadable, checkFileHasValidSuffix


class WeatherTest(unittest.TestCase):

    __this_directory__ = os.path.realpath(os.path.join(os.getcwd(),
                                                 os.path.dirname(__file__)))

    def setUp(self):
        self.dat_file = os.path.join(self.__this_directory__, 'weather.dat')

    def test_missing_file_raises_io_error(self):
        self.nonsense_dat = os.path.join(self.__this_directory__,
                                         'not-here.dat')
        self.assertFalse(os.path.exists(self.nonsense_dat))
        self.assertRaises(IOError, checkFileIsReadable, self.nonsense_dat)

    def test_valid_file_recognised_as_readable(self):
        self.assertTrue(checkFileIsReadable(self.dat_file))

    def test_non_dat_file_raises_value_error(self):
        """Some sample file extensions here - this list could be expanded.
        """
        bad_filepaths = ['file.xls', 'file.csv', 'file.doc', ]
        for bad_file in bad_filepaths:
            self.assertRaises(ValueError, checkFileHasValidSuffix, bad_file)

    def test_dat_file_recognised_as_valid(self):
        self.assertTrue(checkFileHasValidSuffix(self.dat_file))


if __name__ == '__main__':
    unittest.main()
