# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def clust(x, y, x_cc, y_cc, k, points_count):
    cluster = []
    for i in range(0, points_count):
        d = dist(x[i], y[i], x_cc[0], y_cc[0])
        numb = 0
        for j in range(0, k):
            if dist(x[i], y[i], x_cc[j], y_cc[j]) < d:
                d = dist(x[i], y[i], x_cc[j], y_cc[j])
                numb = j
        cluster.append(numb)
    return cluster

def calculate_center_of_mass(cluster, x, y, k):
    center_of_mass_x = [0 for i in range(k)]
    center_of_mass_y = [0 for i in range(k)]
    count = [0 for i in range(k)]

    for i in cluster:
        count[i] += 1

    number = 0
    for i in cluster:
        center_of_mass_x[i] += x[number] / count[i]
        center_of_mass_y[i] += y[number] / count[i]
        number += 1

    return [center_of_mass_x, center_of_mass_y]

def clusterSum(k,x,y,x_cc,y_cc,cluster):
    result = 0
    for i in range(0,k):
        result = 0
        for j in range(0,len(cluster)):
            if(cluster[j] == i):
                result += dist(x[j],y[j],x_cc[i],y_cc[i]) ** 2
    return result

def show_dependence_wcss_on_numbrer_of_clusters(wcss, K):
    plt.plot(range(1, K), wcss)
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()

def main():

    # кол-во точек
    global x_cc, y_cc
    points_count = 200
    # k - кол-во кластеров в данной задаче range и выбираем оптимальный потом
    K = range(0, 10)
    x = np.random.randint(1, 100, points_count)
    y = np.random.randint(1, 100, points_count)

    x_c = np.mean(x)
    y_c = np.mean(y)

    def calculate_R():
        R = 0
        for i in range(0, points_count):
            r = dist(x_c, y_c, x[i], y[i])
            if (r > R):
                R = r
        return R

    R = calculate_R()

    k_values = []

    for k in K:
        x_cc = [R * np.cos(2 * np.pi * i / k) + x_c for i in range(k)]
        y_cc = [R * np.sin(2 * np.pi * i / k) + x_c for i in range(k)]

    print(x_cc)
    print(y_cc)
    cluster = clust(x, y, x_cc, y_cc, k,points_count)
    center_of_mass = calculate_center_of_mass(cluster, x, y, k)

    # Сравниваем текущее расположение точек и новое рассчитанное
    changed = False
    while not changed:
        new_cluster = clust(x, y, center_of_mass[0], center_of_mass[1], k, points_count)
        k_values.append(clusterSum(k,x,y,x_cc,y_cc,cluster))
        if np.array_equal(new_cluster, cluster):
            changed = True
            break
        cluster = new_cluster
        center_of_mass = calculate_center_of_mass(cluster, x, y, k)

    print(k_values)

    plt.plot(K[0:len(k_values)], k_values)
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.show()

    print(len(k_values) - 1)
    k = 3

    changed = False
    while not changed:
        new_cluster = clust(x,y,center_of_mass[0],center_of_mass[1],k,points_count)
        if np.array_equal(new_cluster,cluster):
            changed = True
            break

        cluster = new_cluster
        center_of_mass = calculate_center_of_mass(cluster,x,y,k)

    colors = ['r','b','y']
    print(k)
    print("clusters")
    for i in range(0,points_count):
        plt.scatter(x[i],y[i], c=colors[cluster[i]])
        plt.scatter(center_of_mass[0], center_of_mass[1], marker='*', c='green',s=200)
    plt.show()

if __name__ == '__main__': main()