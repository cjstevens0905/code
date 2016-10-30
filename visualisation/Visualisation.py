from graphics import *
#opens up the text file 
text_file = open("data.txt")
#reads the data text file 
dataRead = text_file.read()
#splits up the data file and transfers it into a list
dataList = dataRead.split("\n")
#closes the file
text_file.close()


# Creates a window, 'ModuleData', to the size allocated 
window = GraphWin("ModuleData", 880, 400)
window.setBackground(color_rgb(0,0,0))

# Create and draw a circle
#number1--------------------------------green
ball1 = Circle(Point(20,350), 9)
ball1.setFill(color_rgb(43,228,61))
ball1.draw(window)
#number2
ball2 = Circle(Point(50,350), 9)
ball2.setFill(color_rgb(21,233,42))
ball2.draw(window)
#number3
ball3 = Circle(Point(80,350), 9)
ball3.setFill(color_rgb(38,236,58))
ball3.draw(window)
#number4
ball4 = Circle(Point(110,350), 9)
ball4.setFill(color_rgb(73,236,90))
ball4.draw(window)
#number5
ball5 = Circle(Point(140,350), 9)
ball5.setFill(color_rgb(92,233,106))
ball5.draw(window)
#number6
ball6 = Circle(Point(170,350), 9)
ball6.setFill(color_rgb(75,185,86))
ball6.draw(window)
#number7
ball7 = Circle(Point(200,350), 9)
ball7.setFill(color_rgb(111,175,117))
ball7.draw(window)
#number8
ball8 = Circle(Point(230,350), 9)
ball8.setFill(color_rgb(152,185,155))
ball8.draw(window)
#number9--------------------------------orange
ball9 = Circle(Point(260,350), 9)
ball9.setFill(color_rgb(185,177,152))
ball9.draw(window)
#number10
ball10 = Circle(Point(290,350), 9)
ball10.setFill(color_rgb(196,177,116))
ball10.draw(window)
#number11
ball11 = Circle(Point(320,350), 9)
ball11.setFill(color_rgb(198,170,78))
ball11.draw(window)
#number12
ball12 = Circle(Point(350,350), 9)
ball12.setFill(color_rgb(216,176,43))
ball12.draw(window)
#number13
ball13 = Circle(Point(380,350), 9)
ball13.setFill(color_rgb(226,178,21))
ball13.draw(window)
#number14
ball14 = Circle(Point(410,350), 9)
ball14.setFill(color_rgb(239,185,9))
ball14.draw(window)
#number15
ball15 = Circle(Point(440,350), 9)
ball15.setFill(color_rgb(255,196,0))
ball15.draw(window)
#number16
ball16 = Circle(Point(470,350), 9)
ball16.setFill(color_rgb(255,219,95))
ball16.draw(window)
#number17
ball17 = Circle(Point(500,350), 9)
ball17.setFill(color_rgb(255,228,135))
ball17.draw(window)
#number18
ball18 = Circle(Point(530,350), 9)
ball18.setFill(color_rgb(255,208,135))
ball18.draw(window)
#number19--------------------------------red
ball19 = Circle(Point(560,350), 9)
ball19.setFill(color_rgb(255,171,135))
ball19.draw(window)
#number20
ball20 = Circle(Point(590,350), 9)
ball20.setFill(color_rgb(240,138,93))
ball20.draw(window)
#number21
ball21 = Circle(Point(620,350), 9)
ball21.setFill(color_rgb(230,115,65))
ball21.draw(window)
#number22
ball22 = Circle(Point(650,350), 9)
ball22.setFill(color_rgb(222,92,37))
ball22.draw(window)
#number23
ball23 = Circle(Point(680,350), 9)
ball23.setFill(color_rgb(210,80,25))
ball23.draw(window)
#number24
ball24 = Circle(Point(710,350), 9)
ball24.setFill(color_rgb(210,56,25))
ball24.draw(window)
#number25
ball25 = Circle(Point(740,350), 9)
ball25.setFill(color_rgb(220,46,11))
ball25.draw(window)
#number26
ball26 = Circle(Point(770,350), 9)
ball26.setFill(color_rgb(233,41,3))
ball26.draw(window)
#number27
ball27 = Circle(Point(800,350), 9)
ball27.setFill(color_rgb(246,43,3))
ball27.draw(window)
#number28
ball28 = Circle(Point(830,350), 9)
ball28.setFill(color_rgb(255,62,23))
ball28.draw(window)
#number29
ball29 = Circle(Point(860,350), 9)
ball29.setFill(color_rgb(255,43,0))
ball29.draw(window)

# Text Title
text = Text(Point(425,40),"ModuleDATa")
text.setSize(30)
#text.setStyle('italic')
text.setTextColor(color_rgb(255,255,255))
text.draw(window)

# Text underneath the coloured circles 
text = Text(Point(426,380), "Click for Scores")
text.setSize(20)
text.setTextColor(color_rgb(255,255,255))
text.setStyle('bold')
text.draw(window)

# Text - marks ---> left and right = first number --- up and down = second number.
#----------------------------------------green
mark = Text(Point(30,100), "80")
mark.setSize(36)
mark.setTextColor(color_rgb(0,228,23))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(90,160), "79")
mark.setSize(36)
mark.setTextColor(color_rgb(0,228,23))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(60,220), "76")
mark.setSize(36)
mark.setTextColor(color_rgb(0,228,23))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(140,290), "74")
mark.setSize(36)
mark.setTextColor(color_rgb(0,228,23))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(180,90), "72")
mark.setSize(36)
mark.setTextColor(color_rgb(0,228,23))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(200,155), "62")
mark.setSize(36)
mark.setTextColor(color_rgb(0,228,23))
mark.setStyle("italic")
mark.draw(window)
#----------------------------------------orange
mark = Text(Point(230,260), "59")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(250,90), "59")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(270,170), "59")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(300,270), "59")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(330,190), "59")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(350,90), "57")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(370,260), "57")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(400,90), "57")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(430,140), "55")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(460,270), "54")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(480,80), "54")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(500,200), "52")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
#mark.draw(window)

mark = Text(Point(530,280), "52")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(570,200), "52")
mark.setSize(36)
mark.setTextColor(color_rgb(255,196,0))
mark.setStyle("italic")
mark.draw(window)
#-----------------------------------------red
mark = Text(Point(630,90), "49")
mark.setSize(36)
mark.setTextColor("red")
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(640,290), "49")
mark.setSize(36)
mark.setTextColor("red")
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(670,250), "48")
mark.setSize(36)
mark.setTextColor("red")
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(710,270), "47")
mark.setSize(36)
mark.setTextColor("red")
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(700,160), "44")
mark.setSize(36)
mark.setTextColor("red")
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(770,130), "44")
mark.setSize(36)
mark.setTextColor("red")
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(800,200), "44")
mark.setSize(36)
mark.setTextColor("red")
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(830,260), "43")
mark.setSize(36)
mark.setTextColor("red")
mark.setStyle("italic")
mark.draw(window)

mark = Text(Point(840,150), "42")
mark.setSize(36)
mark.setTextColor("red")
mark.setStyle("italic")
mark.draw(window)



# Wait until the mouse is clicked before closing the window
window.getMouse()