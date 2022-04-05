from tkinter import * # type: ignore
from random import randint
from buttons import Buttons
from PIL import ImageTk, Image

class App():
  def __init__(self) -> None:
    # Define window and game properties.
    self.window: Tk  = Tk()
    self.bombs_coordinates: list = []
    self.bombs_side_numbers: dict = {}
    self.empty_squares: list = []

  @staticmethod
  def numbers_to_cordinates(numbers_list: list) -> list:
    NINE = 9
    coordinates_list = list(map(lambda number: [number // NINE, number % NINE], numbers_list))
    return coordinates_list

  @staticmethod
  def coordinates_to_numbers(cordinates_list: list) -> list:
    NINE = 9
    numbers_list = list(map(lambda coordinate: coordinate[0] * NINE + coordinate[1],cordinates_list))

    return numbers_list


  def side_numbers_list(self, numbers_list) -> list:
    coordinates_list = App.numbers_to_cordinates(numbers_list)
    side_coordinates_list = []
    
    for coordinate in coordinates_list:
      i = -1
      while i <= 1:
        if 0 <= coordinate[0] + i <= 8:
          j = -1
          while j <= 1:
            currrent_coordinate = [coordinate[0] + i, coordinate[1]+j]
            if 0 <= coordinate[1] + j <= 8 and currrent_coordinate not in coordinates_list:
              side_coordinates_list.append([coordinate[0]+i, coordinate[1]+j])

            j += 1
        i += 1

    side_numbers_list = App.coordinates_to_numbers(side_coordinates_list)
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
    while len(self.bombs_coordinates) <= 9:
      number = randint(0,80)
      if number not in self.bombs_coordinates:
        self.bombs_coordinates.append(number)
    self.bombs_coordinates.sort()


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


  def start_button(self, event):
    self.window.winfo_children()[1].destroy()
    self.window.winfo_children()[0].destroy()
    self.bombs_coordinates= []
    self.bombs_side_numbers: dict = {}
    self.empty_squares = []

    App.startWindow(self)

  def startWindow(self) -> None:
    App.random_bombs(self)
    App.side_numbers_count(self, App.side_numbers_list(self, self.bombs_coordinates))
    App.side_empty_squares(self)
    img = Image.open('images/smiley_face.png') #type:ignore
    img_resized = ImageTk.PhotoImage(img.resize((60,60), Image.ANTIALIAS)) #type:ignore
    play_button = Label(self.window, image=img_resized)
    play_button.grid(row=0,column=1)
    play_button.bind('<Button-1>', lambda event: self.start_button(event=event))
    game_grid = Label(self.window)
    game_grid.grid(row=1,column=1)
    self.window.columnconfigure(0, weight=1)
    self.window.rowconfigure(0, weight=1)

    buttons = Buttons(game_grid, self.bombs_coordinates, self.bombs_side_numbers, self.empty_squares, play_button)

    n = 0
    while n < 81:
      buttons.create_game_buttons(n)
      n += 1
    self.window.title('Minesweeper')
    self.window.mainloop()


root = App()
root.startWindow()