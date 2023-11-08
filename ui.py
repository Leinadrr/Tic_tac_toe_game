import sys
from conditions import who_win
from PySide6.QtCore import QFile, QSize
from PySide6.QtGui import QIcon, QPixmap, QAction
from PySide6.QtWidgets import QToolBar, QApplication, QLabel, QMainWindow, QPushButton, QWidget, QGridLayout


class AnotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Player variables, title window and layout
        self.player1 = True
        self.player2 = True
        self.locations = {}
        self.setWindowTitle("Tic, tac, toe!")
        self.setMinimumSize(800, 800)

        self.locations = {}
        layout = QGridLayout()

        # Style for the buttons loaded from the qss file
        style_file = QFile("styles.qss")
        style_file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = style_file.readAll()
        self.setStyleSheet(str(stylesheet, encoding='utf-8'))

        # Setting up the nine buttons and its behavior
        self.button1 = QPushButton()
        self.button1.setObjectName("1")
        self.button1.clicked.connect(self.who_play)
        layout.addWidget(self.button1, 0, 0)

        self.button2 = QPushButton()
        self.button2.setObjectName("2")
        self.button2.clicked.connect(self.who_play)
        layout.addWidget(self.button2, 0, 1)

        self.button3 = QPushButton()
        self.button3.setObjectName("3")
        self.button3.clicked.connect(self.who_play)
        layout.addWidget(self.button3, 0, 2)

        self.button4 = QPushButton()
        self.button4.setObjectName("4")
        self.button4.clicked.connect(self.who_play)
        layout.addWidget(self.button4, 1, 0)

        self.button5 = QPushButton()
        self.button5.setObjectName("5")
        self.button5.clicked.connect(self.who_play)
        layout.addWidget(self.button5, 1, 1)

        self.button6 = QPushButton()
        self.button6.setObjectName("6")
        self.button6.clicked.connect(self.who_play)
        layout.addWidget(self.button6, 1, 2)

        self.button7 = QPushButton()
        self.button7.setObjectName("7")
        self.button7.clicked.connect(self.who_play)
        layout.addWidget(self.button7, 2, 0)

        self.button8 = QPushButton()
        self.button8.setObjectName("8")
        self.button8.clicked.connect(self.who_play)
        layout.addWidget(self.button8, 2, 1)

        self.button9 = QPushButton()
        self.button9.setObjectName("9")
        self.button9.clicked.connect(self.who_play)
        layout.addWidget(self.button9, 2, 2)

        self.winner = QLabel()
        self.winner.setObjectName("winner")
        self.winner.setStyleSheet("background: black; color: white; font-size: 30px;")
        self.winner.hide()
        layout.addWidget(self.winner)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Toolbar configuration section
        toolbar = QToolBar("menu ")
        self.addToolBar(toolbar)

        button_play = QAction("Close game", self)
        button_play.triggered.connect(self.quit_game)
        toolbar.addAction(button_play)

        # Setting up player marks (icons into the buttons)
        self.x = QPixmap("imgs/x.png")
        self.icon_x = QIcon(self.x)

        self.o = QPixmap("imgs/o.png")
        self.icon_o = QIcon(self.o)

    # Menu bar buttons logic
    def quit_game(self):
        sys.exit(app.exec())

    # Logic for painting the buttons #
    def who_play(self):
        if self.player1:
            if self.sender().clicked:
                self.locations[int(self.sender().objectName())] = "X"
                self.sender().setIcon(self.x)
                self.sender().setIconSize(QSize(200, 200))
                who_win(self.locations)
                self.player1 = False
                if who_win(self.locations):
                    self.winner.setText("Player 1 wins!")
                    self.winner.show()
        else:
            if self.sender().clicked:
                self.locations[int(self.sender().objectName())] = "O"
                self.sender().setIcon(self.o)
                self.sender().setIconSize(QSize(200, 200))
                who_win(self.locations)
                self.player1 = True
                if who_win(self.locations) == False:
                    self.winner.setText("Player 2 wins!")
                    self.winner.show()
        if len(self.locations) >= 8:
            self.winner.setText("This is a draw!")
            self.winner.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle("Tic, tac, toe game")
        self.button = QPushButton("""
        Welcome! Push to play!
        
        (P.S. push again if you want to 
        restart the game)
        """)
        self.button.setFixedSize(400, 100)
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)

    def toggle_window(self):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None


app = QApplication(sys.argv)
w = MainWindow()
w.setGeometry(220, 180, 400, 100)
w.show()

app.exec()
