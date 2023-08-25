import unittest
import hw0


class Hw0Test(unittest.TestCase):
    def test_verify_msg(self):
        self.assertEqual('Hello World', hw0.msg(), 'Unexpected message')
