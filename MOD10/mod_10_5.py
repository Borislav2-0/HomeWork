import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        my_line = file.readline()
        while my_line:
            all_data.append(my_line)
            my_line = file.readline()


files = [f'./file {number}.txt' for number in range(1, 5)]

start1 = datetime.now()
for file in files:
    read_info(file)
end1 = datetime.now()
res1 = end1 - start1
print(f'Длительность чтения файлов линейно: {res1} сек.')

"""if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start2 = datetime.now()
        pool.map(read_info, files)
    end2 = datetime.now()
    res2 = end2 - start2
    print(f'Длительность многопроцессного чтения файлов: {res2} сек.')"""
