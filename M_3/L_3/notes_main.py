#почни тут створювати додаток з розумними замітками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QListWidget,
                            QLayout, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit,
                            QLineEdit, QInputDialog)
import json
app = QApplication([])

#notes = {
#    "Welcome!" : {
#        "text" : "this is the best app for notes",
#        "tags" : ["instruction", "about"]
#        }
#}
#with open("notes_data.json", "w") as file:
#   json.dump(notes, file)
    
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
    text_edit.setText(notes[key]["text"])
    list_tags.clear()
    list_tags.addItems(notes[key]["tags"])
    
def add_note():
    note_name, ok = QInputDialog.getText(win, "Add note", "Note name")
    if ok and note_name != "":
        notes[note_name] = {"text": "", "tags": []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["tags"])
        
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["text"] = text_edit.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("select note to save")
        
def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        text_edit.clear()
        list_notes.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("Select note to delete")
        
def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = line_edit.text()
        if not tag in notes[key]["tags"]:
            notes[key]["tags"].append(tag)
            list_tags.addItem(tag)
            line_edit.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("select note to add tag")
                
def del_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["tags"].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]["tags"])
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("select note and note to delete a tag")
    
def search_by_tag():
    tag = line_edit.text()
    if btn_tag_search.text() == "Search" and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]["tags"]:
                notes_filtered[note] = notes[note]
        btn_tag_search.setText("Cancel searching")
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
    elif btn_tag_search.text() == "Cancel sarching":
        list_notes.clear()
        list_tags.clear()
        line_edit.clear()
        list_notes.addItems(notes)
    else:
        pass
            
btn_note_create.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
btn_note_save.clicked.connect(save_note)
btn_note_del.clicked.connect(del_note)

btn_tag_del.clicked.connect(del_tag)
btn_tag_search.clicked.connect(search_by_tag)
btn_tag_add.clicked.connect(add_tag)

win.show()
with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)
app.exec_()