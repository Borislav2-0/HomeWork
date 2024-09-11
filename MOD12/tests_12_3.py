from runner import *
import runner_2 as rn
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Frol')
        for _ in range(10): runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Foma')
        for _ in range(10): runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner = Runner('Vera')
        runner_1 = Runner('Aglaya')
        for _ in range(10): runner.walk()
        for _ in range(10): runner_1.run()
        self.assertNotEqual(runner.distance, runner_1.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        global all_res
        all_res = {}

    def setUp(self):
        self.runner1 = rn.Runner('Usain', 10)
        self.runner2 = rn.Runner('Andrey', 9)
        self.runner3 = rn.Runner('Nik', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in all_res.items():
            print(value)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        us_nik = rn.Tournament(90, self.runner1, self.runner3)
        res = us_nik.start()

        race = ""
        for key, value in res.items():
            race += str(key) + ": " + str(value) + " "
        all_res["1"] = race

        self.assertTrue(res[2] == "Nik", "Incorrect name of the last runner in race 1")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        andr_nik = rn.Tournament(90, self.runner2, self.runner3)
        res = andr_nik.start()

        race = ""
        for key, value in res.items():
            race += str(key) + ": " + str(value) + " "
        all_res["2"] = race

        self.assertTrue(res[2] == "Nik", "Incorrect name of the last runner in race 2")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        runners = rn.Tournament(90, self.runner1, self.runner2, self.runner3)
        res = runners.start()

        race = ""
        for key, value in res.items():
            race += str(key) + ": " + str(value) + " "
        all_res["3"] = race

        self.assertTrue(res[3] == "Nik", "Incorrect name of the last runner in race 3")


if __name__ == '__main__':
    unittest.main()
