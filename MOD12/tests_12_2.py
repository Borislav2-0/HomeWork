import runner_2 as rn
import unittest


class TournamentTest(unittest.TestCase):

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

    def test_run_1(self):
        us_nik = rn.Tournament(90, self.runner1, self.runner3)
        res = us_nik.start()

        race = ""
        for key, value in res.items():
            race += str(key) + ": " + str(value) + " "
        all_res["1"] = race

        self.assertTrue(res[2] == "Nik", "Incorrect name of the last runner in race 1")

    def test_run_2(self):
        andr_nik = rn.Tournament(90, self.runner2, self.runner3)
        res = andr_nik.start()

        race = ""
        for key, value in res.items():
            race += str(key) + ": " + str(value) + " "
        all_res["2"] = race

        self.assertTrue(res[2] == "Nik", "Incorrect name of the last runner in race 2")

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
