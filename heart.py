import math

2

3

3

from turtle import*

def hearta(k):

return 15 math.sin(k)**3

def heartb(k):

return 12 math.cos(k)-5*\

math.cos(2*k)-2*\

math.cos(3*k)-\

10

11

math.cos(4*k)

speed (0)

12bgcolor("black")

13

14

for i in range(6000):

goto(hearta(i)*20, heartb(i)*20)

15

for j in range(5):

16

color("red")

17

goto (0,0)

18

done()