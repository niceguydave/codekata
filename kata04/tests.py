import unittest
import os

from functions import checkFileIsReadable


class WeatherTest(unittest.TestCase):

    __location__ = os.path.realpath(os.path.join(os.getcwd(),
                                                 os.path.dirname(__file__)))

    def setUp(self):
        self.dat_file = os.path.join(self.__location__, 'weather.dat')

    def test_missing_file_raises_io_error(self):
        self.nonsense_dat = os.path.join(self.__location__, 'not-here.dat')
        self.assertFalse(os.path.exists(self.nonsense_dat))
        self.assertRaises(IOError, checkFileIsReadable, self.nonsense_dat)


if __name__ == '__main__':
    unittest.main()
