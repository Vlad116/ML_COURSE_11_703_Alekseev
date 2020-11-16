import matplotlib.pyplot as plt
import matplotlib.colors as colorsq
import numpy as np


def distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


n = 200
eps, min_pts = 5, 3
color_list = []

colors = ['lavenderblush', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 'darkmagenta', 'darkorange', 'maroon',
          'pink', 'crimson', 'lime', 'red', 'gray', 'olive', 'dodgerblue', 'skyblue', 'orangered', 'sienna', 'olive']

x = [np.random.randint(1, 100) for i in range(n)]
y = [np.random.randint(1, 100) for i in range(n)]
flags = []

for i in range(0, n):
    neighbours_count = -1
    for j in range(0, n):
        if distance(x[i], y[i], x[j], y[j]) <= eps:
            neighbours_count += 1
    if neighbours_count >= min_pts:
        flags.append('g')
    else:
        flags.append('lavenderblush')
for i in range(0, n):
    if flags[i] == 'lavenderblush':
        for j in range(0, n):
            if flags[j] == 'g':
                if distance(x[i], y[i], x[j], y[j]) <= eps:
                    flags[i] = 'y'
cluster = []
for i in range(n):
    cluster.append(0)
c = 1

for i in range(0, n):
    if flags[i] == 'g':
        for j in range(0, n):
            if distance(x[i], y[i], x[j], y[j]) <= eps:
                if flags[j] == 'g':
                    if cluster[i] == 0 and cluster[j] == 0:
                        cluster[i] = c
                        cluster[j] = c
                        c += 1
                    elif cluster[i] == 0 and cluster[j] != 0:
                        cluster[i] = cluster[j]
                    elif cluster[j] == 0 and cluster[i] != 0:
                        cluster[j] = cluster[i]
                    elif cluster[i] != 0 and cluster[j] != 0:
                        if cluster[i] < cluster[j]:
                            cluster[j] = cluster[i]
                        else:
                            cluster[i] = cluster[j]
                elif flags[j] == 'y':
                    if cluster[i] == 0:
                        cluster[i] = c
                        c += 1

for i in range(0, n):
    if flags[i] == 'y':
        for j in range(0, n):
            if flags[j] == 'g':
                if distance(x[i], y[i], x[j], y[j]) <= eps and cluster[j] != 0:
                    cluster[i] = cluster[j]

for i in range(n):
    color_list.append(colors[cluster[i]])

for i in range(0, n):
    plt.scatter(x[i], y[i], color=flags[i])
plt.show()

for i in range(0, n):
    plt.scatter(x[i], y[i], color=color_list[i])
plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
#
# def dist(x1,y1,x2,y2):
#     return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
#
# n = 500
# eps, minPts = 5,3
# x = np.random.randint(1,100,n)
# y = np.random.randint(1,100,n)
# flags = []
#
# for i in range (0,n):
#     # кол-во соседей
#     neighb = 0
#     for j in range(0, n):
#         # если расстояние меньше эпсилон, добавляем соседа
#         if dist(x[i], y[i],x[j],y[j]) < eps:
#             neighb += 1
#     # если соседи
#     if neighb >= minPts:
#         flags.append('g')
#     else:
#         flags.append('r')
#
# for i in range(0,n):
#     if flags[i] != 'g':
#         for j in range(0,n):
#             if flags[j] == 'g':
#                 if dist(x[i], y[i], x[j], y[j]) < eps:
#                     flags[i] = 'y'
#     plt.scatter(x[i],y[i], color=flags[i])
# plt.show()
# clusters = []
# cl = 1
#
# # for i in range (0,n):
# #     for j in range(i,n):
