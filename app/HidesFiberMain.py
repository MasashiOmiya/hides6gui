#/usr/local/bin/python3
# usage: python3 HidesFiberMain.py

import argparse
import tkinter as tk
import tkinter.ttk as ttk

class gui:
    """
    make a main gui for HIDES6 GUI
    """

    def __init__(self, test):
        self.testprint = test

    def makegui(self):
        print("### HIDES Fiber GUI ver 0.1 ### %s" %(self.testprint))

        guimain = tk.Tk()
        guimain.title("Main")
        guimain.geometry("1000x1000")
        guimain.Label = tk.Label(text=u'test')
        guimain['menu'] = setMenu()


        guimain.mainloop()


class setMenu(tk.Menu):
    """
    Create Menu to select the GUI mode 4K or FullHD
    """

    def __init__(self,master=None):
        super().__init__(master)
        self.create_mode_menu()

    def create_mode_menu(self):
        mode = tk.Menu(self)
        mode.add_command(label='4K')
        mode.add_command(label='Full HD')
        self.add_cascade(menu=mode, label='Mode')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='### HIDES Fiber GUI ver 0.1 ###')
    parser.add_argument('--test', help='test file', type=str)
    parser.add_argument('--test2', help='test name', type=str)
    args = parser.parse_args()

    gui = gui(args.test)
    gui.makegui()


    

