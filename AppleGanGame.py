import os
import random
import tkinter.messagebox
from tkinter import *

background_color = "#AEC6CF"


class AppleGame(object):
    def __init__(self, **kwargs):
        self.score=0
        self.total=0
        self.reset_window()

    def manual_reset_window(self,event):
        self.reset_window(False)

    def reset_window(self, init=True):
        if(init is False):
            self.master.destroy()
        master=Tk()
        pad = 3
        self._geom='1000x500+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))

        #bind the keys used for the app
        master.bind('<Escape>',self.close_app)
        master.bind('4',self.manual_reset_window)
        master.bind('l',self.pressed)
        master.bind('r',self.pressed)

        master.resizable(True, True)
        master.title('Apple-GAN')
        question_string = "Which one is the real apple?\n"
        Label(master, text=question_string,fg = "white",bg = background_color, font="none 24 bold").grid(row=1, column=1)

        # images from 001 to 947 are real, 1000 to 1998 are generated
        rand = random.choice(os.listdir(r"Grayscales/Reals"))
        print(rand)
        photoR = PhotoImage(file="Grayscales/Reals/" + rand)
        image_size= master.winfo_screenwidth()/4
        photoR = photoR.zoom(4)
        rand = random.choice(os.listdir(r"Grayscales/Fakes"))
        photoF = PhotoImage(file="Grayscales/Fakes/" + rand)
        photoF = photoF.zoom(4)

        self.Left_is_real = random.randint(0,1)

        if(self.Left_is_real==1):
            Label(master, image=photoR,fg = "white",bg = background_color, width = image_size).grid(row=1, column=0, sticky=E)
            Label(master, image=photoF,fg = "white",bg = background_color, width = image_size).grid(row=1, column=2, sticky=W)
        else:
            Label(master, image=photoF,fg = "white",bg = background_color, width = image_size).grid(row=1, column=0, sticky=E)
            Label(master, image=photoR,fg = "white",bg = background_color, width = image_size).grid(row=1, column=2, sticky=W)
        score_string = "Current score for the day: " + str(self.score) + " / " + str(self.total) + "\n"
        Label(master, text=score_string, fg = "white",bg = background_color, font="none 24 bold").grid(row=3, column=1, sticky =W)
        Label(master, text="Press the button corresponding to the apple you think is real", fg = "white",bg = background_color, font = "none 18 bold").grid(row=4,column=1,sticky=E)
        master.configure(background = background_color)

        self.master= master
        self.master.mainloop()


    def pressed(self,event):
        print(event.keysym)
        if(event.keysym == 'l' and self.Left_is_real==1):
            self.score = self.score+1
            Label(self.master, text="Congratulations!! You Guessed Correctly!", fg = "white",bg = background_color, font = "none 18 bold").grid(row=5,column=1)
        elif(event.keysym == 'r' and self.Left_is_real==0):
            self.score = self.score+1
            Label(self.master, text="Congratulations!! You Guessed Correctly!", fg = "white",bg = background_color, font = "none 18 bold").grid(row=5,column=1)
        else:
            Label(self.master, text="Sorry, you guessed wrong", fg = "white", bg = background_color, font = "none 18 bold").grid(row=5,column=1)
        self.total = self.total + 1
        Label(self.master, text="Press any button to try again!", fg = "white", bg = background_color, font = "none 18 bold").grid(row=6,column=1)
        self.master.bind('l',self.manual_reset_window)
        self.master.bind('r',self.manual_reset_window)

    def close_app(self,event):
        self.master.destroy()
        exit()


if __name__ == "__main__":
    app=AppleGame()
