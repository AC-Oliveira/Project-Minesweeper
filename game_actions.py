from tkinter import * # type: ignore
from PIL import ImageTk, Image

class GameActions:
    def __init__(self) -> None:
        pass

    def bomb_click(self, window, bomb_names, number):
        GameActions.create_label(self,window,number, 'mine_blow')
        for child in window.winfo_children():
            try:
                #Empty string may raise a ValueError when trying to pass child name to integer
                child_number = int(child._name[8:]) #type: ignore
                if isinstance(child, Button):
                    if child._name in bomb_names: #type: ignore
                        child.destroy()
                        GameActions.create_label(self,window,child_number, 'mine')
                    elif 'myQuesti' in child._name: #type:ignore
                        child.destroy()
                        if child_number == number and f'myButton{child_number}' in bomb_names:
                          GameActions.create_label(self,window,child_number, 'mine_blow')
                        elif f'myButton{child_number}' in bomb_names:
                          GameActions.create_label(self,window,child_number, 'mine')
                        else:
                            child.destroy()
                            GameActions.create_label(self,window,child_number, 'question')
                    else:
                        child.destroy()
                        GameActions.create_label(self,window,child_number, 'button')

                # Solve clickable flag after game ending
                if isinstance(child, Label) and 'myButton' in child._name: #type:ignore
                    child.destroy()
                    GameActions.create_label(self,window,child_number, 'flag')
            except ValueError:
                pass


    def game_won(self, window, number):
        for child in window.winfo_children():
            if isinstance(child, Label) and 'myButton' in child._name: #type:ignore
                child_number = int(child._name[8:]) #type: ignore
                child.destroy()
                GameActions.create_label(self,window,child_number, 'flag')
            if isinstance(child, Button):
                child_number = int(child._name[8:]) #type: ignore
                child.destroy()
                if 'myQuesti' in child._name and f'{number}' not in child._name: #type:ignore
                    GameActions.create_label(self,window,child_number, 'question')
                elif 'myQuesti' in child._name and f'{number}' in child._name: #type:ignore
                    GameActions.create_label(self,window,child_number, 'empty')
                else:
                    GameActions.create_label(self,window,child_number, 'button')


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
          'mine': 'images/mine.png',
          'mine_blow': 'images/mine_blow.png',
          'button': 'images/button.png',
          'flag': 'images/flag.png',
          'question': 'images/question_mark.png'
        }

        img = Image.open(images[image_type]) #type:ignore
        img_resized = ImageTk.PhotoImage(img.resize((40,40), Image.ANTIALIAS)) #type:ignore
        myLabel = Label(window, image=img_resized)
        myLabel.image = img_resized # type: ignore
        myLabel.grid(row=number//9 + 1, column=number%9 + 1)
        myLabel.columnconfigure(number, weight=1)
        myLabel.rowconfigure(number, weight=1)
