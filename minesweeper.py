from tkinter import * # type: ignore
from random import randint

from buttons import Buttons

class App:
  def __init__(self) -> None:
    # Define window and game properties.
    self.window = Tk()
    self.bombs = []
    self.side_numbers_count = {}

  def side_numbers(self):
    def numbers_to_cordinates(number):
      NINE = 9
      return [number // NINE, number % NINE]

    def coordinates_to_numbers(cordinates: list) -> list:
      numbers_list = list(map(lambda cordinate: cordinate[0] * 9 + cordinate[1],cordinates))
      numbers_list.sort()
      return numbers_list


    bombs_coordinates = []
    side_bombs_coordinates = []
    for number in self.bombs:
      bombs_coordinates.append(numbers_to_cordinates(number))
    bombs_coordinates.sort()

    for coordinate in bombs_coordinates:
      i = -1
      while i <= 1:
        if 0 <= coordinate[0] + i <= 8:
          j = -1
          while j <= 1:
            currrent_coordinate = [coordinate[0] + i, coordinate[1]+j]
            if 0 <= coordinate[1] + j <= 8 and currrent_coordinate not in bombs_coordinates:
              side_bombs_coordinates.append([coordinate[0]+i, coordinate[1]+j])
            j += 1
        i += 1
    side_bombs_coordinates.sort()
    side_numbers_list = coordinates_to_numbers(side_bombs_coordinates)


    for number in side_numbers_list:
      if number in self.side_numbers_count:
        self.side_numbers_count[number] += 1
      else:
        self.side_numbers_count[number] = 1


  def random_bombs(self):
    #generate bombs in random coordinates
    while len(self.bombs) <= 10:
      number = randint(0,80)
      if number not in self.bombs:
        self.bombs.append(number)

  def grid(self):
    def label_text(number):
      if number in self.bombs: return 'B'
      elif  number in self.side_numbers_count: return self.side_numbers_count[number]
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
    App.side_numbers(self)
    # App.grid(self)
    buttons = Buttons(self.window, self.bombs, self.side_numbers_count)
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
