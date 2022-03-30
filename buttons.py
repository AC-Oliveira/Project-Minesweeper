from tkinter import * # type: ignore
from PIL import ImageTk, Image


class Buttons:
  def __init__(self, window, bombs, side_numbers_count, empty_squares) -> None:
    self.window = window
    self.bombs_coordinates = bombs
    self.side_numbers_count = side_numbers_count
    self.empty_squares = empty_squares
    self.side_empties = []
    self.side_numbers = []


  def create_button(self, number) -> None:
    def handle_click(number) -> None:
      myButton.destroy()
      if number in self.bombs_coordinates:
        print('Perdeu!')
        img = ImageTk.PhotoImage(Image.open('icons8-naval-mine-25.png')) # type: ignore
        myLabel = Label(self.window, image=img)
        myLabel.image = img # type: ignore
        myLabel.grid(row=number//9 , column=number%9)
        myLabel.columnconfigure(number, weight=1)
        myLabel.rowconfigure(number, weight=1)
      elif number in self.side_numbers_count:
        myLabel = Label(self.window, text=f'{self.side_numbers_count[number]} ', borderwidth=4, relief="sunken")
        myLabel.grid(row=number//9 , column=number%9)
        myLabel.columnconfigure(number, weight=1)
        myLabel.rowconfigure(number, weight=1)
      else:
        self.side_empty_list(number)
        for item in self.side_empties:
          Buttons.side_empty_list(self, item)
          myLabel = Label(self.window, text='  ', borderwidth=4, relief="sunken")
          myLabel.grid(row=item//9 , column=item%9)
          myLabel.columnconfigure(item, weight=1)
          myLabel.rowconfigure(item, weight=1)
        for item in self.side_numbers:
          myLabel = Label(self.window, text=f'{self.side_numbers_count[item]}', borderwidth=4, relief="sunken")
          myLabel.grid(row=item//9 , column=item%9)
          myLabel.columnconfigure(item, weight=1)
          myLabel.rowconfigure(item, weight=1)


    # border = Frame(self.window, highlightbackground='blue', highlightthickness=2, padx=20, pady=20)
    myButton = Button(
      self.window, text=' ', command=lambda: handle_click(number)
    )
    myButton.grid(row=number//9 , column=number%9)


  def side_empty_list(self, number: int) -> None:
    number_to_coordinate = lambda _number: [_number//9, _number%9]
    coordinate_to_number = lambda _coordinate: _coordinate[0]*9 + _coordinate[1]
    number_coordinate = number_to_coordinate(number)
    i = -1
    while i <= 1:
      if 0 <= number_coordinate[0] + i <= 8:
        j = -1
        while j <= 1:
          curent_number = coordinate_to_number([number_coordinate[0] + i, number_coordinate[1] + j])
          if 0 <= number_coordinate[1] + j <= 8 and curent_number not in self.bombs_coordinates  and (
            curent_number not in self.side_empties and curent_number not in self.side_numbers_count.keys()
            ):
            self.side_empties.append(curent_number)
          elif curent_number in self.side_numbers_count.keys():
            self.side_numbers.append(curent_number)
          j += 1
      i += 1