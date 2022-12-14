from PyQt5 import QtCore, QtGui, QtWidgets
from hashlib import sha256

class Ui_Form(object):
    
    def action(self):
        # Récupérer les champs de saisies
        fichier = self.lineEdit.text()
        sortie = self.lineEdit_2.text()
        cle = self.lineEdit_3.text()
        #Programme de cryptage/décryptage
        cles = sha256(cle.encode('utf-8')).digest()
        with open(fichier,'rb') as f_fichier:
            with open(sortie,'wb') as f_sortie:
                i = 0
                while f_fichier.peek():
                    c = ord(f_fichier.read(1))
                    j = i % len(cles)
                    b = bytes([c^cles[j]])
                    f_sortie.write(b)
                    i = i + 1
        #Fin du programme de cryptage/décryptage
# Génération de l'UI        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/Cryptage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.widget.setStyleSheet("background:qlineargradient(spread:reflect, x1:1, y1:0, x2:0.46, y2:1, stop:0 rgba(75, 158, 160, 243), stop:1 rgba(220, 220, 220, 220))")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(130, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(238, 238, 238);\n"
"background:none;\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:none;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:none;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:none;")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(190, 250, 161, 31))
        self.pushButton.clicked.connect(self.action)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 100, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 140, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 180, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cryptage"))
        self.label.setText(_translate("Form", "Cryptage"))
        self.label_2.setText(_translate("Form", "Fichier à crypter"))
        self.label_3.setText(_translate("Form", "Nom du fichier de sortie"))
        self.label_4.setText(_translate("Form", "Clé de chiffrement"))
        self.pushButton.setText(_translate("Form", "Chiffrement"))
#Fin de l'UI

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
