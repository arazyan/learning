position = ['junior', 'middle', 'senior']
pos_idx = 0

if worker[2] < 2:
    pos_idx = 0
elif 2 <= worker[2] <= 5:
    pos_idx = 1
else:
    pos_idx = 2
    
status = '{} {} is {}'.format(worker[0], worker[1], position[pos_idx])

