from turtle import Turtle

starting_position  = [(0,0),(-20,0),(-40,0)]

move_distance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake :

    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in starting_position:
            self.add_segment(i)

    def add_segment(self,i):
        segment = Turtle("square")

        segment.color("white")
        segment.penup()
        segment.goto(i)
        self.segments.append(segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extent(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)