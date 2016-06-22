# Chap01/demo_matplotlib.py
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # plot y = x^2 with red dots
    x = np.array([1, 2, 3, 4, 5])
    y = x * x
    plt.plot(x, y, 'ro')
    plt.axis([0, 6, 0, 30])
    plt.savefig('demo_plot.png')
