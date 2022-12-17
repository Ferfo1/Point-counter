# Scoreboard V 1.0.
# Creator Ferfo1

# Importing modules
from tkinter import *

# Creating variable's
red = -1
blue = -1
bluestr = ""
redstr = ""

class App(Tk):
    WIDTH = 300
    HEIGHT = 600

    def __init__(self):
        super().__init__()
        self.button_2 = None
        self.title("Fej vagy Írás?")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.attributes('-fullscreen', True)
        self.redf()
        self.bluef()

    # Functions
    def redf(self):
        global red
        global redstr
        red += 1
        redstr = str(red)
        print(redstr)

        szoveg1 = Label(text=('Red team : ' + redstr), master=self, bg="#D60000", font=2000)
        szoveg1.grid(row=1, column=3, columnspan=2, pady=3, padx=4, sticky="we")
        self.button_2 = Button(master=self, width=87, height=50, bg="#D60000", command=self.redf)
        self.button_2.grid(row=7, column=3, columnspan=2, padx=6, pady=5)

        # Minus one point
        def minusred():
            global red
            global redstr
            red -= 1
            redstr = str(red)
            print(redstr)
            szoveg1 = Label(text=('Red team : ' + redstr), master=self, bg="#D60000", font=2000)
            szoveg1.grid(row=1, column=3, columnspan=2, pady=3, padx=4, sticky="we")
        self.button_3 = Button(master=self, bg="#A40000", text="Minus one point for red team.", command=minusred, border=0)
        self.button_3.grid(row=7, column=3, columnspan=2, padx=6, pady=5)

    bluestr = 0
    def bluef(self):
        global blue
        global bluestr
        blue += 1
        bluestr = str(blue)
        print(bluestr)
        self.button_1 = Button(master=self, width=90, height=50, bg="#0060E3", command=self.bluef, foreground="white",)
        self.button_1.grid(row=7, column=2, columnspan=1, padx=4, pady=0, sticky="we")
        szoveg1 = Label(text=('Blue team : ' + bluestr), master=self, bg="#0060E3", font=600, foreground="white")
        szoveg1.grid(row=1, column=2, columnspan=1, pady=3, padx=3, sticky="we")
        # Minus one point
        def minusblue():
            global blue
            global bluestr
            blue -= 1
            bluestr= str(blue)
            print(bluestr)
            szoveg1 = Label(text=('Blue team : ' + bluestr), master=self, bg="#0060E3", font=600, foreground="white")
            szoveg1.grid(row=1, column=2, columnspan=1, pady=3, padx=3, sticky="we")
        self.button_3 = Button(master=self, bg="#0045A4", text="Minus one point for blue team.", command=minusblue, border=0)
        self.button_3.grid(row=7, column=2, columnspan=1, padx=4, pady=0)

if __name__ == "__main__":
    app = App()
    app.mainloop()
