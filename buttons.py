from tkinter import * # type: ignore
from PIL import ImageTk, Image
from game_actions import GameActions


class Buttons:
  def __init__(self, window, bombs, bombs_side_numbers, empty_squares) -> None:
    self.window = window
    self.bombs_list_numbers = bombs
    self.bombs_side_numbers = bombs_side_numbers
    self.empty_squares = empty_squares
    self.side_empties = []
    self.side_numbers = []
    self.removed_buttons = []


  def create_button(self, number) -> None:
    def handle_click(self, number) -> None:
      myButton.destroy()
      self.removed_buttons.append(myButton._name) # type: ignore
      if number in self.bombs_list_numbers:
          bomb_name_list = list(map(lambda number: f"myButton{number}", self.bombs_list_numbers))
          GameActions.bomb_click(self , self.window, number, bomb_name_list)

      elif number in self.bombs_side_numbers:
          GameActions.create_label(self, self.window, number, self.bombs_side_numbers[number])

      else:
        self.side_empty_list(number)
        for item in self.side_empties:
          button_name = f'myButton{item}'
          if button_name not in self.removed_buttons:
            self.removed_buttons.append(button_name)
            index = self.find_button_position(button_name)

            self.window.winfo_children()[index].destroy()

          GameActions.create_label(self, self.window, item, 'empty')
          Buttons.side_empty_list(self, item)

        for item in self.side_numbers:
          GameActions.create_label(self, self.window, item, self.bombs_side_numbers[item])

          button_name = f'myButton{item}'
          if button_name not in self.removed_buttons:
            self.removed_buttons.append(button_name)
            index = self.find_button_position(button_name)

            self.window.winfo_children()[index].destroy()
      if(len(self.removed_buttons) >= 71): print('Ganhou!')


    # border = Frame(self.window, highlightbackground='blue', highlightthickness=2, padx=20, pady=20)

    img = Image.open('images/button.png') #type:ignore
    img_resized = ImageTk.PhotoImage(img.resize((40,40), Image.ANTIALIAS)) #type:ignore
    myButton = Button(
      self.window, image=img_resized, command=lambda: handle_click(self, number), name=f'myButton{number}'
    )
    myButton.grid(row=number//9 , column=number%9)
    myButton.image = img_resized #type: ignore
  

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
          if 0 <= number_coordinate[1] + j <= 8 and curent_number not in self.bombs_list_numbers  and (
            curent_number not in self.side_empties and curent_number not in self.bombs_side_numbers.keys()
            ):
            self.side_empties.append(curent_number)
          elif curent_number in self.bombs_side_numbers.keys() and 0 <= number_coordinate[1] + j <= 8:
            self.side_numbers.append(curent_number)
          j += 1
      i += 1


  def find_button_position(self, name: str) -> int or None:
    names_list: list = list(map(lambda widget: widget._name,self.window.winfo_children()))
    index = names_list.index(name)
    return index