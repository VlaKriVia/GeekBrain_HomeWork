import time
import itertools
import turtle

class TrafficLight:

    global t
    global rectangle_length
    global rectangle_wigth
    global circle_distance
    global circle_radius
    global line_wigth

    def __init__(self, color):

        t.hideturtle()
        t.pen(fillcolor= "grey", pensize=line_wigth, speed=1000)
        t.pu()
        t.lt(90)
        t.fd(rectangle_length/2)
        t.pd()
        t.begin_fill()
        t.rt(90)
        t.fd(rectangle_wigth/2)
        t.rt(90)
        t.fd(rectangle_length)
        t.rt(90)
        t.fd(rectangle_wigth)
        t.rt(90)
        t.fd(rectangle_length)
        t.rt(90)
        t.fd(rectangle_wigth/2)
        t.end_fill()

        t.pu()
        t.rt(90)
        t.fd(circle_distance/2)
        t.dot(circle_radius*2)
        t.fd(circle_distance)
        t.dot(circle_radius * 2)
        t.fd(circle_distance)
        t.dot(circle_radius * 2)
        t.lt(90)

        t.home()

        self.__color = color


    def running(self):

        def paint_circle(move, color):

            if color == "off":
                t.pen(pencolor="black")
                t.dot(circle_radius * 2)
            else:
                t.pen(speed=1000)
                t.goto(0, move)
                t.pen(pencolor=color)
                t.dot(circle_radius*2)
                time.sleep(0.5)

        for i in itertools.cycle(self._TrafficLight__color):

            move_dict = {"r": circle_distance, "y": 0, "g": -circle_distance, "b": -circle_distance, "o": 0}
            color_dict = {"r": "red", "y": "yellow", "g": "green", "b": "black", "o": "off"}
            paint_circle(move_dict.get(i), color_dict.get(i))


rectangle_length = 150
rectangle_wigth = 50
circle_distance = 50
circle_radius = 20
line_wigth = 5
order = "rrrrrrrrrrrrrroyyyyoggggbgbgbgo"

t = turtle.Turtle()
TrafficLight(order).running()