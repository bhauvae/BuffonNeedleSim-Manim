import random
from numpy import pi
from numpy import sin

width = 800
height = 800

number_of_lines = 15
number_of_sticks = 1000000

t = width / (number_of_lines - 1)
nl = t / 7
t_list = []
d_list = []

intersect = 0
total = 0
k = 0
for i in range(number_of_lines):
    t_list.append(-(width / 2) + i * t)
    d_list.append(0)

for j in range(number_of_sticks):
    x = random.uniform(-width / 2, width / 2)
    y = random.uniform(-height / 2, height / 2)
    angle = random.uniform(-pi / 2, pi / 2)
    total += 1

    for a in range(len(t_list)):
        d_list[a] = t_list[a]

    for a in range(len(t_list)):
        d_list[a] = abs(d_list[a] - x)

    distance = min(d_list)

    if distance < (nl * sin(abs(angle)) / 2):
        intersect += 1


    def predict(inte, tota):
        prob = inte / tota
        if inte > 0:
            pie = (2 * nl / (prob * t))
        else:
            pie = 0
        return pie


    print(predict(intersect, total))
    if round(predict(intersect, total), 5) == 3.1415:
        print(total)
        break
