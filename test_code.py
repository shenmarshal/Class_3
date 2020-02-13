# import class_code
# import home_code
import unittest
from myprint import my_print

class Test:

    def test_my_print(self):

        expected = 2
        assert my_print("test", 2) == expected