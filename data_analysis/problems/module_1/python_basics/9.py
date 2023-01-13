def determine_position(worker):
    """Определитель грейда работника

    Функция определяет позицию работника на основе его стажа работы
    """
    position = ['junior', 'middle', 'senior']

    if worker[3] < 2:
        return position[0]
    elif 2 <= worker[3] <= 5:
        return position[1]
    else:
        return position[2]


for i in range(len(workers)):
    print('{} {} is {}'.format(workers[i][0], workers[i][1], determine_position(workers[i])))

