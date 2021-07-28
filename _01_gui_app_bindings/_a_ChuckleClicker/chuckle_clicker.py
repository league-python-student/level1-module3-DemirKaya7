"""
 Create an app that tells a joke, then a punchline
"""
import tkinter as tk
import random
from tkinter import messagebox


# Use this function to return a random character
def generate_random_letter():
    return chr(random.randint(0, 25) + ord('a'))


class ChuckleClicker(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize 2 buttons (tk.Button)
        #  one button for the joke and another for the punchline
        jokeButton = tk.Button(self, text="Joke")
        punchlineButton = tk.Button(self, text="Punchline")
        # TODO: Place the 2 buttons next to each other (see example image)
        jokeButton.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        punchlineButton.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
        # TODO: Call the joke button's bind() method to call the on_joke()
        #  method when a mouse button is pressed
        #  example: self.joke_button.bind('<ButtonPress>', self.on_joke)
        jokeButton.bind('<ButtonPress>', self.on_joke)

        # TODO: Call the joke button's bind() method to call the on_punchline()
        #  method when a mouse button is pressed
        punchlineButton.bind('<ButtonPress>', self.on_punchline)


    def on_joke(self, event):
        # TODO: Write your joke below!
        print("What did the pirate say when he turned 80?")

    def on_punchline(self, event):
        # TODO: Write a punchline to your joke!
        print("Aye Matey")


if __name__ == '__main__':

    # TODO: Create a new ChuckleClicker object and set the title and geometry.
    #  Remember to call mainloop() at the end
    x = ChuckleClicker()
    x.title("Chuckle clicker")
    x.geometry("500x500")
    x.mainloop()

