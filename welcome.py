from PyQt5 import QtCore, QtGui, QtWidgets 
from crowd_monitor import crowd

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)

        # Background Image
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:\Mini PROJECT\Person_counting\people-counting-systems.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Transparent Overlay for Form Fields
        self.overlay = QtWidgets.QWidget(Form)
        self.overlay.setGeometry(QtCore.QRect(200, 150, 800, 500))
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 180); border-radius: 20px;")
        self.overlay.setObjectName("overlay")

        # Main Title (Further Reduced Font Size)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 160, 700, 81))  # Width remains, font size reduced
        font = QtGui.QFont()
        font.setPointSize(24)  # Further reduced font size to ensure full visibility
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        # Username Label (Fixed width to prevent text cutting off)
        self.label_username = QtWidgets.QLabel(Form)
        self.label_username.setGeometry(QtCore.QRect(250, 290, 200, 51))  # Increased width to fully show "Username"
        font.setPointSize(18)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_username.setText("Username:")
        self.label_username.setObjectName("label_username")

        # Username Input (with spacing)
        self.lineEdit_username = QtWidgets.QLineEdit(Form)
        self.lineEdit_username.setGeometry(QtCore.QRect(470, 290, 300, 50))  # Adjusted position for spacing
        font.setPointSize(18)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setStyleSheet("border-radius: 10px; padding: 5px;")
        self.lineEdit_username.setObjectName("lineEdit_username")

        # Password Label (Fixed width to prevent text cutting off)
        self.label_password = QtWidgets.QLabel(Form)
        self.label_password.setGeometry(QtCore.QRect(250, 370, 200, 51))  # Increased width to fully show "Password"
        font.setPointSize(18)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_password.setText("Password:")
        self.label_password.setObjectName("label_password")

        # Password Input (with spacing)
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(470, 370, 300, 50))  # Adjusted position for spacing
        font.setPointSize(18)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("border-radius: 10px; padding: 5px;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)  # Hide password characters
        self.lineEdit_password.setObjectName("lineEdit_password")

        # Login Button
        self.pushButton_login = QtWidgets.QPushButton(Form)
        self.pushButton_login.setGeometry(QtCore.QRect(350, 460, 191, 61))
        font.setPointSize(19)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("""
            QPushButton {
                background-color: rgb(233, 23, 142);
                color: white;
                border-radius: 30px;
            }
            QPushButton:hover {
                background-color: rgb(200, 20, 120);
            }
        """)
        self.pushButton_login.setText("Login")
        self.pushButton_login.setObjectName("pushButton_login")

        # Connect button to function
        self.pushButton_login.clicked.connect(self.check_credentials)     

        # Set window title and UI layout
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowTitle("Login Page")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Page"))
        self.label_2.setText(_translate("Form", "SMART COUNTING SYSTEM"))  # Full title now visible

    def check_credentials(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        # Simple validation (replace with proper authentication logic)
        if username == "admin" and password == "password":
            print("Login successful!")
            self.next_page()
        else:
            print("Invalid username or password")

    def next_page(self):
        print("HELLO WELCOME TO COUNTING SYSTEM")
        crowd()  # Call the crowd monitoring function

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())