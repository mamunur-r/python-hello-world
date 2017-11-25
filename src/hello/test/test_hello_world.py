"""

"""
import unittest
from src.hello.hello_world import Hello


class HelloTest(unittest.TestCase):
    """
    all unit tests
    """

    def setUp(self):
        self.hw = Hello()

    def test_hello_me(self):
        response = self.hw.hello_me('Hello')

        self.assertEqual(response,'You said Hello to me!')



