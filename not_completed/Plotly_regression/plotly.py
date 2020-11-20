import plotly.graph_objects as go
import numpy as np
from sklearn.cluster import KMeans
import math

# Рандомно задаем точки
count_of_dots = 100
# coordinates (3d)
x = np.random.randint(0,100,count_of_dots)
y = np.random.randint(0,100,count_of_dots)
z = np.random.randint(0,100,count_of_dots)

# Должны разделить точки на классы, применим для этого k-means
points = []

for i in range(count_of_dots):
    points.append([x[i],y[i],z[i]])

kmeans = KMeans(n_clusters=2, random_state=0).fit(points)
clusters = kmeans.labels_
colors = ['red']*count_of_dots

for i in range(count_of_dots):
    if clusters[i] == 1:
        colors[i] = 'blue'

# Рисуем их при помощи plotly
fig = go.Figure(data=[
    go.Scatter3d(x=x, y=y, z=z,
                 mode='markers',
                 marker = dict(color=colors))
])

fig.show()

# Минимизируем сумму логарифмов и вытаскиваем параметры плоскости
# тут нарочно неправильно

# нужно: найти параметры A,B,C,D минимизацией того p что написан ниже
# можно использовать любые готовые библиотеки
# например что-то связанное с градиентным спуском

p = 0
for i in range(count_of_dots):
    #p += math.log(1+math.e**(A*x[i]+B*y[i]+C*z[i]+D))
    pass
# Отсроить разделяющую плоскость (картинка) + точки отрисованные выше

# Предсказать новую точку (тоже рандомно на вход)
# x_new = np.random.randint(0, 100)
# y_new = np.random.randint(0, 100)
# z_new = np.random.randint(0, 100)
# fig = go.Figure(data=[go.Scatter3d(x=[x_new], y=[y_new], z=[z_new],
#                                    mode='markers')])
# fig.show()