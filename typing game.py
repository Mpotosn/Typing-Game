from tkinter import*
import random

sentences = ["The dog ran fast down the street","She opened the door and walked inside","He finished his homework before dinner","The sun rose over the horizon","The children played outside all afternoon","I found my keys in the kitchen","The cat jumped onto the couch","We visited the museum last weekend","The tree was tall and strong","He ate a sandwich for lunch","The car stopped at the red light","She painted a picture of the ocean","I heard a knock at the door","They traveled to the mountains for vacation","The book was thick and heavy"]
screen = Tk()
screen.title("Typing Game")
screen.config(bg="#C5D1F6")

time = 120
points = 0


def startGame(event):
    lbl2.configure(text="Press Enter to start")
    screen.bind('<Return>',nextSentence)
    if time == 120:
        countdown()


def countdown():
    global time
    if time > 0:
        time -= 1
        timer.configure(text="Time:"+str(time))
        timer.after(1000,countdown)

def nextSentence(event):
    global points
    lbl2.configure(text="")
    if time >0:
        if e.get() == sentences[1]:
            points +=1
            print(points)
            score.configure(text="Score:"+str(points))
        e.delete(0,END)
        random.shuffle(sentences)
        print(sentences)
        lbl.configure(text=sentences[1])

lbl1 = Label(screen, text="Type The Sentence Shown As Fast As U Can  !!!",bg="#C5D1F6")
lbl2 = Label(screen, text="Press 1 To Start",bg="#C5D1F6")
lbl3 = Label(screen, text="U Have Exactly 120 Seconds To Sumbit Ur Answers",bg="#C5D1F6")
lbl4 = Label(screen, text="U Get +1 Point For Every Sentence U Get Right !!",bg="#C5D1F6")
score = Label(screen, text="Score:",bg="#C5D1F6")
timer = Label(screen, text="Time:",bg="#C5D1F6")
lbl = Label(screen, text="Loading....",fg="blue",bg="#B1C2F3")
e = Entry(screen,bg="#D8E1F9")


lbl1.pack()
score.pack()
timer.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()
lbl.pack()

e.pack()
#e.focus_set()   #vasei amesos ton kersora sto entry / m gliton clickei ena
screen.bind('1', startGame)



screen.mainloop()