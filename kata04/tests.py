import unittest
import os

from functions import (checkFileIsReadable, current_directory,
                       checkFileHasValidSuffix, processWeatherData)


class WeatherTest(unittest.TestCase):

    def setUp(self):
        self.dat_file = os.path.join(self.current_directory, 'weather.dat')

    def test_missing_file_raises_io_error(self):
        self.nonsense_dat = os.path.join(self.current_directory,
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

    def test_file_has_excepted_header_values(self):
        processWeatherData(self.dat_file)

        # Dy MxT   MnT   AvT   HDDay  AvDP 1HrP TPcpn WxType PDir AvSp Dir MxS SkyC MxR MnR AvSLP


if __name__ == '__main__':
    unittest.main()
