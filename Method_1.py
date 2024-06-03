import time
from machine import Pin
a = Pin(23, Pin.OUT, Pin.PULL_UP)
b = Pin(16, Pin.OUT, Pin.PULL_UP)
c = Pin(13, Pin.OUT, Pin.PULL_UP)
d = Pin(14, Pin.OUT, Pin.PULL_UP)
e = Pin(25, Pin.OUT, Pin.PULL_UP)
f = Pin(21, Pin.OUT, Pin.PULL_UP)
g = Pin(22, Pin.OUT, Pin.PULL_UP)
INC_button = Pin(4, Pin.IN)
DEC_button = Pin(36, Pin.IN)
RESET_button = Pin(39, Pin.IN)
num = {
    0 : [1,1,1,1,1,1,0],
    1 : [0,1,1,0,0,0,0],
    2 : [1,1,0,1,1,0,1],
    3 : [1,1,1,1,0,0,1],
    4 : [0,1,1,0,0,1,1],
    5 : [1,0,1,1,0,1,1],
    6 : [1,0,1,1,1,1,1],
    7 : [1,1,1,0,0,0,0],
    8 : [1,1,1,1,1,1,1],
    9 : [1,1,1,1,0,1,1] }

list = [num.get(0),num.get(1),num.get(2),num.get(3),num.get(4),num.get(5),num.get(6),num.get(7),num.get(8),num.get(9)]
i=0
a.value(list[0][0])
b.value(list[0][1])
c.value(list[0][2])
d.value(list[0][3])
e.value(list[0][4])
f.value(list[0][5])
g.value(list[0][6])

while True:
    
    if INC_button.value() == 1 and i != 9 :
        i = i+1
    a.value(list[i][0])
    b.value(list[i][1])
    c.value(list[i][2])
    d.value(list[i][3])
    e.value(list[i][4])
    f.value(list[i][5])
    g.value(list[i][6])
    time.sleep(0.5)
    if INC_button.value() == 1 and i == 9 :
        i = 9
    a.value(list[i][0])
    b.value(list[i][1])
    c.value(list[i][2])
    d.value(list[i][3])
    e.value(list[i][4])
    f.value(list[i][5])
    g.value(list[i][6])
    time.sleep(0.5)

    if DEC_button.value() == 1 and i != 0 :
        i = i-1
        a.value(list[i][0])
        b.value(list[i][1])
        c.value(list[i][2])
        d.value(list[i][3])
        e.value(list[i][4])
        f.value(list[i][5])
        g.value(list[i][6])
        time.sleep(0.5)
    if DEC_button.value() == 1 and i == 0 :
        i = 0
        a.value(list[i][0])
        b.value(list[i][1])
        c.value(list[i][2])
        d.value(list[i][3])
        e.value(list[i][4])
        f.value(list[i][5])
        g.value(list[i][6])
        time.sleep(0.5)
    if RESET_button.value() == 1 :
        i = 0
        a.value(list[0][0])
        b.value(list[0][1])
        c.value(list[0][2])
        d.value(list[0][3])
        e.value(list[0][4])
        f.value(list[0][5])
        g.value(list[0][6])
        time.sleep(0.5)