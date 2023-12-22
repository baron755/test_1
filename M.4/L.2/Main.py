from PyQt5.QtWidgets import (
    QApplication, QWidget,
QFileDialog, QLabel, QListWidget,
QHBoxLayout, QVBoxLayout,
QPushButton
)
import os

app = QApplication([])
win = QWidget()

win.resize(700,500)
win.setWindowTitle("Easy editor")

btn_dir = QPushButton("Open folder")
btn_left = QPushButton("Left")
btn_right = QPushButton("right")
btn_bw = QPushButton("B/W")
btn_sharp = QPushButton("Sharp")
btn_flip = QPushButton("Flip")

lbl_image = QLabel()
lw_files = QListWidget()

row_1 = QHBoxLayout()
row_2 = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()


row_1.addWidget(btn_left)
row_1.addWidget(btn_right)
row_1.addWidget(btn_sharp)
row_1.addWidget(btn_bw)
row_1.addWidget(btn_flip)

col_1.addWidget(btn_dir)
col_1.addWidget(lw_files)

col_2.addWidget(lbl_image, 95)
col_2.addLayout(row_1)

row_2.addLayout(col_1,20)
row_2.addLayout(col_2,80)

win.setLayout(row_2)
win.show()

workdir = ""

def filter(files, extentions):
    result = []
    for filename in files:
        for ext in extentions:
            if filename.endswith(ext):
                result.append(filename)
    return result
    
def chose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    
def show_filenane_list():
    extentions = [".jpg", ".png", ".jpeg",
                  ".gif", ".bmp"]
    chose_workdir()
    filenames = filter(os.listdir(workdir),
                       extentions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)
        
btn_dir.clicked.connect(show_filenane_list)
app.exec_()
    
    




