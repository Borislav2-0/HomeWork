team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_2 + score_1
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'победа команды "Мастера кода"!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'победа команды "Волшебники данных"!'
else:
    challenge_result = 'Ничья!'

print("В команде Мастера кода участников: %d!" % 5)

print("Итого сегодня в командах участников: %(team1_num)d и %(team2_num)d!" % {'team1_num': 5, 'team2_num': 6})

print("Команда 'Волшебники данных' решила задач: {}!".format(score_2))

print("'Волшебники данных' решили задачи за {}сек.!".format(team1_time))

print(f'Команды решили {score_1} и {score_2} задач.')

print(f'Результат битвы: {challenge_result}')

print(f'Сегодня было решено {tasks_total} задач, в среднем за {time_avg} секунды на задачу!')