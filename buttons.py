from cgitb import text
from tkinter import * # type: ignore
from PIL import ImageTk, Image
from game_actions import GameActions


class Buttons:
  def __init__(self, window, bombs, bombs_side_numbers, empty_squares, play_button) -> None:
    self.window = window
    self.bombs_list_numbers = bombs
    self.bombs_side_numbers = bombs_side_numbers
    self.empty_squares = empty_squares
    self.side_empties = []
    self.side_numbers = []
    self.removed_buttons = []
    self.game_status = play_button


  def create_game_buttons(self, number) -> None:
    def handle_left_click(self, number) -> None:
      myButton.destroy()
      self.removed_buttons.append(myButton._name) # type: ignore
      if number in self.bombs_list_numbers:
          bomb_name_list = list(map(lambda number: f"myButton{number}", self.bombs_list_numbers))
          img = Image.open('images/dead_face.png') #type:ignore
          img_resized = ImageTk.PhotoImage(img.resize((60,60), Image.ANTIALIAS)) #type:ignore
          self.game_status.configure(image=img_resized)
          self.game_status.image=img_resized

          GameActions.bomb_click(self , self.window, bomb_name_list, number)

      elif number in self.bombs_side_numbers:
          GameActions.create_label(self, self.window, number, self.bombs_side_numbers[number])

      else:
        self.side_empty_list(number)
        for item in self.side_empties:
          button_name = f'myButton{item}'
          # Fix: Empty label has no image when clicked.
          if button_name == f'myButton{number}':
            GameActions.create_label(self, self.window, item, 'empty')
          if button_name not in self.removed_buttons:
              # Fix: Now Flag Label and Question Button aren't removed when a empty space is clicked.
              # Fix: When button name isn't myButton... a ValueError is raised by index function.
              try:
                  index = self.find_button_position(button_name)
                  if not isinstance(self.window.winfo_children()[index], Label) and button_name == self.window.winfo_children()[index]._name:
                      self.removed_buttons.append(button_name)
                      self.window.winfo_children()[index].destroy()
                      GameActions.create_label(self, self.window, item, 'empty')
                      Buttons.side_empty_list(self, item)
              except ValueError:
                  pass

        for item in self.side_numbers:
            try:
                button_name = f'myButton{item}'
                index = self.find_button_position(button_name)
                if not isinstance(self.window.winfo_children()[index], Label) and button_name == self.window.winfo_children()[index]._name:
                    GameActions.create_label(self, self.window, item, self.bombs_side_numbers[item])
                    # if button_name == f'myButton{number}':
                    if button_name not in self.removed_buttons:
                        self.removed_buttons.append(button_name)
                        self.window.winfo_children()[index].destroy()
            except ValueError:
                pass
      #Fix: False positive when the last button clicked is a bomb.
      if(len(self.removed_buttons) >= 71) and number not in self.bombs_list_numbers:
          img = Image.open('images/sunglasses_face.png') #type:ignore
          img_resized = ImageTk.PhotoImage(img.resize((60,60), Image.ANTIALIAS)) #type:ignore
          self.game_status.configure(image=img_resized)
          self.game_status.image=img_resized
          GameActions.game_won(self , self.window)


    def handle_button_right_click(event):
        myButton.destroy()
        Buttons.create_button_by_type(self, handle_left_click, handle_flag_click, number, 'flag')


    def handle_flag_click(event):
      event.widget.destroy()
      Buttons.create_button_by_type(self, handle_left_click, handle_question_click, number, 'question')


    def handle_question_click(event):
      event.widget.destroy()
      Buttons.create_button_by_type(self, handle_left_click, handle_button_right_click, number, 'button')


    myButton = Buttons.create_button_by_type(self, handle_left_click, handle_button_right_click, number, 'button')


  def create_button_by_type(self, handle_left_click, handle_right_click, number, type):
    images = {
      'button': 'images/button.png',
      'flag': 'images/flag.png',
      'question': 'images/question_mark.png',
    }

    img = Image.open(images[type]) #type:ignore
    img_resized = ImageTk.PhotoImage(img.resize((40,40), Image.ANTIALIAS)) #type:ignore
    myButton = Button(
      self.window, image=img_resized, command=lambda: handle_left_click(self, number), name=f'myButton{number}'
    )
    if type == 'flag':
        myButton.destroy()
        myButton = Label(self.window, image=img_resized, name=f'myButton{number}')
    if type == 'question':
        myButton.destroy()
        myButton = Button(self.window, image=img_resized, command=lambda: handle_left_click(self, number), name=f'myQuesti{number}')

    myButton.bind('<Button-3>', handle_right_click)
    myButton.grid(row=number//9 + 1, column=number%9 + 1)
    myButton.image = img_resized #type: ignore

    return myButton


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