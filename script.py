#IMPORT
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from ui_design3 import Ui_Form



#INICHIALAYS
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

#LOOGIC

def zero():
   ui.lineEdit.setText(ui.lineEdit.text()+"0")
   
def one():
   ui.lineEdit.setText(ui.lineEdit.text()+"1")

def tow():
   ui.lineEdit.setText(ui.lineEdit.text()+"2")

def tree():
   ui.lineEdit.setText(ui.lineEdit.text()+"3")

def foor():
   ui.lineEdit.setText(ui.lineEdit.text()+"4")

def five():
   ui.lineEdit.setText(ui.lineEdit.text()+"5")

def six():
   ui.lineEdit.setText(ui.lineEdit.text()+"6")

def sevn():
   ui.lineEdit.setText(ui.lineEdit.text()+"7")

def eight():
   ui.lineEdit.setText(ui.lineEdit.text()+"8")

def nine():
   ui.lineEdit.setText(ui.lineEdit.text()+"9")


def fasila():
   ui.lineEdit.setText(ui.lineEdit.text()+",")

def dellet():
     ui.lineEdit.setText(ui.lineEdit.text()[0:-1])



def ac():
    ui.lineEdit.setText("")
   
def plus():
    ui.lineEdit.setText(ui.lineEdit.text()+"+")

def moins():
    ui.lineEdit.setText(ui.lineEdit.text()+"-")

def multip():
    ui.lineEdit.setText(ui.lineEdit.text()+"*")

def division():
    ui.lineEdit.setText(ui.lineEdit.text()+"/")

def plus():
    ui.lineEdit.setText(ui.lineEdit.text()+"+")

def egal():
    ui.lineEdit.setText(str(eval(ui.lineEdit.text())))

def porcent():

    ui.lineEdit.setText(ui.lineEdit.text()+"%")

def plus():
    ui.lineEdit.setText(ui.lineEdit.text()+"+")

#Conection

ui.pushButton_19.clicked.connect(zero)
ui.pushButton_17.clicked.connect(one)
ui.pushButton_16.clicked.connect(tow)
ui.pushButton_15.clicked.connect(tree)
ui.pushButton_14.clicked.connect(foor)
ui.pushButton_13.clicked.connect(five)
ui.pushButton_12.clicked.connect(six)
ui.pushButton_9.clicked.connect(sevn)
ui.pushButton_10.clicked.connect(eight)
ui.pushButton_11.clicked.connect(nine)
ui.pushButton_8.clicked.connect(ac)
ui.symbol_6.clicked.connect(plus)
ui.symbol_5.clicked.connect(egal)
ui.symbol_9.clicked.connect(division)
ui.symbol_8.clicked.connect(multip)                  
ui.symbol_7.clicked.connect(moins)                  
ui.pushButton_18.clicked.connect(fasila)     
ui.pushButton_6.clicked.connect(porcent)                  
ui.pushButton_7.clicked.connect(dellet)                  













sys.exit(app.exec_())
