import matplotlib.pyplot as plt
import random

x_min = 0
x_max = 10
y_min = 0
y_max = 5

x_coors = [x_min, x_max, x_max, x_min, x_min]
y_coors = [y_min, y_min, y_max, y_min, y_min]

plt.plot(x_coors, y_coors)

plt.xlabel("Long")
plt.ylabel("Lat")

for i in range (0,2):
    p_x = random.uniform(x_min, x_max)
    p_y = random.uniform(y_min, y_max)
    plt.plot(p_x, p_y, 'bx')
plt.show()