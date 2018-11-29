import turtle as t

colors = ["#FF0000", "#ffaa00", "#fffa00", "#50ff00", "#0083ff", "#9800ff", "#ff00d8","#FF0000", "#ffaa00", "#fffa00", "#50ff00", "#0083ff", "#9800ff", "#ff00d8","#FF0000", "#ffaa00", "#fffa00", "#50ff00", "#0083ff", "#9800ff", "#ff00d8","#FF0000", "#ffaa00", "#fffa00", "#50ff00", "#0083ff", "#9800ff", "#ff00d8","#FF0000", "#ffaa00", "#fffa00", "#50ff00", "#0083ff", "#9800ff", "#ff00d8","#FF0000", "#ffaa00", "#fffa00", "#50ff00", "#0083ff", "#9800ff", "#ff00d8","#FF0000", "#ffaa00", "#fffa00", "#50ff00", "#0083ff", "#9800ff", "#ff00d8","#FF0000", "#ffaa00", "#fffa00", "#50ff00", "#0083ff", "#9800ff", "#ff00d8","#FF0000", "#ffaa00", "#fffa00", "#50ff00", "#0083ff", "#9800ff", "#ff00d8"]

t.title("Draw Shapes and stuff");
t.setup(425,425,0,0);
t.color("#000000","#000000");

t.width(5)
t.speed(0)


def drawPolygon(sides, length, direction):
    turnAngle = ((180 - ((sides - 2)*180)/sides))*direction
    for i in range(sides):
        t.forward(length);
        t.left(turnAngle);
'''
for i in range(7):
    t.color(colors[i]);
    t.pendown();
    t.begin_fill();
    drawPolygon(10-(i+1), 50, 1);
    t.end_fill();
    t.penup();
    #t.forward(i*10);
i = 0
for i in range(8+1):
    print(i)
    t.color(colors[i]);
    t.pendown();
    t.begin_fill();
    drawPolygon(10-(i+1), 50, -1);
    t.end_fill();
    t.penup();
    #t.forward(i*10);
'''
'''
i =0
while (300-(i*5)>0):
    t.width(30-i)
    t.color(colors[i]);
    drawPolygon(30 - i, 300-(i*5), 1);
    t.right(40)
    i +=1
'''
i=0
while (300-(i*5)>0):
    t.color(colors[i]);
    t.begin_fill();
    drawPolygon(3, 300-(i*5), 1);
    t.end_fill();
    t.right(40)
    i +=1

