from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QListWidget,
                            QLayout, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit,
                            QLineEdit, QInputDialog)


app = QApplication([])
notes = []
    
win = QWidget()
win.setWindowTitle("Smart notes")
win.resize(900,600)

list_notes = QListWidget()
list_tags = QListWidget()

btn_note_create = QPushButton("Cleate")
btn_note_del = QPushButton("Delete")
btn_note_save = QPushButton("Save")
btn_tag_add = QPushButton("Add")
btn_tag_del = QPushButton("Delete")
btn_tag_search = QPushButton("Search")

line_edit = QLineEdit()
text_edit = QTextEdit()
line_edit.setPlaceholderText("Enter tag...")

col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

row_1 = QHBoxLayout()
row_2 = QHBoxLayout()
row_3 = QHBoxLayout()
row_4 = QHBoxLayout()

layout = QHBoxLayout()

row_1.addWidget(btn_note_create)
row_1.addWidget(btn_note_del)
row_2.addWidget(btn_note_save)
row_3.addWidget(btn_tag_add)
row_3.addWidget(btn_tag_del)
row_4.addWidget(btn_tag_search)

col_1.addWidget(text_edit)
col_2.addWidget(list_notes)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addWidget(list_tags)
col_2.addWidget(line_edit)
col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout.addLayout(col_1, stretch=2)
layout.addLayout(col_2, stretch=1)
win.setLayout(layout)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            text_edit.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])

def add_note():
    note_name, ok = QInputDialog.getText(win, "Add note", "Note nane")
    if ok and note_name != "":
        note = list()
        note = [note_name, "", []]
        notes.append(note)
        list_notes.addItem(note[0])
        list_tags.addItems(note[2])
        with open(str(len(notes)-1)+".txt", "w", encoding="UTF8") as file:
            file.write(note[0]+"\n")

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = text_edit.toPlainText()
                with open (str*(index)+".txt", "w", encoding="UTF8") as file:
                    file.write(note[0]+"\n")
                    file.write(note[1]+"\n")
                    for t in note[2]:
                        file.write(t+" ")
                    #file.write("\n")
            index += 1
                    
list_notes.itemClicked.connect(show_note)
btn_note_create.clicked.connect(add_note)
btn_note_save.clicked.connect(save_note)                             

win.show()
name = 0
while True:
    note = []
    filename = str(name)+".txt"
    try:
        with open(filename, "r", encoding="UTF8") as file:
            for line in file:
                line = line.replace("\n", "")
                note.append(line)
        tags = note[2].split(" ")
        note[2] = tags 
        notes.append(note)
        name +=1
    except IOError:
        break
    
for note in notes:
    list_notes.addItem(note[0])        
app.exec_()