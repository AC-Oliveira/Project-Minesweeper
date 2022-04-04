from tkinter import *
import tkinter # type: ignore
from PIL import ImageTk, Image

class GameActions:
    def __init__(self) -> None:
        pass

    def bomb_click(self, window, number, bomb_names):
        print('Perdeu!')
        GameActions.create_label(self,window,number, 'mine_blow')

        # for index in bomb_index:
        #   window.winfo_children()
        for child in window.winfo_children():
          # print(isinstance(child, tkinter.Button))
          if isinstance(child, tkinter.Button):
            if child._name in bomb_names: #type: ignore
                child_number = int(child._name[8:]) #type: ignore
                child.destroy()
                GameActions.create_label(self,window,child_number, 'mine')
            else:
                child['state'] = DISABLED


    def create_label(self, window, number, image_type):
        images = {
          1:'images/1.png',
          2:'images/2.png',
          3:'images/3.png',
          4:'images/4.png',
          5:'images/5.png',
          6:'images/6.png',
          7:'images/7.png',
          8:'images/8.png',
          'empty': 'images/empty_field.png',
          'flag': 'images/flag.png',
          'button': 'images/button.png',
          'mine': 'images/mine.png',
          'mine_blow': 'images/mine_blow.png'
        }

        img = Image.open(images[image_type]) #type:ignore
        img_resized = ImageTk.PhotoImage(img.resize((40,40), Image.ANTIALIAS)) #type:ignore
        myLabel = Label(window, image=img_resized)
        myLabel.image = img_resized # type: ignore
        myLabel.grid(row=number//9 , column=number%9)
        myLabel.columnconfigure(number, weight=1)
        myLabel.rowconfigure(number, weight=1)