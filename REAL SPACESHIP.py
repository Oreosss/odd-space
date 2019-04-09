from graphics import *
import time
from multiprocessing import Process
from random import randrange

def space(C1, C2, C3, C4 , C5, C6, C7, C8, C9, C10):


    win = GraphWin("Space Ship", 1000,800)
    win.setBackground("Black")

    

    star1 = Polygon(Point(50,50), Point(40,70),Point(65,55),Point(35,55),Point(60,70))
    star1.setOutline(C1)
    star1.setFill(C4)
    star1.draw(win)

    star2 = star1.clone()
    star2.move(100,300)
    star2.setOutline(C7)
    star2.setFill(C3)
    star2.draw(win)

    star3 = star1.clone()
    star3.move(190,150)
    star3.setOutline(C2)
    star3.setFill(C5)
    star3.draw(win)

    star4 = star1.clone()
    star4.move(250,10)
    star4.setOutline(C1)
    star4.setFill(C10)
    star4.draw(win)

    star5 = star1.clone()
    star5.move(400,400)
    star4.setOutline(C2)
    star4.setFill(C8)
    star5.draw(win)

    star6 = star1.clone()
    star6.move(230,350)
    star6.setOutline(C1)
    star6.setFill(C7)
    star6.draw(win)

    star7 = star1.clone()
    star7.move(30,420)
    star7.setOutline(C3)
    star7.setFill(C6)
    star7.draw(win)

    star8 = star1.clone()
    star8.move(400,35)
    star8.setOutline(C5)
    star8.setFill(C7)
    star8.draw(win)

    star9 = star1.clone()
    star9.move(0,190)
    star9.setOutline(C1)
    star9.setFill(C8)
    star9.draw(win)

    star10 = star1.clone()
    star10.move(400,170)
    star10.setOutline(C7)
    star10.setFill(C4)
    star10.draw(win)

    star11 = star1.clone()
    star11.move(100,80)
    star11.setOutline(C3)
    star11.setFill(C6)
    star11.draw(win)
    
    star12 = star1.clone()
    star12.move(325,250)
    star12.setOutline(C10)
    star12.setFill(C7)
    star12.draw(win)

    star13 = star1.clone()
    star13.move(125,-15)
    star13.setOutline(C9)
    star13.setFill(C1)
    star13.draw(win)

    star14 = star1.clone()
    star14.move(315,100)
    star14.setOutline(C1)
    star14.setFill(C5)
    star14.draw(win)

   

    stars = [star1, star2, star3, star4, star5, star6 , star7, star8, star9,star10 , star11, star12, star13, star14]

    spaceship(C1,C3,C5,C7,win)
       
    
    for a in range (1000000000000):
        counter = 0
        for i in stars:
            counter = counter+1
            starList= i.getPoints()
            i.move(-10,0)
            time.sleep(0.005)

            if (starList[4].getX() < 0):
                i.move(win.getWidth(),0)
            if counter%2 == 0:
                laser(C5,C10,win)
                   
    


def spaceship(C1,C3,C5,C7,win ):

#SPACESHIP
    body = Oval(Point(200,200),Point(350,250))
    body.setFill(C1)
    body.draw(win)

    front = Polygon(Point(325,206), Point(325,244), Point(380,225))
    front.setFill(C3)
    front.draw(win)

    decor = Oval(Point(248,215), Point(300,235))
    decor.setOutline(C5)
    decor.setWidth("5")
    decor.draw(win)

    decor1 = Polygon(Point(248,201), Point(300,201))
    decor1.setOutline(C7)
    decor1.setWidth("5")
    decor1.draw(win)

    fire1 = Polygon(Point(220,208), Point(185,180), Point(185,270), Point(220,242))
    fire1.setFill("Orange")
    fire1.setOutline("Red")
    fire1.draw(win)
            

    

def laser(C5,C10,win):
    Laser = Rectangle(Point(380,220), Point(450,230))
    Laser.setOutline(C5)
    Laser.setFill(C10)
    Laser.draw(win)
    Laser.move(10,0)
    Laser.undraw()
    Laser.move(20,0)
   
        
        
def main():    


    C1 = color_rgb(randrange(0,255), randrange(0,255), randrange(0,255))
    C2 = color_rgb(randrange(0,255), randrange(0,255), randrange(0,255))
    C3 = color_rgb(randrange(0,255), randrange(0,255), randrange(0,255))
    C4 = color_rgb(randrange(0,255), randrange(0,255), randrange(0,255))
    C5 = color_rgb(randrange(0,255), randrange(0,255), randrange(0,255))
    C6 = color_rgb(randrange(0,255), randrange(0,255), randrange(0,255))
    C7 = color_rgb(randrange(0,255), randrange(0,255), randrange(0,255))
    C8 = color_rgb(randrange(0,255), randrange(0,255), randrange(0,255))
    C9 = color_rgb(randrange(0,255), randrange(0,255), randrange(0,255))
    C10 = color_rgb(randrange(0,255), randrange(0,255), randrange(0,255))

    colors = [C1,C2,C3,C4,C5,C6,C7,C8,C9,C10]

    space_process = Process(target = space,args = (C1,C2,C3,C4,C5,C6,C7,C8,C9,C10))
    space_process.daemon = True
    space_process.start()

    space_process1 = Process(target = space,args = (C1,C2,C3,C4,C5,C6,C7,C8,C9,C10))
    space_process1.daemon = True
    space_process1.start()

    space_process2 = Process(target = space,args = (C1,C2,C3,C4,C5,C6,C7,C8,C9,C10))
    space_process2.daemon = True
    space_process2.start()

    space_process3 = Process(target = space,args = (C1,C2,C3,C4,C5,C6,C7,C8,C9,C10))
    space_process3.daemon = True
    space_process3.start()

    end= input("Done")

if __name__ =='__main__':
    main()
        
    
    
    
