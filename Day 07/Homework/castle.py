from turtle import*

speed(100000)
bgcolor("skyblue")
width(5)

# Ground
penup()
goto(-1000, -400)
pendown()
color("green")
begin_fill()
forward(2000)
right(90)
forward(600)
right(90)
forward(2000)
right(90)
forward(600)
end_fill()


# Left castle
penup()
goto(-900, -400)
pendown()
color("black", "gold")
begin_fill()
forward(200)
right(90)
forward(30)
right(90)
forward(10)
left(90)
forward(30)
left(90)
forward(10)
right(90)
forward(30)
right(90)
forward(10)
left(90)
forward(30)
left(90)
forward(10)
right(90)
forward(30)
right(90)
forward(200)
right(90)
forward(150)
right(90)
end_fill()


# right castle
penup()
goto(750, -400)
pendown()
color("black", "gold")
begin_fill()
forward(200)
right(90)
forward(30)
right(90)
forward(10)
left(90)
forward(30)
left(90)
forward(10)
right(90)
forward(30)
right(90)
forward(10)
left(90)
forward(30)
left(90)
forward(10)
right(90)
forward(30)
right(90)
forward(200)
right(90)
forward(150)
end_fill()



# Left dome
penup()
goto(-750, -400)
pendown()
color("black", "gold")
begin_fill()
right(90)
forward(300)
right(90)
forward(170)
right(90)
forward(300)
right(90)
forward(170)
end_fill()
# Roof
penup()
goto(-750, -100)
pendown()
color("black", "hotpink")
begin_fill()
right(120)
forward(170)
left(30)
forward(50)
right(180)
forward(50)
left(30)
forward(170)
right(120)
forward(170)
end_fill()
# Flag
penup()
goto(-665, 100)
pendown()
color("black", "red")
begin_fill()
right(190)
forward(100)
right(160)
forward(100)
right(10)
end_fill()

# Right dome
penup()
goto(580, -400)
pendown()
color("black", "gold")
begin_fill()
right(90)
forward(300)
right(90)
forward(170)
right(90)
forward(300)
right(90)
forward(170)
end_fill()
# Roof
penup()
goto(580, -100)
pendown()
color("black", "hotpink")
begin_fill()
right(120)
forward(170)
left(30)
forward(50)
right(180)
forward(50)
left(30)
forward(170)
right(120)
forward(170)
end_fill()
# Flag
penup()
goto(665, 100)
pendown()
color("black", "red")
begin_fill()
right(190)
forward(100)
right(160)
forward(100)
right(100)
end_fill()


#Main castle
penup()
goto(-580, -400)
pendown()
color("black", "gold")
begin_fill()
forward(375)
right(90)
forward(68.52)
right(90)
forward(30)
left(90)
forward(68.25)
left(90)
forward(30)
right(90)
forward(68.52)
right(90)
forward(30)
left(90)
forward(68.25)
left(90)
forward(30)
right(90)
forward(68.52)
right(90)
forward(30)
left(90)
forward(68.25)
left(90)
forward(30)
right(90)
forward(68.52)
right(90)
forward(30)
left(90)
forward(68.25)
left(90)
forward(30)
right(90)
forward(68.52)
right(90)
forward(30)
left(90)
forward(68.25)
left(90)
forward(30)
right(90)
forward(68.52)
right(90)
forward(30)
left(90)
forward(68.25)
left(90)
forward(30)
right(90)
forward(68.52)
right(90)
forward(30)
left(90)
forward(68.25)
left(90)
forward(30)
right(90)
forward(68.52)
right(90)
forward(30)
left(90)
forward(68.25)
left(90)
forward(30)
right(90)
forward(68.25)
right(90)
forward(375)
right(90)
forward(1165)
end_fill()

# Second dome
penup()
goto(-340, -55)
pendown()
color("black", "gold")
begin_fill()
right(90)
forward(250)
right(90)
forward(205)
right(90)
forward(220)
right(90)
forward(34.2)
left(90)
forward(30)
right(90)
forward(68.25)
right(90)
forward(30)
left(90)
forward(68.52)
left(90)
forward(30)
end_fill()
# Roof
penup()
goto(-340, 195)
pendown()
color("black", "hotpink")
begin_fill()
right(210)
forward(200)
left(30)
forward(50)
right(180)
forward(50)
left(30)
forward(200)
right(120)
forward(200)
end_fill()
# Flag
penup()
goto(-240, 420)
pendown()
color("black", "red")
begin_fill()
right(190)
forward(100)
right(160)
forward(100)
right(100)
end_fill()

# Forth dome
penup()
goto(140, -25)
pendown()
color("black", "gold")
begin_fill()
forward(220)
right(90)
forward(205)
right(90)
forward(250)
right(90)
forward(37)
right(90)
forward(30)
left(90)
forward(68.52)
left(90)
forward(30)
right(90)
forward(68.25)
right(90)
forward(30)
left(90)
forward(33)
end_fill()
# Roof
penup()
goto(140, 195)
pendown()
color("black", "hotpink")
begin_fill()
right(120)
forward(200)
left(30)
forward(50)
right(180)
forward(50)
left(30)
forward(200)
right(120)
forward(200)
end_fill()
# Flag
penup()
goto(240, 420)
pendown()
color("black", "red")
begin_fill()
right(190)
forward(100)
right(160)
forward(100)
right(100)
end_fill()


# Third dome
penup()
goto(-135, -25)
pendown()
color("black", "gold")
begin_fill()
forward(280)
right(90)
forward(275)
right(90)
forward(280)
right(90)
forward(34.2)
left(90)
forward(30)
right(90)
forward(68.25)
right(90)
forward(30)
left(90)
forward(68.52)
left(90)
forward(30)
right(90)
forward(68.25)
right(90)
forward(30)
left(90)
forward(34.2)
end_fill()

# Roof
penup()
goto(-135, 255)
pendown()
color("black", "hotpink")
begin_fill()
right(130)
forward(210)
left(40)
forward(50)
left(180)
forward(50)
left(40)
forward(210)
right(130)
forward(270)
end_fill()

# Flag
penup()
goto(0, 465)
pendown()
color("black", "red")
begin_fill()
right(190)
forward(100)
right(160)
forward(100)
right(100)
end_fill()


# Main door
penup()
goto(-180, -400)
pendown()
color("black", "brown")
begin_fill()
forward(190)
right(30)
forward(110)
right(60)
forward(260)
right(60)
forward(110)
right(30)
forward(190)
right(90)
forward(360)
end_fill()




#Widnow(left dome)

penup()
goto(-700, -220)
pendown()
color("black", "dodgerblue")
begin_fill()
right(90)
forward(80)
right(90)
forward(70)
right(90)
forward(80)
right(90)
forward(70)
end_fill()

penup()
goto(-700, -220)
pendown()
color("black", "brown")
begin_fill()
right(90)
forward(10)
right(90)
forward(70)
right(90)
forward(10)
right(90)
forward(70)
end_fill()


#Widnow(right dome)

penup()
goto(630, -220)
pendown()
color("black", "dodgerblue")
begin_fill()
right(90)
forward(80)
right(90)
forward(70)
right(90)
forward(80)
right(90)
forward(70)
end_fill()

penup()
goto(630, -220)
pendown()
color("black", "brown")
begin_fill()
right(90)
forward(10)
right(90)
forward(70)
right(90)
forward(10)
right(90)
forward(70)
end_fill()


# Window(second dome)
penup()
goto(-275, 80)
pendown()
color("black", "dodgerblue")
begin_fill()
right(90)
forward(80)
right(90)
forward(70)
right(90)
forward(80)
right(90)
forward(70)
end_fill()

penup()
goto(-275, 80)
pendown()
color("black", "brown")
begin_fill()
right(90)
forward(10)
right(90)
forward(70)
right(90)
forward(10)
right(90)
forward(70)
end_fill()

# Window(forth dome)
penup()
goto(205, 80)
pendown()
color("black", "dodgerblue")
begin_fill()
right(90)
forward(80)
right(90)
forward(70)
right(90)
forward(80)
right(90)
forward(70)
end_fill()

penup()
goto(205, 80)
pendown()
color("black", "brown")
begin_fill()
right(90)
forward(10)
right(90)
forward(70)
right(90)
forward(10)
right(90)
forward(70)
end_fill()

# Window(third dome)
penup()
goto(-35, 125)
pendown()
color("black", "dodgerblue")
begin_fill()
right(90)
forward(95)
right(90)
forward(75)
right(90)
forward(95)
right(90)
forward(75)
end_fill()

penup()
goto(-35, 125)
pendown()
color("black", "brown")
begin_fill()
right(90)
forward(10)
right(90)
forward(75)
right(90)
forward(10)
right(90)
forward(75)
end_fill()




exitonclick()