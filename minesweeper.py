from tkinter import * # type: ignore
from random import randint

from numpy import empty

from buttons import Buttons

class App:
  def __init__(self) -> None:
    # Define window and game properties.
    self.window: Tk  = Tk()
    self.bombs_coordinates: list = []
    self.bombs_side_numbers: dict = {}
    self.empty_squares: list = []


  def numbers_to_cordinates(self, numbers_list: list) -> list:
    NINE = 9
    coordinates_list = list(map(lambda number: [number // NINE, number % NINE], numbers_list))
    return coordinates_list


  def coordinates_to_numbers(self, cordinates_list: list) -> list:
    NINE = 9
    numbers_list = list(map(lambda coordinate: coordinate[0] * NINE + coordinate[1],cordinates_list))

    return numbers_list


  def side_numbers_list(self, numbers_list, type='numbers') -> list:
    coordinates_list = App.numbers_to_cordinates(self, numbers_list)
    side_coordinates_list = []

    for coordinate in coordinates_list:
      i = -1
      while i <= 1:
        if 0 <= coordinate[0] + i <= 8:
          j = -1
          while j <= 1:
            currrent_coordinate = [coordinate[0] + i, coordinate[1]+j]
            if type == 'numbers' and 0 <= coordinate[1] + j <= 8 and currrent_coordinate not in coordinates_list:
              side_coordinates_list.append([coordinate[0]+i, coordinate[1]+j])

            elif 0 <= coordinate[1] + j <= 8 and coordinate[0] * 9 + coordinate[1] in self.empty_squares:
              side_coordinates_list.append([coordinate[0]+i, coordinate[1]+j])

            j += 1
        i += 1

    side_numbers_list = App.coordinates_to_numbers(self, side_coordinates_list)
    
    return side_numbers_list


  def side_numbers_count(self, side_numbers_list):
    for number in side_numbers_list:
      if number in self.bombs_side_numbers:
        self.bombs_side_numbers[number] += 1
      else:
        self.bombs_side_numbers[number] = 1



  def side_empty_squares(self):
    n = 0
    while n <= 80:
      if n not in self.bombs_coordinates and n not in self.bombs_side_numbers.keys():
        self.empty_squares.append(n)
      n += 1


  def random_bombs(self) -> None:
    #generate bombs in random coordinates
    while len(self.bombs_coordinates) <= 9:
      number = randint(0,80)
      if number not in self.bombs_coordinates:
        self.bombs_coordinates.append(number)


  def grid(self) -> None:
    def label_text(number):
      if number in self.bombs_coordinates: return 'B'
      elif  number in self.bombs_side_numbers: return self.bombs_side_numbers[number]
      else: return '  '

    def create_label(number) -> None:
      myLabel = Label(
        self.window, text=label_text(number), borderwidth=2, relief="sunken"
      )
      myLabel.grid(row=number//9 , column=number%9)

    n = 0
    while n < 81:
      create_label(n)
      n += 1


  def startWindow(self) -> None:
    # frame.pack()
    App.random_bombs(self)
    App.side_numbers_count(self, App.side_numbers_list(self, self.bombs_coordinates))
    App.side_empty_squares(self)

    # App.grid(self)

    buttons = Buttons(self.window, self.bombs_coordinates, self.bombs_side_numbers, self.empty_squares)
    # buttons.side_empty_list(10)
    n = 0
    while n < 81:
      buttons.create_button(n)
      self.window.columnconfigure(n, weight=1)
      self.window.rowconfigure(n, weight=1)
      n += 1

    self.window.title('Campo Minado')
    # self.window.maxsize(280,320)
    # self.window.minsize(280,320)
    self.window.mainloop()


newApp = App()
newApp.startWindow()
