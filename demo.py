import matplotlib.pyplot as plt
import random
# demo 1: make a rectangle
x_min = 0
x_max = 10
y_min = 0
y_max = 5
#set the boundary, there should be 5 points to show that it's a closed figure
#(x_min, y_min) -> (x_max, y_min) -> (x_max, y_max) -> (x_min, y_max) -> (x_min, y_min)
x_coors = [x_min, x_max, x_max, x_min, x_min]
y_coors = [y_min, y_min, y_max, y_min, y_min]
#plot the rectangle
plt.plot(x_coors, y_coors)
#display labels
plt.xlabel("Long")
plt.ylabel("Lat")
#set break point
bp_x = 5
bp_y = 2.5
#demo2: create 2 random points inside the boundary
for i in range(0,2):
    p_x = random.uniform(x_min, x_max)
    p_y = random.uniform(y_min, y_max)
    #demo3: set point label based on its locations
    if p_x < bp_x:
        #left region
        if p_y < bp_y:
            #left_bot
            plt.plot(p_x, p_y, 'bx')
        else:
            #left top
            plt.plot(p_x, p_y, 'b*')
    else: #right part
        if p_y < bp_y:
            #right bot
            plt.plot(p_x, p_y, 'rx')
        else:
            plt.plot(p_x, p_y, 'r*')
            
#display
plt.show()
#stop the code to see the results
raw_input("press any key to see the results")