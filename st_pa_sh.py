from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QMessageBox, QRadioButton, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QWidget
from random import shuffle

pomosh_pls = ""

def show_win():
    global pomosh_pls
    victory_win = QMessageBox()
    i = 'Вы победили!\nКомпьютер выбрал '+str(pomosh_pls)
    victory_win.setText(i)
    victory_win.exec()
def show_lose():
    global pomosh_pls
    victory_win= QMessageBox()
    i = 'Вы проиграли!\nКомпьютер выбрал '+str(pomosh_pls)
    victory_win.setText(i)
    victory_win.exec()
def show_n():
    global pomosh_pls
    victory_win= QMessageBox()
    i = 'Ничья!\nКомпьютер тоже выбрал '+str(pomosh_pls)
    victory_win.setText(i)
    victory_win.exec()
def start():
    global pomosh_pls
    shuffle(main_list)
    pomosh_pls = main_list[1]
    if pomosh_pls == "Камень":
        button_stone.clicked.connect(show_n)
        nozhnitsy_rezat.clicked.connect(show_lose)
        bumaga_gam.clicked.connect(show_win)
    elif pomosh_pls == "Бумага":
        button_stone.clicked.connect(show_lose)
        nozhnitsy_rezat.clicked.connect(show_win)
        bumaga_gam.clicked.connect(show_n)
    else:
        button_stone.clicked.connect(show_win)
        nozhnitsy_rezat.clicked.connect(show_n)
        bumaga_gam.clicked.connect(show_lose)
main_list = ["Камень", "Ножницы", "Бумага"]
app = QApplication([])
main_win = QWidget()
main_win.show()
main_win.resize(700, 500)
main_win.setWindowTitle('Камень-ножницы-бумага')

main_label = QLabel("Выбери предмет")
button_stone = QRadioButton("Камень")
bumaga_gam = QRadioButton("Бумага")
nozhnitsy_rezat = QRadioButton("Ножницы")
main_layout = QVBoxLayout()
button_layout = QHBoxLayout()
button_layout.addWidget(button_stone)
button_layout.addWidget(bumaga_gam)
button_layout.addWidget(nozhnitsy_rezat)
main_layout.addWidget(main_label)
main_layout.addLayout(button_layout)
main_win.setLayout(main_layout)
start()
main_win.show()
app.exec()