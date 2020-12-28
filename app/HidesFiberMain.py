#/usr/local/bin/python3
# usage: python3 HidesFiberMain.py

class gui:
    """
    make a main gui for HIDES6 GUI
    """

    def __init__(self, test):
        self.testprint = test

    def makegui(self):
        print(self.testprint)

if __name__ == '__main__':
    test = "HIDES6GUI"
    gui = gui(test)
    gui.makegui()


    

