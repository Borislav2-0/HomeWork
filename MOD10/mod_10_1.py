from time import sleep
from datetime import datetime
from threading import Thread

start_time = datetime.now()


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}" + '\n')
            sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')


first_func = write_words(10, 'example1.txt')
second_func = write_words(30, 'example2.txt')
third_func = write_words(200, 'example3.txt')
fourth_func = write_words(100, 'example4.txt')

print(first_func, second_func, third_func, fourth_func)

end_time_func = datetime.now()
time_res_func = end_time_func - start_time
print(f'Работа функций: {time_res_func}')

first = Thread(target=write_words, args=(10, 'example5.txt'))
second = Thread(target=write_words, args=(30, 'example6.txt'))
third = Thread(target=write_words, args=(200, 'example7.txt'))
fourth = Thread(target=write_words, args=(100, 'example8.txt'))

first.start()
second.start()
third.start()
fourth.start()

first.join()
second.join()
third.join()
fourth.join()

end_time = datetime.now()
time_res = end_time - start_time
print(f'Работа потоков: {time_res}')
