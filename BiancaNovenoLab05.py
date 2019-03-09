"""
Author: Bianca Noveno
Lab 5: Conditional Statements
Using conditional statements to plot random points in different quadrats.
Due date: March 15, 2019
"""
#import modules
import matplotlib.pyplot as plt
import random

#set up the rectangle
min_long = -109
max_long = -102
min_lat = 37
max_lat = 41

#set up split values
bp_long = -105.5
bp_lat = 39

#5 points for the rectangle: (min_long,min_lat), (max_long,min_lat), (max_long, max_lat), (min_long, max_lat), (min_long, min_lat)
#make 2 lists with the corresponding coordinates for the rectangle
longitude = [min_long, max_long, max_long, min_long, min_long]
latitude = [min_lat, min_lat, max_lat, max_lat, min_lat]

#plot the rectangle
plt.plot(longitude, latitude)
#include axis labels
plt.xlabel('Longitude')
plt.ylabel('Latitude')

for i in range (0,500):
    rand_long = random.uniform(min_long, max_long)
    rand_lat = random.uniform(min_lat, max_lat)
    if rand_long > bp_long: 
        #all the points that satisfy this condition is on the right side
        if rand_lat > bp_lat: #upper right
            symbol = 'y^'
        else: #lower right
            symbol = 'bo'
    else: #left side
        if rand_lat > bp_lat: #upper left
            symbol = 'gs'
        else: #lower left
            symbol = 'r*'
<<<<<<< HEAD
    plt.plot(rand_long, rand_lat, symbol) #plot the random longitude and latitude with corresponding symbol 
plt.show() #shows plot
raw_input ("press any key to show the results") 
=======
    plt.plot(rand_long, rand_lat, symbol)    
plt.show()
raw_input ("press any key to show the results")
>>>>>>> 8c986e86ce6dd97b4e82046846239ec98776a5b9
