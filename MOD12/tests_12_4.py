import logging
import rt_with_exceptions
import unittest

logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename='runner_tests.log',
    encoding='UTF-8',
    format='%(levelname)s | %(message)s'
)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner_obj_1 = rt_with_exceptions.Runner('John', 5)
        except ValueError as VE:
            logging.warning(f'Неверная скорость для Runner. ValueError: {VE}')
        else:
            for i in range(10):
                runner_obj_1.walk()
            self.assertEqual(runner_obj_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner_obj_2 = rt_with_exceptions.Runner(123)
        except TypeError as TE:
            logging.warning(f'Неверный тип данных для объекта Runner. TypeError: {TE}')
        else:
            for i in range(10):
                runner_obj_2.run()
            self.assertEqual(runner_obj_2.distance, 100)
            logging.info('"test_run" выполнен успешно')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_obj_3 = rt_with_exceptions.Runner('Katie')
        runner_obj_4 = rt_with_exceptions.Runner('Maggie')
        for i in range(10):
            runner_obj_3.run()
            runner_obj_4.walk()
        self.assertNotEqual(runner_obj_3.distance, runner_obj_4.distance)


if __name__ == '__main__':
    unittest.main()