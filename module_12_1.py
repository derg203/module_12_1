import test2
import unittest
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        den = test2.Runner('den')
        for i in range(10):
            den.walk()
        self.assertEqual(den.distance,50)
    def test_run(self):
        den = test2.Runner('den')
        for i in range(10):
            den.run()
        self.assertEqual(den.distance,100)
    def test_challenge(self):
        denis = test2.Runner('denis')
        danil = test2.Runner('danil')
        for i in range(10):
            denis.walk()
            danil.run()
        self.assertNotEqual(denis.distance,danil.distance)

