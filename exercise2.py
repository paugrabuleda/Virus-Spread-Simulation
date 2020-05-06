import matplotlib.pyplot as plt
import random as rad
import pygame
import math

class Point:
    def __init__(self, radius):
        self.x = rad.uniform(x_min, x_max)
        self.y = rad.uniform(y_min, y_max)
        self.rad = radius
        self.status = "Cured"

n = 1000
coordinates = []

points = []

x_min, x_max = -10, 10
y_min, y_max = -10, 10

for _ in range(0,n):
    x_cord = rad.uniform(x_min,x_max)
    y_cord = rad.uniform(y_min,y_max)
    cord = [x_cord,y_cord]
    coordinates.append(cord)

    p = Point(5)
    points.append(p)

points[0].status = "Infected"

height = 800
width = 800

white = (255, 255, 255)
red = (255, 0 , 0)
blue = (0 ,0 ,255)

screen = pygame.display.set_mode((width, height))

def cartesian_to_screen(coor):
    x_screen = int((coor[0])/10 * width/2 + width/2)
    y_screen = int((coor[1]) / 10 * width / 2 + width / 2)
    return [x_screen,y_screen]

def get_distance(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

t_history = []
i_history = []
t = 0
d_history = []

for _ in range(10):
    dead = 0
    infected = 0
    t += 1
    for p in range(n):
        if points[p].status == "Infected":
            death = 0.01
            infected = 0.96
            cured = 0.03
            r = rad.uniform(0,1)
            if 0 <= r < death:
                points[p].status = "Death"
            if death <= r < infected + death:
                points[p].status = "Infected"
            if infected + death <= r < 1:
                points[p].status = "Cured"
    for c in range(n):
        if points[c].status == "Infected":
            infected += 1
        if points[c].status == "Death":
            dead += 1
    t_history.append(t)
    i_history.append(infected)
    d_history.append(dead)
    pygame.event.get()
    screen.fill((0, 0, 0))
    for i in range(n):
        displacement_x = rad.uniform(-0.5, 0.5)
        displacement_y = rad.uniform(-0.5,0.5)
        incr_rad = rad.randint(-1,1)
        points[i].x += displacement_x
        points[i].y += displacement_y
        points[i].x = max(-9, points[i].x)
        points[i].x = min(9, points[i].x)
        points[i].y = max(-9, points[i].y)
        points[i].y = min(9, points[i].y)
        for j in range(n):
            if j != i:
                d = get_distance(points[i].x,points[j].x,points[i].y,points[j].y)
                if d<0.5 and points[j].status == "Infected":
                    if points[i].status != "Death":
                        points[i].status = "Infected"
        if points[i].status == "Infected":
            pygame.draw.circle(screen,red, cartesian_to_screen([points[i].x, points[i].y]), points[i].rad)
        if points[i].status == "Cured":
            pygame.draw.circle(screen, white, cartesian_to_screen([points[i].x, points[i].y]), points[i].rad)
        if points[i].status == "Death":
            pygame.draw.circle(screen, blue, cartesian_to_screen([points[i].x, points[i].y]), points[i].rad)
    pygame.display.flip()

plt.plot(t_history,i_history)
plt.plot(t_history,d_history)
plt.show()
