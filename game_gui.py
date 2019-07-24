# name: Paige Sanford
# date: 2019-07-19
# description: Text-based medieval adventure game

from tkinter import *

import random
import time

def clicked():
 
    if selected.get() == 1:
        lbl = Label(window, text="                                          ")
        lbl.grid(column=0, row=9)
        lbl = Label(window, text="Verily, Thou hast chosen.")
        lbl.grid(column=0, row=10)
        lbl = Label(window, text="Thou art wise, but brave be thou not!")
        lbl.grid(column=0, row=11)
    else:
        lbl = Label(window, text="                                          ")
        lbl.grid(column=0, row=9)
        lbl = Label(window, text="Verily, Thou hast chosen.")
        lbl.grid(column=0, row=10)
        lbl = Label(window, text="A storm is coming, but the Castle is in sight, so ye travel on.")
        lbl.grid(column=0, row=11)
        lbl = Label(window, text="A great ogre cometh out of the woods chasing thee hastily.")
        chosenOption = "2"
        correctOption = random.randint(1, 2)

        if chosenOption == str(correctOption):
            lbl = Label(window, text="Ye draw yon bow, and shootest the ogre dead with yay one shot.")
            lbl.grid(column=0, row=13)
            lbl = Label(window, text="Thou art applauded by the group for thine great shot, and are thus appointed leader.")
            lbl.grid(column=0, row=14)
            lbl = Label(window, text="Ye have chosen wisely!")
            lbl.grid(column=0, row=15)
            lbl = Label(window, text="Hoo-Ray! ")
            lbl.grid(column=0, row=16)
        else:
            lbl = Label(window, text="Thine horse is frightened by the ogre and cast thee off.                     ")
            lbl.grid(column=0, row=13)
            lbl = Label(window, text="Thou sense great pain, as soon as ye fall to the ground.                                      ")
            lbl.grid(column=0, row=14)
            lbl = Label(window, text="The ogre has slammed a battle ax deep into thine back, nearly splitting ye asunder.")
            lbl.grid(column=0, row=15)
            lbl = Label(window, text='taking thine last breath, thou wonderest why did not thou say,"No Thanks!"')
            lbl.grid(column=0, row=16)
           

window = Tk()

window.title("Long Knights and Castle Daze")
 
window.geometry('600x500')
 
lbl = Label(window, text="Hello, Sir Knight! Join us on a quest to a castle.")
lbl.grid(column=0, row=0)
lbl = Label(window, text="We hear tell of great treasure in a castle not too far from here.")
lbl.grid(column=0, row=1)
lbl = Label(window, text="You're interest is peaked, so you consider joining this curious band of mis-fits.")
lbl.grid(column=0, row=2)
lbl = Label(window, text="                          ")
lbl.grid(column=0, row=3)
lbl = Label(window, text="Choose Thine Path:  (Prithee, Maketh thou choice wisely!)")
lbl.grid(column=0, row=4)

selected = IntVar()
rad1 = Radiobutton(window,text='Path I: Say "No Thanks"', value=1, variable=selected)
rad2 = Radiobutton(window,text='Path II: Ride along with them on your noble steed', value=2, variable=selected)
btn = Button(window, text="Clicketh Thou Here", command=clicked)


rad1.grid(column=0, row=6)
rad2.grid(column=0, row=7)
btn.grid(column=0, row=8)



window.mainloop()
