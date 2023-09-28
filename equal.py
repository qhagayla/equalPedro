import unittest

def fun(x):
    return x == "PEDRO"

class MyTest(unittest.TestCase):
    def test(self):
        assertTrue(fun("PEDRO"), true)

if __name__ == '__main__':