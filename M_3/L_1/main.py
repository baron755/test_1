from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from random import randint
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.example)
        
    def example(self):
        #number = randint(10000000, 99999999)
        allfavit = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num_list = "0123456789"
        real_number = ""
        while True:
            randomiser = randint(0, 100)
            if self.ui.cb_numbers.isChecked() and randomiser > 50:
                real_number += choise(num_list)
            if self.ui.cb_alphabet.isChecked() and randomiser > 50:
                real_number += choise(allfavit)
            
        if len(real_number) > 16:
            break
        self.ui.label_2.setText(str(real_number))
        

                
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()

        
        
