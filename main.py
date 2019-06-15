import shutil
import sys
import traceback
import logging
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

logger = logging.getLogger(__name__)

def excepthook(excType=None, excValue=None, tracebackobj=None):
    ex = ''.join(traceback.format_exception(
        etype=excType,
        value=excValue,
        tb=tracebackobj,
    )).strip()
    logger.exception(ex)
    exception_dump(ex)


sys.excepthook = excepthook

global tid
tid = "init"


titles = {
    "X":"0004000000055D00",
    "Y":"0004000000055E00",
    "Omega Ruby":"000400000011C400",
    "Alpha Sapphire":"000400000011C500",
    "Sun":"0004000000164800",
    "Moon":"0004000000175E00",
    "Ultra Sun":"00040000001B5000",
    "Ultra Moon":"00040000001B5100"
}

garc = {
    "XY":[
        ("movesprite","a/0/0/5"),
        ("encdata","a/0/1/2"),
        ("trdata","a/0/3/8"),
        ("trclass","a/0/3/9"),
        ("trpoke","a/0/4/0"),
        ("mapGR","a/0/4/1"),
        ("mapMatrix","a/0/4/2"),
        ("wallpaper","a/1/0/4"),
        ("titlescreen","a/1/0/4"),
        ("maisonpkN","a/2/0/3"),
        ("maisontrN","a/2/0/4"),
        ("maisonpkS","a/2/0/5"),
        ("maisontrS","a/2/0/6"),
        ("move","a/2/1/2"),
        ("eggmove","a/2/1/3"),
        ("levelup","a/2/1/4"),
        ("evolution","a/2/1/5"),
        ("megaevo","a/2/1/6"),
        ("personal","a/2/1/8"),
        ("item","a/2/2/0"),
        ("gametext","a/0/7/2"),
        ("storytext","a/0/8/0")
    ],
    
    "ORAS":[
        ("encdata","a/0/1/3"),
        ("trdata","a/0/3/6"),
        ("trclass","a/0/3/7"),
        ("trpoke","a/0/3/8"),
        ("mapGR","a/0/3/9"),
        ("mapMatrix","a/0/4/0"),
        ("wallpaper","a/1/0/3"),
        ("titlescreen","a/1/5/2"),
        ("maisonpkN","a/1/8/2"),
        ("maisontrN","a/1/8/3"),
        ("maisonpkS","a/1/8/4"),
        ("maisontrS","a/1/8/5"),
        ("move","a/1/8/9"),
        ("eggmove","a/1/9/0"),
        ("levelup","a/1/9/1"),
        ("evolution","a/1/9/2"),
        ("megaevo","a/1/9/3"),
        ("personal","a/1/9/5"),
        ("item","a/1/9/7"),
        ("gametext","a/0/7/1"),
        ("storytext","a/0/7/9")
    ],
    "SM":[
        ("move","a/0/1/1"),
        ("eggmove","a/0/1/2"),
        ("levelup","a/0/1/3"),
        ("evolution","a/0/1/4"),
        ("megaevo","a/0/1/5"),
        ("personal","a/0/1/7"),
        ("item","a/0/1/9"),
        ("zonedata","a/0/7/7"),
        ("worlddata","a/0/9/1"),
        ("trclass","a/1/0/4"),
        ("trdata","a/1/0/5"),
        ("trpoke","a/1/0/6"),
        ("encounterstatic","a/1/5/5"),
        ("maisonpkN","a/2/7/7"),
        ("maisontrN","a/2/7/8"),
        ("maisonpkS","a/2/7/9"),
        ("maisontrS","a/2/8/0"),
        ("gametext","a/0/3/0"),
        ("storytext","a/0/4/0")
    ],
    "USUM":[
        ("move","a/0/1/1"),
        ("eggmove","a/0/1/2"),
        ("levelup","a/0/1/3"),
        ("evolution","a/0/1/4"),
        ("megaevo","a/0/1/5"),
        ("personal","a/0/1/7"),
        ("item","a/0/1/9"),
        ("zonedata","a/0/7/7"),
        ("worlddata","a/0/9/1"),
        ("trclass","a/1/0/5"),
        ("trdata","a/1/0/6"),
        ("trpoke","a/1/0/7"),
        ("encounterstatic", "a/1/5/9"),
        ("pickup","a/2/7/1"),
        ("maisonpkN","a/2/8/1"),
        ("maisontrN","a/2/8/2"),
        ("maisonpkS","a/2/8/3"),
        ("maisontrS","a/2/8/4"),
        ("gametext","a/0/3/2"),
        ("storytext","a/0/4/2"),
        ("encdata","a/0/8/3")
    ]
}

default_instructions = "Unhandled Exception: Click 'show details' and upload the contents to\nhttp://github.com/TheStraying11/Garc_Copy_Tool/issues along with\na description of what you did before this box popped up"

def exception_dump(exception, instructions=default_instructions):
    exception_message.setDetailedText(exception)
    exception_message.setText(instructions)
    exception_window.show()
def game(x):
    global title
    global tid
    title = x
    tid = titles[x]
    print(tid)
    main.hide()
    path.show()

def browse_0():
    edited_path.setText(str(QFileDialog.getExistingDirectory()))
def browse_1():
    pk3DS_path.setText(str(QFileDialog.getExistingDirectory()))
def browse_2():
    luma_line.setText(str(QFileDialog.getExistingDirectory()))
def submit_0():
    global edited_path_value
    global pk3DS_path_value
    edited_path_value = edited_path.text()
    pk3DS_path_value = pk3DS_path.text()
    check()
    
def submit_1():
    if not luma_line.text() ==  '':
        try:
            for i in copy:
                file = os.path.normcase(os.path.join(edited_path_value,i))
                dirs = os.path.normcase(os.path.join(luma_line.text(),'luma','titles',tid,i))
                dirs = dirs[:-2]
                os.makedirs(dirs, exist_ok=True)
                shutil.copy2(file, dirs)
        except:
            exception_dump('Invalid Path', "The path you've asked the program to copy to either is\ninvalid or cannot be written to, try using the browse\nbutton and make sure the folder isn't read only")

def check():
    global copy
    copy = []
    translate = {
        "X":"XY",
        "Y":"XY",
        "Omega Ruby":"ORAS",
        "Alpha Sapphire":"ORAS",
        "Sun":"SM",
        "Moon":"SM",
        "Ultra Sun":"USUM",
        "Ultra Moon":"USUM"
        }
    
    global title
    translated = translate[title]

    for i in garc[translated]:
        global edited_path_value
        global pk3DS_path_value
        try:                
            with open(os.path.normcase(os.path.join(edited_path_value,i[1])), 'rb') as e:
                with open(os.path.normcase(os.path.join(pk3DS_path_value,'backup',os.path.basename(os.path.dirname(edited_path_value)),'a',(i[0]+' ('+(i[1].replace('/','')))+')')), 'rb') as b:
                    if not e == b:
                        copy.append(i[1])
        except FileNotFoundError:
            exception_dump('FileNotFoundError','One or both of your file paths are incorrect or blank')
    if not copy == []:
        print(copy)
        path.hide()
        copy_window.show()

            
app = QApplication(['Garc Copy Tool'])
app.setApplicationName('Garc Copy Tool')

     
main = QWidget()

layout0 = QVBoxLayout()

game_label = QLabel("pick your game")
layout0.addWidget(game_label)
game_buttons = {
    
}

for i in titles:
    game_buttons[i] = QPushButton(i)
    game_buttons[i].clicked.connect(lambda: game(i))
    layout0.addWidget(game_buttons[i])

main.setLayout(layout0)
main.show()

path = QWidget()

layout1 = QVBoxLayout()

HLayout0 = QHBoxLayout()
HLayout1 = QHBoxLayout()
HLayout2 = QHBoxLayout()

edited_label = QLabel('Enter the path to the RomFS folder you edited in pk3DS')
edited_path = QLineEdit()
edited_path.setPlaceholderText('Enter the path to the RomFS folder you edited in pk3DS')
pk3DS_label = QLabel('Enter the path to your pk3DS folder')
pk3DS_path = QLineEdit()
pk3DS_path.setPlaceholderText('Enter the path to your pk3DS folder')

edit_browse = QPushButton('Browse')
edit_browse.clicked.connect(browse_0)
pk3DS_browse = QPushButton('Browse')
pk3DS_browse.clicked.connect(browse_1)
submit0 = QPushButton('Submit')
submit0.clicked.connect(submit_0)

HLayout0.addWidget(edited_path)
HLayout0.addWidget(edit_browse)
HLayout1.addWidget(pk3DS_path)
HLayout1.addWidget(pk3DS_browse)
HLayout2.addWidget(submit0)

layout1.addWidget(edited_label)
layout1.addLayout(HLayout0)
layout1.addWidget(pk3DS_label)
layout1.addLayout(HLayout1)
layout1.addLayout(HLayout2)

path.setLayout(layout1)

centerPoint = QDesktopWidget().availableGeometry().center()
x = centerPoint.x()
y = centerPoint.y()

path.setGeometry(x-247,y-116,494,232)

copy_window = QWidget()

luma_label = QLabel('Choose where you want to create the luma patch folder')
luma_line = QLineEdit()
luma_line.setPlaceholderText('Choose where you want to create the luma patch folder')
luma_browse = QPushButton('browse')
luma_browse.clicked.connect(browse_2)
luma_submit = QPushButton('submit')
luma_submit.clicked.connect(submit_1)

layout2 = QVBoxLayout()

HLayout3 = QHBoxLayout()
HLayout4 = QHBoxLayout()

HLayout3.addWidget(luma_line)
HLayout3.addWidget(luma_browse)
HLayout4.addWidget(luma_submit)

layout2.addWidget(luma_label)
layout2.addLayout(HLayout3)
layout2.addLayout(HLayout4)

copy_window.setLayout(layout2)

exception_window = QWidget()

layout3 = QVBoxLayout()

exception_message = QMessageBox()
exception_message.setStandardButtons(QMessageBox.NoButton)
exception_message.setStyleSheet("* { selection-background-color: #0278f7; selection-color: white }")


layout3.addWidget(exception_message)

exception_window.setLayout(layout3)


app.exec()
