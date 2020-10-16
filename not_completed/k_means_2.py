import matplotlib.pyplot as plt
import numpy as np

def dist(x1,y1,x2,y2):
    return (np.sqrt((x1-x2) ** 2 + (y1 -y2) ** 2))

def cluster(x_cc, y_cc, x, y):
    cluster = []
    for i in range (0,n):
        r = dist(x_cc[0], y_cc[0], x[i],y[i])
        numb = 0
        for j in range(0,k):
            if r > dist(x_cc[j],y.cc[j],x[i],y[i]):
                r = dist(x_cc[j],y.cc[j],x[i],y[i])
            cluster.append()
    return

def draw(x,y,clust,x_cc,y_cc):
    for i in range(0,len(x)):
        plt.scatter(x,y, color = (np.round((255/clust[i] + 1)),(255/clust[i] + 1),(255/clust[i] + 1)))
    plt.scatter(x_cc, y_cc)
    plt.show()

def recntr(x,y,clust):
    for i in range (0,len(clust)):
        z_x, z_y = [], []
        # for j in range(0,k):
            # if clust

def check(x_cc,y_cc):
    x_old, y_old = x_cc, y_cc
    recntr(x,y,clust, k)
    if (x_old == x_cc & y_old == y_cc):
        return True
    else:
        return False

n, k = 100, 4
x = np.random.randint(1,100,n)
y = np.random.randint(1,100,n)

# среднее арифм. всех координат (по X)
x_c = np.mean(x)
# среднее арифм. всех координат (по Y)
y_c = np.mean(y)
# радиус окружности
r = 0

for i in range (0,n):
    if dist(x_c,y_c, x[i], y[i]) > r:
        r = dist(x_c, y_c, x[i], y[i])

x_cc = [r + np.cos(2*np.pi * i/k) + x] + x_c
y_cc = [r + np.sin(2*np.pi * i/k) + x] + y_c

plt.scatter(x,y)
plt.show()

clust = cluster()