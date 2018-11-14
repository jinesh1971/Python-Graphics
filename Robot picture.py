from graphics import *
win = GraphWin("ROBERT",1000,1000)


spike1F = Line(Point(100,250),Point(110,230))
spike1F.draw(win)

spike2F = Line(Point(110,230),Point(120,250))
spike2F.draw(win)

spike3F = Line(Point(120,250),Point(130,230))
spike3F.draw(win)

spike4F = Line(Point(130,230),Point(140,250))
spike4F.draw(win)

spike5F = Line(Point(140,250),Point(150,230))
spike5F.draw(win)

spike6F = Line(Point(150,230),Point(160,250))
spike6F.draw(win)

spike7F = Line(Point(160,250),Point(170,230))
spike7F.draw(win)

spike8F = Line(Point(170,230),Point(180,250))
spike8F.draw(win)

spike1B = Line(Point(500,250),Point(490,230))
spike1B.draw(win)

spike2B = Line(Point(490,230),Point(480,250))
spike2B.draw(win)

spike3B = Line(Point(480,250),Point(470,230))
spike3B.draw(win)

spike4B = Line(Point(470,230),Point(460,250))
spike4B.draw(win)

spike5B = Line(Point(460,250),Point(450,230))
spike5B.draw(win)

spike6B = Line(Point(450,230),Point(440,250))
spike6B.draw(win)

spike7B = Line(Point(440,250),Point(430,230))
spike7B.draw(win)

spike8B = Line(Point(430,230),Point(420,250))
spike8B.draw(win)





head = Rectangle(Point(200,100),Point(400,200))
head.draw(win)

neck = Rectangle(Point(275,200),Point(325,250))
neck.draw(win)

body = Rectangle(Point(100,250),Point(500,500))
body.draw(win)

leg1 = Rectangle(Point(190,500),Point(250,600))
leg1.draw(win)

leg2 = Rectangle(Point(350,500),Point(410,600))
leg2.draw(win)

shoe1 = Rectangle(Point(170,600),Point(270,620))
shoe1.draw(win)

shoe2 = Rectangle(Point(330,600),Point(430,620))
shoe2.draw(win)

eye1 = Circle(Point(250,120),10)
eye1.draw(win)

eye1blackspot = Circle(Point(250,120),3)
eye1blackspot.draw(win)

eye2 = Circle(Point(350,120),10)
eye2.draw(win)

eye2blackspot = Circle(Point(350,120),3)
eye2blackspot.draw(win)

mouth = Rectangle(Point(260,150),Point(340,175))
mouth.draw(win)

mouthline1 = Rectangle(Point(268,150),Point(268,175))
mouthline1.draw(win)

mouthline2 = Rectangle(Point(276,150),Point(276,175))
mouthline2.draw(win)

mouthline3 = Rectangle(Point(284,150),Point(284,175))
mouthline3.draw(win)

mouthline4 = Rectangle(Point(292,150),Point(292,175))
mouthline4.draw(win)

mouthline5 = Rectangle(Point(300,150),Point(300,175))
mouthline5.draw(win)

mouthline6 = Rectangle(Point(308,150),Point(308,175))
mouthline6.draw(win)

mouthline7 = Rectangle(Point(316,150),Point(316,175))
mouthline7.draw(win)

mouthline8 = Rectangle(Point(324,150),Point(324,175))
mouthline8.draw(win)

mouthline9 = Rectangle(Point(332,150),Point(332,175))
mouthline9.draw(win)

leftLegDesign1 = Rectangle(Point(190,510),Point(200,590))
leftLegDesign1.draw(win)

leftLegDesign2 = Rectangle(Point(250,510),Point(240,590))
leftLegDesign2.draw(win)

rightLegDesign1 = Rectangle(Point(350,510),Point(360,590))
rightLegDesign1.draw(win)

rightLegDesign2 = Rectangle(Point(410,510),Point(400,590))
rightLegDesign2.draw(win)


leftLegDesign1.setFill('light blue')
leftLegDesign2.setFill('light blue')
rightLegDesign1.setFill('light blue')
rightLegDesign2.setFill('light blue')

head.setFill('tan')
eye1.setFill('white')
eye2.setFill('white')
eye1blackspot.setFill('black')
eye2blackspot.setFill('black')
mouth.setFill('yellow')
neck.setFill('blue')
body.setFill('purple')
leg1.setFill('green')
leg2.setFill('green')


win.getMouse()
win.close()

