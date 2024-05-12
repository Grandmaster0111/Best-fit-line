import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
s=10
x = np.random.randint(50, 100, s)
y = np.random.randint(1, 50, s)


def best_fit_line(x, y):
    m = ((mean(x) * mean(y)) - mean(x * y)) / ((mean(x) * mean(x)) - mean(x * x))
    b = mean(y) - m * mean(x)
    return m, b


m, b = best_fit_line(x,y)

regression_line = [(m*i)+b for i in x]

plt.scatter(x,y)
plt.plot(x,regression_line)
plt.show()
