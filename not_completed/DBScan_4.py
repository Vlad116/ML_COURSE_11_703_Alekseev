import matplotlib.pyplot as plt
import numpy as np

def dist(x1,y1,x2,y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

n = 500
eps, minPts = 5,3
x = np.random.randint(1,100,n)
y = np.random.randint(1,100,n)
flags = []

for i in range (0,n):
    # кол-во соседей
    neighb = 0
    for j in range(0, n):
        # если расстояние меньше эпсилон, добавляем соседа
        if dist(x[i], y[i],x[j],y[j]) < eps:
            neighb += 1
    # если соседи
    if neighb >= minPts:
        flags.append('g')
    else:
        flags.append('r')

for i in range(0,n):
    if flags[i] != 'g':
        for j in range(0,n):
            if flags[j] == 'g':
                if dist(x[i], y[i], x[j], y[j]) < eps:
                    flags[i] = 'y'
    plt.scatter(x[i],y[i], color=flags[i])
plt.show()
clusters = []
cl = 1

# for i in range (0,n):
#     for j in range(i,n):
