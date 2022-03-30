from tkinter import * # type: ignore
from PIL import ImageTk, Image

class Buttons:
  def __init__(self, window, bombs, side_numbers_count) -> None:
    self.window = window
    self.bombs = bombs
    self.side_numbers_count = side_numbers_count



  def create_button(self, number) -> None:
    def handle_click(number) -> None:
      myButton.destroy()
      if number in self.bombs:
        img = ImageTk.PhotoImage(Image.open('icons8-naval-mine-25.png')) # type: ignore
        myLabel = Label(self.window, image=img)
        myLabel.image = img # type: ignore
        myLabel.grid(row=number//9 , column=number%9)
      elif number in self.side_numbers_count:
        myLabel = Label(self.window, text=f'{self.side_numbers_count[number]}', borderwidth=4, relief="sunken")
        myLabel.grid(row=number//9 , column=number%9, padx=30,pady=30)
      else:
        myLabel = Label(self.window, text='  ', borderwidth=4, relief="sunken")
        myLabel.grid(row=number//9 , column=number%9)
    
    border = Frame(self.window, highlightbackground='blue', highlightthickness=2, padx=20, pady=20)

    myButton = Button(
      border, text=" ", command=lambda: handle_click(number)
    )
    border.grid(row=number//9 , column=number%9)
