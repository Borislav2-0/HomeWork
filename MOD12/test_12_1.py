from runner import *
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Frol')
        for _ in range(10): runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Foma')
        for _ in range(10): runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner = Runner('Vera')
        runner_1 = Runner('Aglaya')
        for _ in range(10): runner.walk()
        for _ in range(10): runner_1.run()
        self.assertNotEqual(runner.distance, runner_1.distance)

if __name__ == '__main__':
    unittest.main()
